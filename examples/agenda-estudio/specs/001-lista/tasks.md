# Tareas 001

## Trabajo

- [ ] T1. Preparar la app de práctica
  - RF: ninguno (infraestructura necesaria para T2 y T3)
  - Dependencias: ninguna
  - Hecho cuando: la app de confianza abre en Android y se conoce su versión Flutter.
  - Verificación: flutter doctor -v y ejecución en un destino Android disponible.
  - Evidencia: no ejecutada.

- [ ] T2. Validar títulos y añadir a la lista
  - RF: RF-1, RF-3
  - Dependencias: T1
  - Hecho cuando: títulos válidos se añaden normalizados y en orden; los vacíos no mutan la lista.
  - Verificación: pruebas unitarias de normalización, orden y no mutación, primero rojas y luego verdes.
  - Evidencia: no ejecutada.

- [ ] T3. Construir los estados de la pantalla
  - RF: RF-1, RF-2, RF-3, RF-4
  - Dependencias: T2
  - Hecho cuando: se ve el estado vacío, se pueden añadir temas y el error conserva la lista.
  - Verificación: flutter test sobre widgets de los recorridos y revisión de pantalla.
  - Evidencia: no ejecutada.

- [ ] T4. Validar sin conexión y cerrar la spec
  - RF: RNF-1
  - Dependencias: T3
  - Hecho cuando: la demo Android permite añadir y listar sin Internet y queda evidencia por requisito.
  - Verificación: recorrido manual en modo avión, más suite y análisis de la app.
  - Evidencia: no ejecutada.

## Continuación

La implementación empieza por T1 solo cuando se encargue. Ejemplo documental, sin app ni pruebas Flutter ejecutadas.
