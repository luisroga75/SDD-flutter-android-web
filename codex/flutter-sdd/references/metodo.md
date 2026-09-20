# Método, entrevista y continuidad

Adaptación del itinerario de MoureDev, no un sustituto genérico ni una transcripción del vídeo. Conserva el acuerdo de producto antes del diseño y la trazabilidad después de implementar. Las extensiones multiplataforma, GitHub y auditoría se distinguen del método original.

## Criterio humano y modo de planificación

Enfoque spec-first con continuidad spec-anchored: la especificación inicia el trabajo y se mantiene coherente con código y pruebas. No se trata de spec-as-source ni de regenerar toda la app sin revisar el código. El alumno revisa documentos, diseño, código y tests; un agente no certifica por sí solo que entendió la intención.

En fases documentales recomienda el modo de planificación del agente si está disponible. No finjas activarlo ni confundas ese modo con `plan.md`: son cosas diferentes. Si el modo actual no permite escritura, presenta el borrador y pide salir de ese modo para guardar lo acordado; nunca intentes sortear su restricción. En modo normal puedes escribir documentación autorizada sin implementar la app.

AGENTS y constitución se preparan al comienzo en el orden que mejor aproveche el contexto; no hay que imponer uno. Se conservan entre funcionalidades y se modifican solo cuando cambia un acuerdo global. Revisa también plan y tareas con el alumno antes de ejecutar en el modo docente.

## Entrevista

Lee constitución, instrucciones y specs existentes. Anota hechos observados (con archivo/fuente), requisitos expresados, supuestos S-n y decisiones pendientes D-n. No deduzcas funcionalidades por el nombre del proyecto ni por una dependencia instalada.

Pregunta **una cosa por turno**, hasta seis en este ciclo de spec. Prioriza lo que cambia aceptación o alcance; evita cuestionarios de veinte apartados y preguntas ya contestadas. Si no basta, entrega el borrador con dudas y propone otro ciclo delimitado.

Orden orientativo, no formulario obligatorio:

1. Persona y problema: un ejemplo real y el resultado que necesita.
2. Primera demostración y plataformas: dónde la usará primero y qué recorrido completo necesita.
3. Datos observables: qué se conserva, comparte o recupera y qué ocurre sin conexión.
4. Interrupciones relevantes: denegación de permiso, cierre, reintento, vacío o duplicado.
5. Límite crítico del dominio: fechas, zonas horarias, concurrencia, acceso o error externo.
6. Exclusiones y aceptación: qué queda fuera y cómo sabremos que sirve.

Ejemplo: «¿La lista debe conservarse al cerrar la app? Para uso diario recomiendo que sí; para una práctica de widgets podemos limitarla a la sesión. Esto cambia lo que habrá que demostrar». No preguntes por SQLite o Riverpod durante la definición del comportamiento.

Cuando se pida “adivinar”, presenta una hipótesis, por qué encaja, una alternativa y el impacto de equivocarse. Una selección predefinida no es una respuesta. Si el usuario delega la decisión, resuélvela y documéntala como tal. No inventes umbrales, datos personales ni permisos de terceros.

## Documentos y puertas de revisión

1. Contexto y constitución: seis a ocho principios comprobables; núcleo de unas quince líneas, metadatos aparte. No heredes las restricciones de almacenamiento de la CLI Python.
2. Instrucciones: Codex usa AGENTS.md; Claude Code, CLAUDE.md. Si se solicitan ambos, un contrato común y un importador evitan duplicación.
3. Spec: qué y por qué; EARS, errores, exclusiones, finalización, dudas.
4. QA: lista ambigüedades, contradicciones, límites ausentes y conflictos con constitución. No corrijas durante una revisión de solo lectura.
5. Clarificación: resuelve con respuestas y conserva IDs; no reutilices los retirados.
6. Plan: Flutter/Dart, contratos, decisiones y alternativas descartadas, datos y pruebas por requisito.
7. Tareas: resultados pequeños, referencia RF/RNF, dependencia, comprobación y condición de fin. Objetivo pedagógico de veinte a treinta minutos; divide lo mayor sin prometer una duración exacta.
8. Implementación: solo el alcance autorizado, normalmente una tarea; test pertinente antes del código; evidencia y parada al completar ese encargo.
9. Validación: RF/RNF frente a prueba, resultado, entorno y pendiente. Cambios posteriores empiezan en la spec.

Si se descubre una diferencia entre implementación y documentación, no cambies el requisito para justificar un fallo. Decide si es bug (prueba de regresión y tarea en la spec correspondiente) o cambio de contrato acordado; sincroniza plan/tareas y conserva el historial. La carpeta completa de spec es la memoria del incremento.

Por defecto presenta constitución y spec para revisión, como en la práctica. Un encargo explícito de varias fases autoriza su avance dentro del alcance, no resuelve incógnitas materiales por silencio. Si el alumno pide “solo T2”, no comiences T3. No uses estas puertas para bloquear una explicación o una corrección mecánica ya encargada.

## Varias specs y reanudación

Una spec por resultado independiente, no una por capa técnica. Comparte principios globales. Usa `NNN-nombre` sin colisiones; referencia dependencias con `001-lista/RF-1` o `001-lista/T2`. Un cambio del mismo contrato suele pertenecer a su spec existente. `specs/plan.md` puede contener mapa, prioridades y estado, nunca planes duplicados.

Registra al cerrar: spec activa, fase, última decisión, dudas bloqueantes, tarea siguiente y verificación pendiente. Al reanudar lee también cambios Git; una casilla marcada no demuestra implementación. No reinicies la entrevista desde cero.
