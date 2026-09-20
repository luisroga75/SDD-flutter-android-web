# Decisiones propias de Flutter y Dart

## Antes del diseño

Inspecciona `pubspec.yaml`, lockfile, restricciones Dart, versión Flutter usada por el equipo, carpetas habilitadas, `analysis_options.yaml`, CI y tests. Un directorio `ios/` generado no demuestra soporte validado. No añadas todos los destinos ni ejecutes `flutter create .` sobre un proyecto existente como solución automática.

En un proyecto nuevo acuerda destino inicial. Flutter incluye Dart; no presupongas instalar Kotlin, Gradle o Dart globalmente. Si el equipo fija Flutter con una herramienta de versiones, respétala. No hagas `flutter upgrade` para resolver cualquier fallo.

## Diseño proporcionado

- Mantén widgets centrados en presentación e interacción; extrae reglas probables de prueba fuera de ellos. Un prototipo puede usar estado local; un flujo compartido puede justificar una solución más amplia.
- Conserva el gestor de estado existente. Evalúa ciclo de vida, dependencia, capacidad de pruebas y complejidad del equipo antes de proponer un paquete.
- Define carga, vacío, error y éxito; evita efectos disparados repetidamente desde `build`. Gestiona suscripciones, controladores, Futures y resultados que lleguen tras abandonar una pantalla.
- Repositorios/adaptadores son útiles cuando separan una fuente real o un sustituto de pruebas; no impongas capas vacías. UI no equivale a modelo de dominio.
- Revisa null safety, errores asíncronos, parseo, fechas y zona horaria. No confundas hora local con instante UTC.
- Navegación declarativa, deep links, sesión y rutas web solo si lo requiere el producto. Datos en URL y almacenamiento de navegador tienen riesgos propios.

Consulta la [guía arquitectónica oficial](https://docs.flutter.dev/app-architecture/guide) como referencia, no como obligación de adoptar una arquitectura completa.

## Plataformas y datos

Para cada plugin anota plataformas y versiones soportadas, permisos, implementación web/desktop, mantenimiento y alternativas. No asumas que `dart:io` funciona en web. Los temporizadores Dart no garantizan tareas periódicas con la app cerrada; investiga mecanismos y restricciones nativas antes de prometer automatización. Declara diferencias aceptables por plataforma en la spec.

Persistencia depende del contrato: sesión, preferencias, datos estructurados, ficheros o sincronización. No metas secretos de backend en assets ni en `--dart-define`: una aplicación cliente no es un almacén secreto. Elige autenticación y backend solo si se necesitan; reglas de servidor no se sustituyen con checks de UI. No incluyas datos reales de alumnos en ejemplos.

## UI y calidad

Diseña para espacio disponible, no para un único modelo de teléfono. Verifica texto escalado, foco/teclado, semántica, contraste y estados accesibles según el alcance. Idiomas, localización, formatos regionales y RTL se incorporan por requisitos, no por una lista automática.

Los tests unitarios cubren lógica; los de widgets, interacción/renderizado controlado; los de integración, recorridos sobre destinos reales. Los golden tests son opcionales y sensibles al entorno. Mocks no prueban integración nativa. [Tipos de prueba Flutter](https://docs.flutter.dev/testing/overview).

Comandos candidatos a verificar en la app:

```sh
flutter --version
flutter doctor -v
flutter pub get
dart format --output=none --set-exit-if-changed .
flutter analyze
flutter test
flutter devices
```

`pub get` usa red y puede actualizar archivos; no se ejecuta en una inspección estrictamente de solo lectura. Ajusta el formato a rutas pertinentes si hay código generado. Para integración prepara `integration_test` y un destino disponible; no inventes una suite inexistente.

Builds y publicación se separan: `flutter build apk --debug` comprueba Android debug; una versión firmada, una release GitHub y una subida a una tienda son actos distintos. iOS/macOS requieren host Mac; Windows desktop requiere Windows; Linux desktop, Linux. Un checkout común no elimina estas restricciones.
