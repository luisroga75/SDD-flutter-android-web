# Destinos Flutter y primera ejecución

[Inicio](../README.md). Instala antes el SDK con la guía de tu sistema. Separa **sistema de desarrollo** de **plataforma donde ejecutará la app**.

| Destino local | Windows | macOS | Ubuntu/Linux |
| --- | --- | --- | --- |
| Android | Sí, toolchain compatible | Sí, toolchain compatible | Sí, toolchain compatible |
| Web | Sí | Sí | Sí |
| iOS | No | Sí, con Xcode | No |
| macOS desktop | No | Sí, con Xcode | No |
| Windows desktop | Sí, con Visual Studio C++ | No | No |
| Linux desktop | No | No | Sí, con toolchain Linux |

La tabla describe compilaciones locales, no servicios remotos. El soporte de cada plugin y las versiones mínimas se comprueban aparte. Para clase, empieza por un destino y amplía después de validar su contrato.

## Android

Instala [Android Studio](https://developer.android.com/studio/install): instalador Windows, DMG a Aplicaciones en macOS o archivo Linux extraído en una carpeta propia (por ejemplo `~/Aplicaciones/android-studio`). En Linux arranca el lanzador `bin/studio` o `bin/studio.sh` que incluya tu descarga. Completa el asistente inicial.

En **More Actions > SDK Manager**, anota la ubicación. Instala la plataforma que necesita tu Flutter/proyecto (la guía consultada usa API 36; verifica la versión vigente) y las herramientas: Platform-Tools, Build-Tools, Command-line Tools, Emulator, CMake y NDK side by side según versiones del proyecto. [Preparación oficial Flutter Android](https://docs.flutter.dev/platform-integration/android/setup).

Flutter suele detectar Java incluido en Studio. Comprueba `flutter doctor -v`: muestra SDK y Java utilizados. No impongas JDK 17 universalmente; respeta la compatibilidad Flutter/Gradle/AGP. Si autodetección falla, revisa `flutter config --help` y configura **rutas reales**, por ejemplo `flutter config --android-sdk RUTA_REAL` o `flutter config --jdk-dir RUTA_REAL_DEL_JDK`. Estos ajustes afectan al usuario Flutter; no los cambies sin necesidad. Java de terminal y Java de Flutter pueden diferir.

Para disponer de `adb`/emulador también en terminal, configura `ANDROID_HOME` y añade carpetas sin eliminar PATH previo:

| Sistema | SDK habitual que debes verificar |
| --- | --- |
| Windows | `%LOCALAPPDATA%\Android\Sdk` |
| macOS | `$HOME/Library/Android/sdk` |
| Ubuntu | `$HOME/Android/Sdk` |

**Windows:** Variables de entorno de usuario → `ANDROID_HOME` con ruta absoluta; añade `%ANDROID_HOME%\platform-tools`, `%ANDROID_HOME%\emulator` y `%ANDROID_HOME%\cmdline-tools\latest\bin` al Path. Reabre terminal/editor.

**macOS:** añade a `~/.zprofile`, ajustando la ruta:

```zsh
export ANDROID_HOME="$HOME/Library/Android/sdk"
export PATH="$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$ANDROID_HOME/cmdline-tools/latest/bin:$PATH"
```

**Ubuntu Bash:** añade a `~/.bashrc`:

```bash
export ANDROID_HOME="$HOME/Android/Sdk"
export PATH="$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$ANDROID_HOME/cmdline-tools/latest/bin:$PATH"
```

Carga el archivo apropiado o reabre la sesión. No añadas rutas inexistentes: `cmdline-tools` se instala desde SDK Manager. Lee las licencias antes de aceptarlas:

```sh
flutter doctor --android-licenses
flutter doctor -v
```

En **Device Manager**, crea un teléfono virtual, descarga una imagen compatible con tu CPU (ARM64 en Apple Silicon, x86_64 en Intel/AMD cuando corresponda) y arráncalo. Para aceleración: WHPX en Windows, hipervisor integrado en macOS, KVM en Linux. No instales HAXM antiguo. [Aceleración oficial](https://developer.android.com/studio/run/emulator-acceleration).

Alternativa: teléfono Android con Depuración USB, cable de datos y huella RSA aceptada. Windows puede necesitar controlador del fabricante; Linux, permisos udev. Comprueba:

```sh
adb devices
flutter emulators
flutter devices
```

`device` indica un destino autorizado; `unauthorized` no. La instalación del emulador no crea automáticamente un AVD. Evita depender de nombres de plantillas Android CLI o flags de otra versión: aquí la app se crea con `flutter create`.

## Web

Instala [Chrome](https://www.google.com/chrome/) para una ruta homogénea de clase; Flutter también contempla Edge en Windows. Confirma el destino con `flutter devices`. Para una app con web habilitado, `flutter run -d chrome` abre la sesión de desarrollo. [Preparación web](https://docs.flutter.dev/platform-integration/web/setup).

Una ejecución web no prueba Android/iOS, permisos del teléfono ni plugins exclusivamente nativos. No es una solución equivalente si el requisito exige una API no disponible en navegador.

## iOS y macOS en un Mac

Instala **Xcode completo** compatible desde Apple, ábrelo y termina la instalación de componentes. Si está en Aplicaciones:

```zsh
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
sudo xcodebuild -runFirstLaunch
sudo xcodebuild -license
xcodebuild -downloadPlatform iOS
```

Lee la licencia; no la aceptes de forma automática sin revisarla. Para iOS abre el simulador desde Xcode; según versión puede llamarse Simulator o Device Hub. Para plugins que requieran CocoaPods usa la preparación de [macOS](macos.md).

Ejecuta `flutter doctor -v` y `flutter devices`. Una app para simulador no requiere configurar firma de distribución. Un dispositivo físico requiere configuración de desarrollo y firma; distribución a usuarios/tiendas tiene requisitos adicionales de Apple. No incluyas certificados en Git. [iOS](https://docs.flutter.dev/platform-integration/ios/setup) y [macOS](https://docs.flutter.dev/platform-integration/macos/setup).

## Primera app y comprobaciones

Para verificar instalación puedes usar una app de humo separada del proyecto académico. Desde tu carpeta habitual de proyectos, sin una carpeta `prueba_flutter` existente, elige **una** línea:

```sh
flutter create --platforms=android,web prueba_flutter
```

O solo web (sin SDK Android):

```sh
flutter create --platforms=web prueba_flutter
```

En Mac puedes seleccionar `ios,macos`; para escritorio utiliza `windows` o `linux` en el host adecuado. No habilites destinos que no usarás. Una app generada de prueba no define los requisitos de la app académica.

```sh
cd prueba_flutter
flutter pub get
dart format --output=none --set-exit-if-changed .
flutter analyze
flutter test
flutter devices
```

`pub get` descarga dependencias y puede cambiar archivos; úsalo solo en proyectos de confianza. Para ejecutar, sustituye `ID_REAL` por el identificador que liste Flutter:

```sh
flutter run -d ID_REAL
```

Pulsa `q` para salir. Según el destino habilitado, un build de comprobación puede ser:

```sh
flutter build apk --debug
flutter build web
```

Ejecuta solo el correspondiente a tu proyecto. Para escritorios existen `flutter build windows`, `flutter build macos` y `flutter build linux` en sus hosts. Para iOS simulador, `flutter build ios --simulator` en Mac con Xcode.

La salida satisfactoria acredita esos comandos y destino, no una spec completa. `flutter test` no ejecuta por sí solo todos los recorridos nativos. La suite `integration_test` se prepara cuando hay requisitos de integración y se ejecuta con destino concreto; no inventes una carpeta de tests que no existe.

Ahora abre la **raíz de la app** en el editor (contiene `pubspec.yaml`) y comienza la [práctica](practica-sdd.md). No abras solo `lib/`, `android/` ni la carpeta de la skill.
