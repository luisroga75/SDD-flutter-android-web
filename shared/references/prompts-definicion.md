# P0–P6: definir, especificar y clarificar

Los bloques son prompts completos reutilizables. Sustituye `{campos}` con contexto real; si falta una decisión relevante, pregunta. `INSTRUCCIONES` significa AGENTS.md en Codex o CLAUDE.md en Claude Code. No ejecutes un prompt si solo te piden mostrarlo.

## P0. Descubrimiento

```text
Usa la skill flutter-sdd para definir {idea} en {raíz de la app}.
Mi alcance ahora es {documentación / fases concretas / también código}.
Lee las instrucciones, archivos de producto y specs existentes. Distingue
plantilla, código real y decisiones confirmadas. No instales ni actualices nada
solo para entrevistarme. Identifica plataformas objetivo y entorno disponible.
Pregunta de una en una; empieza por el dato ausente de mayor impacto. Ofrece
opciones comprensibles y una recomendación con motivo, sin resolver el diseño
técnico antes del comportamiento. Propón un MVP demostrable y exclusiones.
Anota supuestos, dudas y decisiones delegadas. No inventes login, nube o pagos.
Si ya tienes información suficiente, redacta el borrador documental autorizado.
```

## P1. Constitución

```text
Prepara docs/constitution.md para {app Flutter} con la plantilla incluida.
Lee el repositorio y acuerdos previos. Propón seis a ocho principios verificables
sobre spec/código, simplicidad, separación de lógica y widgets, calidad, datos,
accesibilidad e idiomas cuando apliquen. Mantén el núcleo en unas quince líneas.
Flutter/Dart es el marco de este encargo, no una autorización para imponer
paquetes. Conserva decisiones existentes compatibles y plataformas elegidas.
No conviertas una función del MVP en principio universal. No fijes versiones
sin evidencia. Separa estado, revisión, dudas y mecanismo de cambio del núcleo.
Muestra la propuesta y solicita revisión en el modo docente; no pases a código.
Si ya autoricé otras fases, avanza solo las partes sin decisiones bloqueantes.
```

## P2. Instrucciones del agente

```text
Crea o mejora el archivo INSTRUCCIONES de {app}, preservando lo que ya existe.
Incluye contexto fiel, mapa de carpetas, constitución y cómo encontrar la spec
activa. Lista comandos Flutter que correspondan al proyecto y distingue los
verificados de los propuestos. No inventes una ejecución de flutter doctor.
Incluye reglas spec-first, Dart, tests y revisión, datos sensibles y Git según
los acuerdos. No dupliques toda la constitución ni fijes la primera spec como
única funcionalidad para siempre. No edites configuración global del agente.
Para la variante Claude nueva de esta práctica o para ambos agentes, propone
AGENTS.md común y CLAUDE.md con @AGENTS.md; conserva una estructura existente
solo CLAUDE si corresponde. Para Codex solo, AGENTS.md basta. Las instrucciones
no anulan permisos del entorno.
```

## P3. Mapa de funcionalidades

```text
Divide {alcance} en incrementos observables con aceptación independiente.
Reutiliza contratos existentes cuando sea un cambio del mismo comportamiento.
Asigna el siguiente número libre a cada spec nueva sin renumerar las anteriores.
Cada carpeta contendrá spec.md, plan.md y tasks.md cuando llegue a su fase.
Relaciona dependencias, límites y responsables del comportamiento para evitar
RF duplicados. Si solicité specs/plan.md, úsalo como mapa de orden y estado.
Recomienda la siguiente spec por valor y dependencia, no por comodidad técnica.
No diseñes en detalle funcionalidades futuras que aún no hemos definido.
```

## P4. Entrevista y contrato EARS

```text
Especifica {funcionalidad}. Lee constitución, INSTRUCCIONES y specs relacionadas.
No escribas código ni arquitectura. Entrevístame con preguntas de una en una,
hasta seis en este ciclo, concentradas en errores, límites y exclusiones.
Reutiliza respuestas previas. Recomienda comportamientos, no librerías.
Aclara usuario, disparador, entrada, resultado, estados y alcance por plataforma.
Incluye solo los casos de conectividad, permisos, concurrencia o accesibilidad
que condicionen esta función. No prometas igualdad de capacidades entre sistemas.
Redacta con la plantilla spec.md: contexto, actores, historias, RF en EARS,
RNF medibles, límites, fuera de alcance, finalización y dudas. Una obligación
comprobable por RF. No inventes umbrales ni requisitos de negocio para completar
secciones. Expresa ausencias con [NECESITA ACLARACIÓN: pregunta concreta].
Presenta el contrato para revisión; no saltes al plan sin el acuerdo correspondiente.
```

EARS separa condición de respuesta: obligación permanente; reacción a evento; conducta durante un estado; variante opcional; respuesta ante un fallo. Redacta una frase por obligación. Ejemplo propio, solo si se acuerda ese alcance:

- RF-1: CUANDO se confirme un título válido, EL SISTEMA mostrará el elemento en la lista.
- RF-2: SI el título solo contiene espacios, ENTONCES EL SISTEMA mostrará un error junto al campo.
- RF-3: SI el título solo contiene espacios, ENTONCES EL SISTEMA mantendrá la lista sin añadir elementos.

“Rápido” no es medible. Un RNF de rendimiento necesita operación, entorno, volumen y umbral acordados. No pongas Riverpod, tablas SQL o nombres de clases en la spec. Escenarios Dado/Cuando/Entonces pueden ilustrarla, no reemplazan RF.

## P5. Revisión QA sin cambios

```text
Revisa {spec} como QA, frente a constitución y contratos relacionados.
No edites archivos ni propongas soluciones todavía. Lista hallazgos en cuatro
bloques: ambigüedades, contradicciones, límites ausentes y conflictos con los
principios. Para cada hallazgo indica ubicación/RF, contraejemplo, impacto y
pregunta que permitiría resolverlo. Detecta supuestos disfrazados de acuerdos.
No exijas funcionalidades declaradas fuera de alcance. Si no hay defectos
relevantes, dilo sin inventarlos. Distingue dudas de producto de viabilidad técnica.
```

## P6. Clarificación

```text
Resuelve conmigo los hallazgos de {spec}, una pregunta significativa cada vez.
Da opciones, recomendación y consecuencias; cita respuestas previas si bastan.
Incorpora los acuerdos en la spec conservando IDs y exclusiones. Retira requisitos
explícitamente sin reutilizar sus IDs. Muestra el cambio de comportamiento.
Comprueba coherencia de historias, errores y finalización. Mantén visibles las
dudas que no podamos resolver. Declara lista para el plan solo la parte cuyo
comportamiento y aceptación sean verificables; todavía no implementes.
```
