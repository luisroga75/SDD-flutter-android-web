import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


installer = module("install_skill")
builder = module("sync_packages")


class DistributionTests(unittest.TestCase):
    def test_shared_resources_match_packages(self):
        self.assertEqual(builder.sync(check=True), [])

    def test_install_each_agent_self_contained(self):
        with tempfile.TemporaryDirectory() as folder:
            for agent in ("codex", "claude-code"):
                dest = installer.install(agent, home=folder)
                source = ROOT / agent / "flutter-sdd"
                self.assertEqual(builder.files(source).keys(), builder.files(dest).keys())
                for rel, path in builder.files(source).items():
                    self.assertEqual(path.read_bytes(), (dest / rel).read_bytes())
                self.assertTrue((dest / "scripts/audit_sdd.py").exists())

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as folder:
            installer.install("codex", home=folder, dry_run=True)
            self.assertEqual(list(Path(folder).iterdir()), [])

    def test_existing_installation_preserved(self):
        with tempfile.TemporaryDirectory() as folder:
            dest = installer.install("codex", home=folder)
            entry = dest / "SKILL.md"
            entry.write_text("user changes", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                installer.install("codex", home=folder)
            self.assertEqual(entry.read_text(), "user changes")

    def test_project_scope_only_changes_skill_folder(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            (project / "keep.txt").write_text("keep", encoding="utf-8")
            dest = installer.install("claude-code", "project", project)
            self.assertEqual(dest, project / ".claude/skills/flutter-sdd")
            self.assertEqual((project / "keep.txt").read_text(), "keep")

    def test_scope_requires_existing_project(self):
        with self.assertRaises(ValueError):
            installer.install("codex", "project")

    def test_sync_detects_changed_package(self):
        import shutil
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(ROOT / "shared", root / "shared")
            for agent in builder.AGENTS:
                shutil.copytree(ROOT / agent, root / agent)
            target = root / "codex/flutter-sdd/references/metodo.md"
            target.write_text("divergent", encoding="utf-8")
            self.assertTrue(builder.sync(root, check=True))
            self.assertEqual(target.read_text(), "divergent")


if __name__ == "__main__":
    unittest.main()
