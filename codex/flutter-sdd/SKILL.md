---
name: flutter-sdd
description: Guía el desarrollo SDD de aplicaciones Flutter y Dart en Codex, desde la entrevista hasta specs, planes, tareas, implementación y validación con Git/GitHub. Úsala para iniciar o continuar ese ciclo, no para preguntas aisladas de Dart.
---

# Flutter SDD para Codex

Invocación: `$flutter-sdd`. Trabaja en el proyecto del usuario, no en esta carpeta. Lee los AGENTS.md aplicables y la constitución antes de proponer cambios. Genera `AGENTS.md` como instrucciones del proyecto; no generes CLAUDE.md salvo que se pida compatibilidad con ambos agentes. No presupongas herramientas de Claude ni un conector GitHub: usa las capacidades realmente disponibles.

## Contrato del flujo

Conserva el método de entrevista → constitución → spec → revisión/clarificación → plan → tareas → implementación → validación → cambio del contrato. Lee [el método](references/metodo.md) al iniciar o reanudar. Distingue una plantilla inicial de una función implementada.

- Una pregunta significativa cada vez; hasta seis por ciclo de spec. Sugiere una respuesta razonada cuando ayude, pero no conviertas una hipótesis en una decisión del usuario. Un producto amplio se divide en ciclos, no se completa inventando respuestas.
- La spec expresa comportamiento y motivo; las decisiones Flutter, datos, paquetes y clases pertenecen al plan. Requisitos verificables en EARS; fuera de alcance explícito; incógnitas marcadas `[NECESITA ACLARACIÓN: pregunta]`.
- Modo docente por defecto: presenta constitución y spec para revisión antes de avanzar de fase. Si el usuario ya encargó varias fases o delegó decisiones, aprovecha esa autorización sin pedirla de nuevo; conserva dudas materiales visibles. Pedir documentación no autoriza implementación, commit ni publicación.
- Implementar una tarea significa solo esa tarea; pruebas primero cuando sean pertinentes y evidencia antes de marcarla. No inventes tests ejecutados, disponibilidad de dispositivos ni compatibilidad multiplataforma.
- Antes de cambiar comportamiento, actualiza el contrato y evalúa impacto en plan, tareas y pruebas. Un encargo de revisión es de solo lectura salvo indicación contraria.

## Elegir recursos

Lee únicamente los necesarios, completos, antes de ejecutar la fase:

| Necesidad | Recursos |
| --- | --- |
| Descubrir, entrevistar, definir principios o varias specs | [Método](references/metodo.md), [P0–P6](references/prompts-definicion.md) |
| Plan, tareas, implementación, aceptación o reanudar | [P7–P13](references/prompts-desarrollo.md), [criterios Flutter](references/flutter-dart.md) |
| Repositorio, commits, PR, CI o entregas | [P14–P17](references/git-github.md) |
| Redactar documentos | Plantilla correspondiente de [assets/templates](assets/templates) |
| Verificar trazabilidad documental | [Auditor](references/auditoria.md), `scripts/audit_sdd.py` |
| Explicar procedencia o límites del curso | [Fuentes](references/fuentes.md) |

Los prompts son procedimientos reutilizables: adáptalos y ejecútalos cuando te lo pidan, no te limites a entregarlos para que la persona los copie. Si solicita el prompt, muéstralo completo y adaptado sin ejecutarlo.

## Archivos de salida

```text
AGENTS.md
docs/constitution.md
specs/001-funcionalidad/{spec.md,plan.md,tasks.md}
specs/002-otra-funcionalidad/{spec.md,plan.md,tasks.md}
```

`specs/plan.md` es un mapa global opcional. Respeta rutas explícitas y convenciones existentes; no dupliques el contrato en raíz y carpetas. Una `/` inicial al hablar de documentos suele significar raíz del proyecto: confirma antes de escribir fuera de él. Para el formato canónico usa el mayor número existente más uno, sin renumerar specs antiguas.

## Particularidades Flutter

Pregunta plataformas objetivo y primera plataforma de demostración; no asumas todas. Revisa `pubspec.yaml`, `pubspec.lock`, SDK, carpetas de plataforma, tests e instrucciones existentes. Conserva el gestor de estado y diseño razonables; no impongas Riverpod, Bloc, Firebase, navegación avanzada ni arquitectura por capas a una práctica pequeña. Flutter no garantiza que un plugin funcione en todas las plataformas ni ejecución de fondo idéntica.

Compara `flutter doctor -v` con los destinos acordados. Una alerta de Xcode en un flujo solo Android no bloquea la redacción. Nunca pruebes iOS localmente en Windows/Linux ni declares validada una plataforma no ejecutada. No actualices SDK, sistema operativo ni paquetes fuera del encargo.

## Cierre de cada fase

Resume documentos/código afectados, decisiones frente a supuestos, requisitos cubiertos, comprobaciones reales, pendientes y próxima acción. En el modo docente espera revisión cuando corresponda; al ejecutar un alcance más amplio continúa solo lo ya autorizado.
