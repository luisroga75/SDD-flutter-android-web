# Spec 001 — Lista de estudio de sesión

Estado: ejemplo acordado ficticio, no implementado. Primer destino: Android.

## Contexto y actores

Una estudiante quiere apuntar temas a estudiar durante una sesión sin cuenta ni conexión.

## Historias

- H1: Como estudiante quiero añadir títulos para ver lo que estudiaré en esta sesión.

## Requisitos funcionales

- RF-1: CUANDO confirme un título no vacío tras quitar espacios exteriores, EL SISTEMA añadirá ese título al final de la lista.
- RF-2: SI confirma un título vacío tras quitar espacios exteriores, ENTONCES EL SISTEMA mostrará un error junto al campo.
- RF-3: SI confirma un título vacío tras quitar espacios exteriores, ENTONCES EL SISTEMA conservará la lista sin cambios.
- RF-4: MIENTRAS la lista esté vacía, EL SISTEMA mostrará una invitación a añadir el primer tema.

## Requisitos no funcionales

- RNF-1: EL SISTEMA permitirá añadir y listar temas con el dispositivo sin conexión a Internet.

## Casos límite

Los títulos repetidos están permitidos como elementos distintos. Los espacios exteriores no forman parte del título. Al terminar el proceso de la app se pierde la lista, según el alcance de sesión; navegar fuera de un campo no la borra.

## Fuera de alcance

Persistencia entre procesos, sincronización, cuenta, borrar, editar, notificaciones e iOS.

## Finalización

Pruebas de reglas y widgets cubren RF-1 a RF-4. Demo Android sin conexión verifica RNF-1 y el recorrido de añadir. Todos los resultados se registran; no hay implementación ni resultados todavía.

## Dudas

Ninguna dentro del alcance ficticio del ejemplo.
