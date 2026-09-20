# Instrucciones del proyecto

Guardar como AGENTS.md para Codex o CLAUDE.md para Claude Code. Sustituir marcadores y retirar esta nota al adaptar.

## Contexto y alcance

{{PRODUCTO_REAL_Y_PLATAFORMAS_ACORDADAS}}

Principios: [docs/constitution.md](docs/constitution.md). Localizar spec activa en `specs/` y leer sus `spec.md`, `plan.md` y `tasks.md`. No fijar esta instrucción a una sola spec.

## Trabajo SDD

- Comportamiento y exclusiones en spec antes de código; diseño en plan.
- Conservar IDs, supuestos visibles y acuerdos. Respetar la revisión por fases acordada.
- Implementar solo la tarea/alcance solicitado y no marcar sin evidencia.
- Revisar cambios existentes y no sobrescribir trabajo ajeno.

## Flutter y comprobaciones

{{MAPA_REAL_DE_LIB_TEST_INTEGRATION_TEST_Y_DESTINOS}}

{{CONVENCIONES_DE_DART_UI_ESTADO_DATOS_Y_ACCESIBILIDAD}}

{{COMANDOS_DE_FORMATO_ANALISIS_TEST_Y_BUILD_CON_ESTADO_VERIFICADO_O_PENDIENTE}}

No declarar una plataforma probada si no se ejecutó. Distinguir falta de entorno de fallo de producto. No instalar paquetes ni actualizar Flutter fuera del encargo.

## Git y datos

{{FLUJO_ACORDADO_DE_RAMAS_COMMITS_PR_Y_DESTINO}}

No versionar secretos, datos personales de alumnos, SDK local ni firmas. Commit, push, PR, merge y publicación son acciones distintas dentro del alcance autorizado.
