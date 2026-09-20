# Plan 001

Contrato: [spec.md](spec.md). Diseño docente propuesto, pendiente de implementar.

Estado de lista en memoria durante el proceso y una pantalla con campo, botón y lista. Una función Dart normaliza y valida el título. El widget muestra el resultado; no se añade almacenamiento ni paquete de estado. Alternativa descartada: repositorio persistente, innecesario para esta spec de sesión.

| Requisito | Diseño | Prueba prevista |
| --- | --- | --- |
| RF-1 | Normalización y append en memoria | Unitario de espacios y widget de dos títulos en orden |
| RF-2 | Error de validación junto al campo | Widget de título de solo espacios |
| RF-3 | Validación antes de mutar lista | Unitario y widget de lista sin cambios |
| RF-4 | Estado vacío de pantalla | Widget antes del primer elemento |
| RNF-1 | Sin red ni dependencias de servicios | Demo real Android en modo avión |

Herramientas propuestas: Flutter estable acordado al preparar el entorno y flutter_test del SDK. No se registra versión inventada. Riesgo principal: confundir estado de sesión con persistencia; la siguiente spec puede ampliar ese contrato tras entrevista.
