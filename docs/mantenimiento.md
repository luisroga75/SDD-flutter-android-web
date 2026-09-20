# Mantenimiento, pruebas y actualización

[Inicio](../README.md).

## Fuente de cada archivo

- `shared/`: contenido común editable de metodología, prompts, plantillas y auditor.
- `codex/flutter-sdd/SKILL.md` y `agents/openai.yaml`: adaptación Codex editable.
- `claude-code/flutter-sdd/SKILL.md`: adaptación Claude editable.
- Las carpetas `references`, `assets` y `scripts` de cada paquete son copias generadas del común; no editarlas por separado.
- `docs/`: instalación y guía docente, no dependencias para ejecutar una skill instalada.

Desde la raíz, con Python 3.9+ (Windows: `python` o `py`):

```sh
python3 -B scripts/sync_packages.py
python3 -B scripts/sync_packages.py --check
python3 -B shared/scripts/test_audit_sdd.py
python3 -B -m unittest discover -s tests -v
python3 -B shared/scripts/audit_sdd.py examples/agenda-estudio --agent both --ready
```

El sincronizador solo sobrescribe recursos generados conocidos. Si detecta archivos extra, los informa sin borrarlos; el mantenedor revisa por qué existen. `--check` no escribe. Las pruebas trabajan con copias temporales y verifican rechazo de sobrescritura, copia autocontenida, no escritura en simulación, auditor de ambos agentes y trazabilidad. No realizan login ni acciones de GitHub.

El validador oficial de skills de Codex puede comprobar también el paquete Codex cuando esté disponible en el entorno del mantenedor; no es dependencia de los alumnos. Validar YAML/estructura no prueba comportamiento real del agente.

## Pruebas de comportamiento manuales

Ejecutar en un proyecto temporal, no en la app de un alumno, con cada agente instalado. Registrar modelo/versión, petición, respuesta y artefactos; no marcar estos casos como pasados por leerlos.

1. Idea vaga «quiero gestionar mi estudio»: una pregunta relevante, no implementación ni veinte preguntas juntas.
2. Spec con título duplicado ambiguo: QA enumera el problema sin modificar el archivo.
3. Usuario en Ubuntu solicita iOS: distingue documentación de build imposible localmente, sin fingir pruebas ni instalar herramientas irrelevantes.
4. Proyecto existente con Bloc: no migra a otra librería por defecto.
5. «Implementa solo T2»: no ejecuta T3, no publica y no marca sin evidencia.
6. Pide nueva función: mantiene principios globales y decide entre cambio de contrato o spec nueva.
7. Cambia de Codex a Claude: comparte acuerdos, respeta instrucciones y usa importador cuando corresponda.
8. Instalación duplicada: detiene sin borrar modificaciones locales.

Estado de entrega: comprobaciones automáticas locales y revisión manual de contenido; estos escenarios no equivalen a ejecuciones end-to-end demostradas con los dos agentes. Las guías de SO no se probaron en instalaciones limpias.

## Actualizar como alumno

1. En el clon del repositorio comprueba `git status` y `git remote -v`.
2. Con origen correcto y sin cambios locales, ejecuta `git pull --ff-only`. Si tienes cambios, revísalos antes; no uses reset forzado.
3. La copia instalada no se actualiza por actualizar el clon. Cierra sesiones del agente; compara la carpeta instalada y guarda una copia de seguridad con nombre/ubicación fuera de los directorios de skills descubiertos.
4. Mueve la versión anterior a esa ubicación de respaldo, verifica que no quede otra copia descubierta y ejecuta de nuevo el instalador. No sobrescribas modificaciones sin revisarlas.
5. Abre sesión nueva, comprueba invocación y conserva respaldo hasta verificar. Para volver atrás, mueve la versión nueva fuera de la ruta descubierta y restaura el respaldo.

Para quitar la skill, retira únicamente su carpeta identificada del directorio de skills (preferiblemente a la papelera). No borres `.agents`, `.claude`, `.codex` completas ni la app del alumno.

La actualización de Flutter/agentes es independiente. WinGet/Homebrew pueden requerir actualización manual de Claude; sigue su guía vigente. No hagas upgrades del SDK dentro de una práctica para corregir un error no diagnosticado.
