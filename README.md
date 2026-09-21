# Flutter SDD para Codex y Claude Code

Dos skills en español para aprender y aplicar **Spec-Driven Development con Flutter y Dart**. Siguen el método: entrevista, constitución, spec, clarificación, plan, tareas, tests, implementación, validación y evolución.

No es una app Flutter terminada ni un generador que decide el producto por ti. El agente propone y redacta; la persona revisa contratos, código y pruebas. Incluye 18 prompts, seis plantillas, auditor estructural y un ejemplo documental sin código implementado.

## Empieza aquí

1. Prepara tu equipo: [Windows](docs/windows.md), [macOS](docs/macos.md) o [Ubuntu](docs/ubuntu.md).
2. Configura solo los [destinos que necesitas](docs/plataformas.md): Android, web, iOS o escritorio.
3. Sigue la [instalación de Codex/Claude Code y de la skill](docs/agentes-e-instalacion.md).
4. Realiza la [práctica SDD guiada](docs/practica-sdd.md).

**Repositorio privado:** [luisroga75/flutter-sdd](https://github.com/luisroga75/flutter-sdd). Los alumnos necesitan invitación y aceptar el acceso. El profesor no comparte su token, contraseña ni cuenta de IA. Cada alumno usa su cuenta o el acceso autorizado por su centro.

## Dos versiones independientes

| | Codex | Claude Code |
| --- | --- | --- |
| Paquete a instalar | [codex/flutter-sdd](codex/flutter-sdd) | [claude-code/flutter-sdd](claude-code/flutter-sdd) |
| Invocación en el chat | `$flutter-sdd` | `/flutter-sdd` |
| Carpeta personal habitual | `~/.agents/skills/flutter-sdd` | `~/.claude/skills/flutter-sdd` |
| Instrucciones de la app | AGENTS.md | AGENTS.md + CLAUDE.md importador; respeta CLAUDE existente |

Cada carpeta contiene todas sus referencias, plantillas y scripts. No copies solo SKILL.md ni la raíz del repositorio como si fuera una skill. No necesitas instalar ambos agentes.

## Descarga e instalación rápida

Si ya tienes Git, GitHub CLI y Python 3.9+:

```sh
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
gh repo clone luisroga75/flutter-sdd
cd flutter-sdd
```

Elige **una** variante (macOS/Ubuntu; en Windows usa `python` o `py` en lugar de `python3`):

```sh
python3 scripts/install_skill.py --agent codex --dry-run
python3 scripts/install_skill.py --agent codex
```

O para Claude Code:

```sh
python3 scripts/install_skill.py --agent claude-code --dry-run
python3 scripts/install_skill.py --agent claude-code
```

El instalador no descarga software, no toca PATH ni sobrescribe instalaciones. Hay [instalación manual sin Python y por proyecto](docs/agentes-e-instalacion.md). Abre una sesión nueva en la raíz de **tu app**, no en este repositorio.

## Primer mensaje

Codex:

```text
Usa $flutter-sdd para definir mi app Flutter. Quiero seguir el modo docente
del curso, revisando cada fase. Lee lo que existe y hazme preguntas de una
en una, con opciones razonadas. No escribas código todavía. Ayúdame a
definir el problema, el MVP y la primera plataforma que vamos a demostrar.
```

Claude Code:

```text
/flutter-sdd Quiero definir mi app Flutter en modo docente, revisando cada
fase. Lee lo que existe y hazme preguntas de una en una, con opciones
razonadas. No escribas código todavía. Ayúdame a definir problema, MVP
y primera plataforma de demostración.
```

## Documentos que produce en tu app

```text
AGENTS.md
CLAUDE.md                 # solo para Claude/equipo mixto: @AGENTS.md
docs/constitution.md
specs/
  001-primera-funcion/
    spec.md
    plan.md
    tasks.md
  002-otra-funcion/
    spec.md
    plan.md
    tasks.md
```

Respeta estructuras existentes y rutas elegidas. `specs/plan.md` puede ser un mapa global opcional. No exige una nueva constitución para cada funcionalidad.

## Documentación y fuentes

- [Correspondencia con la transcripción del vídeo](docs/correspondencia-curso.md).
- [Guía de práctica para alumnos y profesor](docs/practica-sdd.md).
- [Errores frecuentes](docs/problemas.md).
- [Pruebas, mantenimiento y actualización](docs/mantenimiento.md).
- [Fuentes y límites](shared/references/fuentes.md).

Se consultó la transcripción completa aportada por el usuario; procede de subtítulos automáticos y se contrastó con el repositorio del curso. No se redistribuye ese texto. Flutter, GitHub, paquetes para dos agentes y el auditor son adaptaciones de este proyecto, no funcionalidades atribuidas al vídeo.

## Verificaciones y límites

Pruebas locales del auditor e instalador y comprobación de sincronización de los paquetes; consulta [cómo repetirlas](docs/mantenimiento.md). El ejemplo documental pasa la comprobación estructural, pero **no es una aplicación implementada ni probada**.

Las guías se contrastaron con documentación oficial el 20 de septiembre de 2026. No se han realizado instalaciones limpias en Windows/macOS/Ubuntu ni ejecuciones end-to-end de ambos agentes. No se garantizan resultados idénticos entre modelos ni precios o cuotas fijos.

No se asigna una licencia pública de reutilización en esta entrega privada. El acceso docente autorizado no equivale a permiso de redistribución pública de los materiales de terceros.
