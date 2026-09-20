# Auditor documental opcional

Python 3.9+ y biblioteca estándar, sin pip. Desde la carpeta instalada de la skill:

```sh
python3 scripts/audit_sdd.py /ruta/a/la/app --agent codex --ready
python3 scripts/audit_sdd.py /ruta/a/la/app --agent claude --ready --json
```

En Windows usa `python` o `py` según tu instalación. `--agent both` exige ambos archivos; `auto` detecta los presentes. Un CLAUDE.md con una línea `@AGENTS.md` obliga a comprobar también el archivo importado. No es un resolutor general de imports de Claude.

Comprueba documentos faltantes/vacíos, marcadores `{{...}}` y aclaraciones pendientes, numeración de specs, RF/RNF duplicados, referencias inexistentes, cobertura textual en planes/tareas, dependencias y ciclos entre tareas. Una casilla completa exige un campo de evidencia no pendiente.

Formato esperado: carpetas `specs/NNN-nombre`, requisitos `- RF-1: ...` o `- RNF-1: ...`, tareas `- [ ] T1. ...`, campos RF, Dependencias, Hecho cuando, Verificación y Evidencia. Los IDs son locales a cada spec; se califican para referencias cruzadas. Los requisitos `[RETIRADO]` no se exigen en cobertura.

Sin `--ready`, las carencias de borrador son avisos; con él pasan a errores. Retorno 0 significa ausencia de errores estructurales y 1 indica errores. Esto no es prueba de cumplimiento funcional, EARS correcto, correspondencia semántica, realidad de la evidencia ni cobertura de plataformas. No ejecuta Flutter, no usa red ni escribe en la app.

Si el usuario usa otra estructura, conserva esa elección: revisión manual en vez de reformatear para el auditor. Pruebas del comprobador: `python3 -B scripts/test_audit_sdd.py`, en directorios temporales.
