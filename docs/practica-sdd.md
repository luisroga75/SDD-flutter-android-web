# Práctica docente de principio a fin

[Inicio](../README.md). Esta actividad conserva el método del material original; cambia la CLI Python por Flutter, no el papel de la persona que revisa. La instalación técnica puede comprobarse con una app de humo antes de definir el producto real.

## Antes de empezar

- Abre la carpeta de tu proyecto, vacía o con una app existente; no abras el repositorio de la skill como si fuera tu aplicación.
- Usa `$flutter-sdd` en Codex o `/flutter-sdd` en Claude Code. Tras invocarla, los mensajes por fase son iguales.
- Pide modo docente. Si tu agente ofrece modo de planificación, úsalo para revisar antes de escribir; `plan.md` es un documento distinto. No pidas guardar archivos mientras el entorno tenga prohibida la escritura.
- Acordad plataformas, primer recorrido y qué significa terminar. No es necesario elegir proveedor de nube antes de saber si necesitas nube.

## Secuencia y revisión

| Fase | Mensaje que puedes dar | Qué debes revisar tú |
| --- | --- | --- |
| Descubrimiento | Ayúdame a definir una agenda de estudio; pregunta de una en una. | Que el problema sea el tuyo, no uno inventado |
| Constitución | Propón principios verificables y espera mi revisión. | Datos, simplicidad, pruebas, alcance y lenguaje |
| Instrucciones | Prepara AGENTS/CLAUDE según mi agente. | Contexto, comandos reales, límites y cierre de tareas |
| Spec | Redacta 001 con EARS, sin diseño técnico. | Qué sucede con cada entrada, error y exclusión |
| QA | Detecta ambigüedades y contradicciones, no corrijas aún. | Hallazgos con ejemplos, no vaguedades |
| Clarificación | Resolvamos los hallazgos, una pregunta cada vez. | Decisiones incorporadas y dudas que siguen abiertas |
| Plan | Diseña el cómo con alternativas y cobertura RF. | Que cada componente tenga motivo; compatibilidad real |
| Tareas | Divide el plan por resultados pequeños y dependencias. | Hecho cuando y comprobaciones realmente ejecutables |
| Implementación | Implementa solo T1; test primero y detente al terminar. | Diff, prueba roja/verde pertinente, ausencia de extras |
| Validación | Recorre cada RF/RNF y muestra evidencia por destino. | Lo que pasó, falló y no pudo probarse |
| Evolución | Este comportamiento cambia: primero modifica el contrato. | Impacto en datos, regresión y aceptación |

La entrevista tiene hasta seis preguntas por ciclo, no seis respuestas inventadas. Si el producto es grande, trabaja por incrementos. Revisa también planes y tareas antes de ejecutarlos, no solo constitución y spec.

Los [prompts de definición](../shared/references/prompts-definicion.md), [desarrollo](../shared/references/prompts-desarrollo.md) y [GitHub](../shared/references/git-github.md) contienen las versiones completas. Puedes pedir «Muéstrame P7 adaptado a esta app sin ejecutarlo».

## Varias especificaciones

Primero podrías crear `001-lista`, luego `002-persistencia` y después `003-sincronizacion`, **solo si esos resultados fueron acordados**. No significa que toda práctica deba tener nube o persistencia.

Cada carpeta tiene su contrato, plan y tareas. Cambia la constitución solo al cambiar principios globales. Conserva IDs y dependencias entre specs. Si usas `specs/plan.md`, que sea un mapa de estado, no otro contrato independiente.

El [ejemplo de agenda](../examples/agenda-estudio) muestra una spec coherente con decisiones ficticias y tareas pendientes. No contiene app ni tests Flutter. El objetivo del ejercicio es reconstruir el proceso con decisiones propias, no copiar el ejemplo y afirmar que ya está validado.

## Git y GitHub en clase

Comprueba antes la identidad con `git config user.name` y `git config user.email`. Si falta, configura tus datos (globalmente solo si quieres usarlos en todos los repositorios). Usa dirección noreply de tu cuenta si necesitas privacidad en commits.

Pide al agente:

```text
Prepara control de versiones para esta app, separado del repositorio de la skill.
Comprueba estado, historial y .gitignore. Quiero commits revisables por spec/tarea.
No publiques todavía: primero muéstrame los archivos y verifica que no hay claves,
firmas, datos personales ni configuración local del SDK. Conserva pubspec.lock.
```

Cuando decidas publicar, indica cuenta, nombre y visibilidad. Una tarea de push no implica merge ni publicación en tiendas. Una tarea de PR debe describir pruebas reales y limitaciones. La estrategia puede ser una rama por spec, sin imponer un proceso complejo a un ejercicio pequeño.

## Evidencia para entregar

Entrega los documentos, diff/código, pruebas y un registro de versión Flutter y destinos usados. Los comandos candidatos son `flutter analyze`, `flutter test`, formato y build/ejecución del destino acordado, más integración cuando corresponda. Las capturas ayudan a demostrar UI, no sustituyen pruebas de datos ni reglas.

Para ejecutar el auditor desde la raíz del repositorio **de la skill**, sustituyendo la ruta por la raíz de tu app:

```sh
python3 codex/flutter-sdd/scripts/audit_sdd.py /ruta/a/mi_app --agent codex --ready
```

Claude: cambia la carpeta a `claude-code` y usa `--agent claude` (o `both` si exiges los dos archivos). Windows: usa `python` o `py`. Sin `--ready` admite carencias de borrador como avisos.

## Rúbrica breve para el profesor

1. ¿El alumno puede explicar problema, exclusiones y decisiones, sin leer una respuesta de IA como sustituto de comprensión?
2. ¿La spec se puede verificar sin conocer cómo se implementó?
3. ¿El plan y cada tarea trazan requisitos sin inventar alcance?
4. ¿Las pruebas examinan errores además del camino feliz y hay revisión de código?
5. ¿Se distinguen destinos probados, pendientes y no soportados?
6. ¿Un cambio o bug deja contrato, implementación y evidencia coherentes?

El auditor solo ayuda con estructura; no evalúa todos estos criterios. No es un sistema automático de calificaciones.
