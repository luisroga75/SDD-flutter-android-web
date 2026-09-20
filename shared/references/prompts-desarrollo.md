# P7–P13: diseñar, implementar y comprobar

Lee los criterios Flutter y la plantilla de la fase. No atribuyas una ejecución a un comando solo por incluirlo en el plan.

## P7. Plan técnico

```text
Lee constitución, instrucciones y {spec aprobada}. Sin implementar, redacta
plan.md: componentes Flutter/Dart, datos y ciclo de vida, navegación, estado,
contratos con servicios y comportamiento por plataforma. Relaciona cada parte
con RF/RNF y con su prueba prevista. Conserva el stack existente cuando encaje.
Justifica las decisiones significativas y una alternativa descartada. Elige
el mecanismo más simple suficiente, no añadas capas, paquetes o backend por
costumbre. Comprueba compatibilidad y soporte real de plugins por destino.
Separa modelo de dominio, DTO y persistencia solo cuando esa separación aporte.
Describe carga, vacío, error, éxito, interrupciones, offline y cancelación si
aplican. Identifica permisos y límites de fondo del sistema, migraciones y datos
sensibles. Para UI incluye adaptación, teclado/foco, semántica y textos escalados.
Define pruebas unitarias, de widgets e integración pertinentes; indica qué necesita
dispositivo, backend o macOS. Registra riesgos, dudas y una matriz RF→componente→test.
Si falta una decisión material del producto vuelve a clarificar, no la ocultes
en una librería. Presenta el plan sin modificar pubspec ni código.
```

## P8. Tareas pequeñas

```text
Transforma {spec y plan} en tasks.md con IDs T1, T2… y checkboxes.
Ordena por dependencias; busca incrementos de veinte a treinta minutos como
objetivo docente, no garantía. Divide tareas grandes por resultado comprobable.
Cada tarea: RF/RNF, dependencia, componentes, primera prueba, trabajo concreto,
Hecho cuando, Verificación con entorno y Evidencia inicialmente no ejecutada.
Una tarea técnica sin RF necesita justificación y las tareas que desbloquea.
Incluye tests antes del código cuando sea aplicable, casos de error y regresión.
No marques completado por generar una plantilla. Comprueba requisitos sin tareas,
trabajo ajeno al alcance y ciclos entre specs. Muestra qué tarea comenzar primero.
```

## P9. Auditoría previa

```text
Audita constitución, spec, plan y tareas sin editarlos. Comprueba acuerdos,
trazabilidad de todos los RF/RNF activos, tareas sin justificación, dependencias,
riesgos Flutter y aceptación por plataforma. Si existe Python, puedes ejecutar
el auditor estructural incluido contra la raíz de la app, con --ready y el agente
correcto; su éxito no sustituye la revisión semántica. Si el formato es distinto,
no lo cambies solo para satisfacer el script: revisa manualmente y declara límites.
Entrega bloqueos, advertencias y siguiente paso. No empieces código por auditar.
```

## P10. Implementación de una tarea

```text
Implementa SOLO {Tn de spec}. Lee documentos y cambios actuales; preserva trabajo
ajeno. Comprueba dependencias terminadas y el alcance real de esta tarea.
Escribe primero la prueba del comportamiento cuando corresponda, observa su
fallo pertinente y después implementa lo mínimo. No uses skips para fingir éxito.
Ejecuta formato/análisis y pruebas relevantes disponibles. Prueba un destino
real si el criterio depende de plugins, permisos o integración nativa.
No hagas upgrades globales ni añadas servicios externos sin necesidad/autorización.
Registra comandos, entorno, resultados y limitaciones. Marca la tarea solo si
cumple Hecho cuando y hay evidencia; si no, déjala pendiente con la causa.
Al terminar muestra archivos, RF cubiertos, pruebas y pendientes. Detente: no
empieces la siguiente tarea ni publiques salvo que formen parte del encargo.
```

## P11. Validación por requisito

```text
Valida {spec}: para cada RF/RNF identifica prueba/escenario, plataforma, ejecución,
resultado y evidencia. Recorre también errores, límites y criterios de finalización.
Distingue test unitario, widget e integración. Un build o captura no demuestra todo.
No declares iOS validado por probar Android, ni offline por un mock sin ese caso.
Si falta equipo, credencial o servicio, marca esa comprobación no ejecutada.
Entrega veredicto: cumplida, parcial o no verificada, con razones comprobables.
No cambies requisitos para hacer pasar la evaluación sin acordarlo.
```

## P12. Cambio spec-first

```text
Nuevo comportamiento: {cambio}. Todavía no cambies código. Localiza el contrato
afectado; decide si evoluciona la spec existente o corresponde a otro resultado.
Aclara la diferencia observable y los límites nuevos. Actualiza primero la spec,
mantén IDs estables, muestra el diff y evalúa impacto en datos, plan, tareas,
pruebas y compatibilidad por plataforma. Señala decisiones que necesitan revisión.
Después del acuerdo, propón el trabajo de migración/regresión necesario.
```

## P13. Reanudar

```text
Retoma {proyecto} desde archivos y estado Git, sin reiniciar la entrevista.
Resume spec activa, fase, última decisión, tarea pendiente y verificación real.
Contrasta tareas marcadas con evidencia y código; no las des por hechas solo por
la casilla. Identifica cambios fuera del plan y respeta trabajo ajeno.
Continúa el alcance ya autorizado. Si falta una decisión material, pregunta una
sola cosa con contexto y opciones. No crees specs o commits duplicados.
```
