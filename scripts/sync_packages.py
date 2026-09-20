#!/usr/bin/env python3
"""Copy shared resources into self-contained skills; --check never writes."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PARTS = ("references", "assets", "scripts")
AGENTS = ("codex", "claude-code")


def files(folder):
    return {p.relative_to(folder): p for p in folder.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"}


def sync(root=ROOT, check=False):
    problems = []
    for agent in AGENTS:
        package = root / agent / "flutter-sdd"
        if not (package / "SKILL.md").is_file():
            raise ValueError(f"Falta entrada de paquete: {package}")
        for part in PARTS:
            source = root / "shared" / part
            target = package / part
            expected, actual = files(source), files(target)
            for relative in actual.keys() - expected.keys():
                problems.append(f"Recurso extra; revisar manualmente: {target / relative}")
            for relative, path in expected.items():
                dest = target / relative
                if path.is_symlink() or dest.is_symlink():
                    raise ValueError("No se admiten symlinks en recursos de distribución")
                if not dest.is_file() or path.read_bytes() != dest.read_bytes():
                    if check:
                        problems.append(f"Recurso desincronizado: {dest}")
                    else:
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copyfile(path, dest)
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    problems = sync(check=args.check)
    for problem in problems:
        print(problem)
    print("Paquetes sincronizados" if not problems else "Revisar distribución")
    return bool(problems)


if __name__ == "__main__":
    raise SystemExit(main())
