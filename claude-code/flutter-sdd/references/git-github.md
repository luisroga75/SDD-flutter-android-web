# P14–P17: versionado, CI y entregas

Git es parte del trabajo cuando se solicita; nunca una consecuencia automática de entrevistar. Verifica estado, raíz, rama, remotos, archivos preparados y cuenta autenticada antes de escribir. No mezcles el repositorio de la skill con el de la app del alumno.

## P14. Preparar el repositorio

```text
Prepara Git/GitHub para {app Flutter} dentro del alcance {local/publicación}.
Inspecciona si ya existe Git y conserva historial/cambios. Si falta destino,
pregunta propietario, nombre y visibilidad; un repositorio privado necesita
invitaciones para alumnos. No cambies visibilidad por conveniencia.
Revisa .gitignore generado por Flutter y particularidades del proyecto. Conserva
pubspec.lock en aplicaciones para reproducibilidad. Excluye cachés, builds,
credenciales, archivos locales del SDK y material de firma. No ignores a ciegas
toda la configuración nativa ni todos los lockfiles. Revisa el diff antes del add.
Propón una rama por spec cuando aporte, o flujo simple para una práctica pequeña.
No publiques ni invites usuarios que no estén autorizados e identificados.
```

## P15. Commit, push y PR

```text
Versiona {alcance concreto}. Comprueba estado y diff; selecciona archivos por
relación con la tarea. Separa documentación de código cuando ayude a revisarlos.
Menciona la spec/Tn y la razón del cambio; no incluyas secretos ni cambios ajenos.
Si pedí subida, verifica el remoto y rama y realiza push sin forzar historial.
Si pedí PR, crea resumen con requisitos, pruebas reales, limitaciones y riesgos.
Crear un PR no autoriza fusionarlo. Si ya existe, actualízalo sin duplicar.
Si falla autenticación o un control, informa del motivo; no desactives protecciones.
```

## P16. Integración continua Flutter

```text
Diseña o implementa CI según {encargo} y las plataformas de esta app.
Revisa Flutter fijado por el proyecto, lockfile y herramientas del runner. Verifica
acciones/proveedores vigentes antes de seleccionarlos y usa permisos mínimos.
Propón formato sin escritura, flutter analyze y flutter test. Añade builds e
integración solo para destinos acordados y con runner/toolchain adecuados.
macOS para iOS/macOS, Windows para Windows, Linux para Linux; una prueba de widgets
en Linux no valida todos los plugins. Para integración define dispositivo y datos.
No expongas secretos a PRs no confiables ni publiques desde un workflow de tests.
Registra qué comprobaciones bloquean una entrega y cuáles son manuales. Un YAML
creado no es un workflow pasado; comprueba la ejecución del commit cuando exista.
```

## P17. Entrega y evolución

```text
Prepara {entrega} frente a los criterios de la spec. Relaciona versión de pubspec,
número de compilación, tag, artefacto y notas, sin tratarlos como lo mismo.
Enumera plataformas probadas, cambios de datos y limitaciones conocidas.
Generar artefactos no autoriza subir a tiendas, crear cuentas, aceptar términos
ni usar certificados. Comprueba destino y autorización antes de publicar.
No firmes una entrega final con credenciales inventadas o material de ejemplo.
Deja siguiente spec/cambio y pasos de recuperación proporcionados al riesgo.
```

Consulta [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) y las guías de despliegue de Flutter correspondientes al destino al aplicar el procedimiento. Las versiones de acciones y SDK se resuelven en ese momento, no se fijan para siempre en la skill.
