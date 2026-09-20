# Preparar macOS para Flutter SDD

[Inicio](../README.md) · Después: [plataformas](plataformas.md) y [agentes](agentes-e-instalacion.md).

Usa Terminal con zsh. Identifica Apple Silicon o Intel en **Acerca de este Mac** y descarga SDKs compatibles. Sigue requisitos vigentes de macOS/Xcode/Flutter; una versión antigua de macOS puede no admitir las herramientas actuales.

## 1. Programas básicos

Instala herramientas de línea de comandos Apple si no existen:

```zsh
xcode-select --install
```

Acepta el diálogo y espera. Esto proporciona Git, pero **no sustituye Xcode completo** para iOS/macOS.

Instala Homebrew desde [brew.sh](https://brew.sh/), con su instalador oficial o `.pkg` enlazado. Sigue las instrucciones finales de PATH para tu equipo (Apple Silicon e Intel usan ubicaciones diferentes). Luego:

```zsh
brew --version
brew install gh
brew install python
git --version
gh --version
python3 --version
```

Python 3.9+ solo se necesita para el instalador y auditor de esta skill, no para Flutter.

Instala [VS Code](https://code.visualstudio.com/docs/setup/mac) en Aplicaciones. En su paleta `Cmd+Shift+P`, ejecuta **Shell Command: Install 'code' command in PATH**. Reabre la terminal.

## 2. Flutter y Dart

Descarga el SDK Flutter **stable** (o la versión acordada por el profesor) para tu procesador desde la [guía manual](https://docs.flutter.dev/install/manual). Extrae la carpeta `flutter` en `~/develop`; crea `develop` si no existe. No sobrescribas otro SDK ni lo coloques dentro del proyecto.

En VS Code abre `~/.zprofile` (puedes ejecutar `code ~/.zprofile`) y añade, sin borrar lo existente:

```zsh
export PATH="$HOME/develop/flutter/bin:$PATH"
```

Guarda y abre una nueva ventana de Terminal. Para una terminal integrada zsh que no sea de login, carga ese bloque también en su sesión o configura tu entorno de shell de forma coherente. Evita añadirlo repetidamente.

```zsh
command -v flutter
flutter --version
dart --version
flutter doctor -v
```

Dart viene con Flutter; no instales otro SDK Dart. [Configuración de PATH](https://docs.flutter.dev/install/add-to-path).

## 3. Editor y destinos

Instala la extensión **Flutter** del publicador Dart Code, que aporta soporte Dart, o ejecuta:

```zsh
code --install-extension Dart-Code.flutter
```

Para web configura navegador; para Android, Studio/SDK; para iOS y macOS, Xcode completo. Todos los pasos están en [plataformas](plataformas.md). Xcode no es obligatorio para una práctica únicamente web o Android.

Si usarás plugins nativos que requieren CocoaPods, tras tener Homebrew:

```zsh
brew install cocoapods
pod --version
```

No cambies a otra solución de dependencias Apple ni modifiques el proyecto solo para silenciar una alerta; respeta el mecanismo utilizado por sus plugins. La [guía Flutter iOS](https://docs.flutter.dev/platform-integration/ios/setup) identifica las herramientas requeridas.

## 4. Comprobación

```zsh
flutter doctor -v
flutter devices
```

Resuelve los avisos de los destinos elegidos. Para el emulador Android elige imágenes compatibles con tu CPU; macOS utiliza su hipervisor integrado. Continúa con [el agente y la skill](agentes-e-instalacion.md).
