# Instalar Codex o Claude Code y la skill

[Inicio](../README.md). La instalación del agente no instala Flutter; completa también la guía de tu sistema. Estas instrucciones cubren **agentes locales**, no la carga de archivos en una conversación web genérica.

## 1. Elegir agente

### Codex en VS Code

1. Instala VS Code siguiendo la guía del sistema.
2. En la [página oficial de Codex para IDE](https://learn.chatgpt.com/docs/codex/ide), sigue el enlace a la extensión publicada por **OpenAI**. Comprueba el publicador para evitar imitaciones.
3. Instálala y abre su panel; también puedes buscar **Codex: Open Codex Sidebar** en la paleta.
4. Completa el inicio de sesión con el método disponible para tu cuenta y confirma acceso. GitHub y Codex son autenticaciones distintas.
5. Abre la raíz de una app de confianza y solicita una inspección sin cambios para comprobar la conexión.

No necesitas Codex CLI además de la extensión. Si prefieres terminal, usa el instalador vigente de la [guía oficial de CLI](https://learn.chatgpt.com/docs/codex/cli), confirma `codex --version` y ejecuta `codex` desde tu app. Una aplicación de escritorio ya configurada puede trabajar con la misma carpeta local.

### Claude Code

Ruta recomendada aquí: CLI en la terminal, incluida la de VS Code. Elige **un método** para no mantener instalaciones duplicadas. Los pasos se contrastaron con [Quickstart](https://code.claude.com/docs/en/quickstart) y [Setup](https://code.claude.com/docs/en/setup).

Windows PowerShell, con WinGet disponible:

```powershell
winget install Anthropic.ClaudeCode
```

Si WinGet no existe, instala/actualiza **App Installer** desde Microsoft o utiliza el instalador nativo enlazado en la guía oficial. Git for Windows ya instalado permite usar Git Bash; no ejecutes un comando de CMD como si fuera PowerShell.

macOS con Homebrew:

```zsh
brew install --cask claude-code
```

Ubuntu Bash: el instalador nativo oficial descarga y ejecuta un script. Si tu centro permite este procedimiento, revisa primero su origen; para inspeccionarlo antes de ejecutarlo puedes abrir la URL en el navegador. No lo ejecutes con `sudo`:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Sigue sus indicaciones de PATH (habitualmente `~/.local/bin`) y abre otra terminal. En el sistema elegido:

```text
claude --version
claude
```

Inicia sesión con una cuenta/método que permita Claude Code y acepta confianza solo para carpetas conocidas. No necesitas instalar Node.js con estas rutas nativas. No utilices flags para saltarte permisos. Los planes, cuotas y acceso dependen del proveedor y pueden cambiar; esta skill no proporciona acceso gratuito al servicio.

## 2. Acceso al repositorio privado

El profesor debe invitar al usuario GitHub del alumno desde la configuración de colaboradores de `luisroga75/flutter-sdd`. El alumno acepta la invitación con **su** cuenta. Este procedimiento no invita automáticamente a nadie.

Con GitHub CLI instalado:

```text
gh auth login --hostname github.com --git-protocol https --web
gh auth status
gh auth setup-git
gh repo view luisroga75/flutter-sdd
```

En la carpeta donde guardas herramientas (no dentro de otra app), sin una carpeta `flutter-sdd` previa:

```text
gh repo clone luisroga75/flutter-sdd
cd flutter-sdd
```

No pegues tokens ni códigos de acceso en archivos/prompts. Si aparece «not found», comprueba cuenta e invitación; no significa necesariamente que no exista. Alternativa sin `gh`: descarga el ZIP desde GitHub con sesión iniciada y descomprímelo; entra en su carpeta raíz antes del siguiente paso.

## 3. Instalador local sin sobrescritura

Requiere Python 3.9+ sin paquetes externos. Desde la raíz de este repositorio, elige variante:

**Windows:**

```powershell
python scripts/install_skill.py --agent codex --dry-run
python scripts/install_skill.py --agent codex
```

Para Claude sustituye `codex` por `claude-code`. Si solo existe el lanzador `py`, utiliza `py` en lugar de `python`.

**macOS / Ubuntu:**

```sh
python3 scripts/install_skill.py --agent codex --dry-run
python3 scripts/install_skill.py --agent codex
```

O elige `--agent claude-code`. El instalador copia una sola carpeta autocontenida, sin red ni comandos de sistema. Si el destino existe, se detiene y **no lo sobrescribe**. `--dry-run` muestra destino sin escribir.

Destinos personales:

- Codex: `~/.agents/skills/flutter-sdd`.
- Claude Code: `~/.claude/skills/flutter-sdd`.

En Windows `~` representa la carpeta de tu usuario; PowerShell la expone mediante `$HOME`. No cambies esa variable. Algunos entornos Codex descubren skills en `~/.codex/skills`; si ya tienes una instalación allí, conserva una única copia canónica y usa la instalación manual en esa ruta. [Ubicaciones Codex](https://learn.chatgpt.com/docs/build-skills), [ubicaciones Claude Code](https://code.claude.com/docs/en/skills).

Para instalar solo en una **app existente**, por ejemplo (sustituye la ruta por la real):

```sh
python3 scripts/install_skill.py --agent codex --scope project --project /ruta/a/mi_app --dry-run
python3 scripts/install_skill.py --agent codex --scope project --project /ruta/a/mi_app
```

Windows: `python scripts/install_skill.py --agent claude-code --scope project --project "C:\Proyectos\mi_app"`. Esto escribe `.agents/skills/flutter-sdd` o `.claude/skills/flutter-sdd` dentro de esa app, sin modificar sus instrucciones globales.

No instales la misma variante a la vez en varios ámbitos sin motivo. No subas el contenido privado con una app pública sin permiso.

## 4. Instalación manual sin Python

Con el explorador de archivos, activa la visualización de carpetas ocultas. Copia la carpeta completa:

- `codex/flutter-sdd` a la carpeta personal `.agents/skills/`.
- `claude-code/flutter-sdd` a `.claude/skills/`.

Créala si falta. El resultado debe ser `.../skills/flutter-sdd/SKILL.md`, no `.../skills/flutter-sdd/flutter-sdd/SKILL.md`. Incluye `references`, `assets`, `scripts` y, en Codex, `agents`. No copies `shared` por separado; sus recursos ya están incluidos.

Si existe una versión anterior, lee [actualización segura](mantenimiento.md) antes de sustituir archivos. No borres una instalación con modificaciones del alumno.

## 5. Confirmar descubrimiento

Abre una sesión nueva en la raíz de tu app Flutter. En Codex escribe `$flutter-sdd` (también puedes buscarla en `/skills` cuando esté disponible). En Claude Code escribe `/flutter-sdd`. Pide que lea la entrada y localice la referencia de entrevista y la plantilla de spec.

No ejecutes esas menciones como comandos del sistema. Un archivo Markdown abierto en el editor no basta para instalar una skill. Si falta, revisa ruta, duplicados y las restricciones administradas del centro; no intentes sortearlas.

En proyectos nuevos, la versión Codex prepara AGENTS.md. La versión Claude propone AGENTS.md común y CLAUDE.md importador, como la práctica del curso:

```markdown
@AGENTS.md
```

Si ya hay CLAUDE.md, se preserva y se acuerda dónde integrar las instrucciones. [Imports de Claude](https://code.claude.com/docs/en/memory).

Continúa con la [práctica SDD](practica-sdd.md).
