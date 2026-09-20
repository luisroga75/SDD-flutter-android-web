# Procedencia y alcance

Revisión: 20 de septiembre de 2026. Deriva del encargo y la skill Android/Kotlin anterior del mismo autor, con redacción nueva para Flutter/Dart y dos agentes. Se reutiliza el auditor estructural propio con adaptación de archivos de instrucciones.

Base metodológica proporcionada por el usuario: [Hello SDD de MoureDev](https://github.com/mouredev/hello-sdd) y [vídeo del curso](https://www.youtube.com/watch?v=5HaOxAAA5qI). Se volvieron a consultar la [skill de specs](https://github.com/mouredev/hello-sdd/tree/main/habits-cli/.claude/skills/spec-generator), [prompts](https://github.com/mouredev/hello-sdd/blob/main/samples/prompts.md), plantilla y [práctica](https://github.com/mouredev/hello-sdd/blob/main/habits-cli/README.md). La adaptación anterior contrastó también constitución, AGENTS y pizarra de la revisión `358dfe85a818bccdd839f78e804668b3ebaa10b5`.

El usuario aportó el documento «Transcripción - El fin del Vibe Coding.md», leído completo (marcas de 0:00 a 2:03:00). Procede de subtítulos automáticos revisados y advierte de errores de términos. Se contrastaron sus explicaciones con los archivos del curso; no se afirma haber verificado el audio palabra por palabra. No se redistribuye la transcripción completa. Las ampliaciones Flutter, GitHub, auditoría y distribución son propias de este encargo. El proyecto fuente declara Apache-2.0; no se incorporan sus archivos originales como parte de estos paquetes.

## Correspondencia docente

| Material original | Aplicación Flutter |
| --- | --- |
| Constitución y contexto del agente | Principios compartidos y AGENTS/CLAUDE según herramienta |
| Entrevista acotada, una pregunta por vez | Decisiones visibles de comportamiento y plataforma |
| Spec de qué/por qué, EARS y exclusiones | Contrato independiente de widgets y paquetes |
| QA detecta antes de resolver | P5 y clarificación P6 |
| Plan con alternativas y RF | Flutter/Dart, capacidades por destino y pruebas |
| Tareas pequeñas, test primero, una tarea | P8/P10 y evidencia, sin empezar la siguiente |
| Recorrer RF y cambiar contrato primero | P11/P12, diferencias de plataforma explícitas |

La autorización explícita de varias fases puede permitir avanzar sin confirmaciones repetidas; no sustituye decisiones materiales por silencio. El modo docente mantiene la revisión de constitución y spec.

Marcas relevantes de la transcripción: 28:01–32:01 (spec-first/anchored/source), 42:02–47:00 (instrucciones, EARS y ciclo), 1:04:00–1:10:01 (constitución, orden flexible, modo plan e importador CLAUDE), 1:11:02–1:25:01 (entrevista y QA), 1:26:00–1:38:01 (plan, tareas y TDD), 1:39:02–1:46:00 (sincronización, bugs y nuevas specs), 1:48:00–1:56:02 (skills y ampliaciones opcionales), 1:57:00–2:01:00 (revisión humana y ejercicio). No se convierte una recomendación de modelo o una afirmación comercial del vídeo en requisito de instalación.

## Documentación técnica oficial

- [Codex skills](https://learn.chatgpt.com/docs/build-skills), [extensión](https://learn.chatgpt.com/docs/codex/ide).
- [Claude Code skills](https://code.claude.com/docs/en/skills), [CLAUDE.md e imports](https://code.claude.com/docs/en/memory), [instalación](https://code.claude.com/docs/en/setup).
- [Instalar Flutter](https://docs.flutter.dev/install), [instalación manual](https://docs.flutter.dev/install/manual), [arquitectura](https://docs.flutter.dev/app-architecture/guide), [pruebas](https://docs.flutter.dev/testing/overview).
- [Android](https://docs.flutter.dev/platform-integration/android/setup), [iOS](https://docs.flutter.dev/platform-integration/ios/setup), [web](https://docs.flutter.dev/platform-integration/web/setup), [Windows](https://docs.flutter.dev/platform-integration/windows/setup), [macOS](https://docs.flutter.dev/platform-integration/macos/setup), [Linux](https://docs.flutter.dev/platform-integration/linux/setup).

Verifica compatibilidad al aplicar la skill; esta referencia no fija una combinación universal de versiones.
