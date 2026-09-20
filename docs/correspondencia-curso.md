# Correspondencia con el vídeo y su transcripción

Fuente: [curso de MoureDev](https://www.youtube.com/watch?v=5HaOxAAA5qI), [repositorio Hello SDD](https://github.com/mouredev/hello-sdd) y el documento «Transcripción - El fin del Vibe Coding.md» aportado por el usuario. Se leyó completo el 20 de septiembre de 2026. Los tiempos son los de esa transcripción, basada en subtítulos automáticos: pueden existir errores de términos. No se redistribuye la transcripción ni se afirma haber verificado cada palabra del audio.

| Tiempo aproximado | Enseñanza que se conserva | Aplicación en esta entrega |
| --- | --- | --- |
| 4:00–5:02 | Fundamentos antes que una herramienta concreta | Un método compartido, adaptadores Codex y Claude |
| 9:02–11:00 | La especificación comunica intención; Markdown estructura el contrato | Plantilla de spec y documentos versionables |
| 17:01–21:00 | Planificar, analizar y diseñar antes de programar | Descubrimiento, principios, spec y plan antes de tareas de código |
| 28:01–32:01 | Spec-first y spec-anchored conservan importancia del código | No se sustituye revisión de código por generación automática |
| 42:02–47:00 | Instrucciones breves, anatomía de spec y EARS | Contexto, RF/RNF, errores, exclusiones, fin y dudas |
| 48:01 y 1:05:01–1:07:00 | Modo plan y revisión humana | Revisar propuestas; guardar solo con permisos apropiados |
| 56:00–1:10:01 | AGENTS, constitución y puente a Claude; orden inicial flexible | AGENTS para Codex; importador CLAUDE para el recorrido nuevo de Claude |
| 1:11:02–1:18:01 | Una pregunta cada vez, hasta seis, numeración y exclusiones | P4 y carpetas NNN, sin deducir un producto entero |
| 1:23:01–1:25:01 | Clarificación iterativa antes del plan | QA de solo detección seguido de incorporación de respuestas |
| 1:26:00–1:29:02 | Diseño técnico y alternativas | Flutter/Dart, datos, estado, widgets y tests con RF |
| 1:30:00–1:36:00 | Tareas pequeñas, ordenadas, trazables y revisables | Tn, dependencias, Hecho cuando y evidencia |
| 1:37:01–1:42:00 | Tests primero, implementación acotada, parada según encargo | Una tarea o conjunto expresamente encargado, sin ampliarlo |
| 1:39:02–1:40:03 | Sincronizar documentos y corregir bugs con trazabilidad | Cambio del contrato o tarea de regresión, según el caso |
| 1:42:00–1:46:00 | Validar RF y repetir por nuevas funcionalidades | Veredicto por destino y nuevas specs sin rehacer constitución |
| 1:48:00–1:54:02 | Skills como procedimientos reutilizables | Prompts P0–P17 ejecutables por la skill y visibles a petición |
| 1:55:01–1:56:02 | Agentes especializados y MCP como extensión | No se hacen obligatorios ni se instalan sin necesidad |
| 1:57:00–2:01:00 | Persona responsable de revisar documentos, código y tests | Modo docente, rúbrica y ejercicio con decisiones propias |

## Adaptaciones explícitas

La app Python del curso no se traduce mecánicamente. El almacenamiento, las bibliotecas y las restricciones de esa app no son mandatos para cualquier Flutter. Se acuerdan por producto. Las comprobaciones de pytest se sustituyen por las apropiadas de Flutter, sin confundir unitarios, widgets e integración nativa.

Git/GitHub, distribución privada a alumnos, instalador y auditor son ampliaciones pedidas por el usuario. El auditor no demuestra la corrección de los tests ni de la spec. Una skill tampoco garantiza resultados deterministas entre modelos.

Se conserva revisión por fases como experiencia docente. Si la persona autoriza varias fases o varias tareas, la skill puede avanzar en ese alcance; no exige reiterar una autorización ya dada. Las decisiones materiales pendientes siguen requiriendo respuesta. Las afirmaciones del vídeo sobre mercado, precios o modelos no son requisitos técnicos de esta entrega.
