# Preparar Windows para Flutter SDD

[Inicio](../README.md) · Después: [plataformas](plataformas.md) y [agentes](agentes-e-instalacion.md).

Ruta local en Windows x64 con PowerShell. No necesitas WSL. En equipos ARM comprueba soporte vigente de Flutter, Android Studio y las herramientas de tus destinos antes de aplicar la guía. No mezcles SDK Windows con un shell de Linux.

## 1. Programas básicos

1. Instala [Git for Windows](https://git-scm.com/install/windows), permitiendo Git en PATH. Proporciona también Git Bash, útil para Claude Code.
2. Instala [VS Code](https://code.visualstudio.com/docs/setup/windows), con la opción PATH.
3. Instala [GitHub CLI](https://cli.github.com/) usando su instalador Windows.
4. Para el instalador/auditor de esta skill instala Python 3.9 o posterior desde [python.org](https://www.python.org/downloads/). Es auxiliar: tu app seguirá siendo Dart. Si instalarás la skill manualmente y no usarás auditor, Python es opcional.
5. Cierra y abre PowerShell y VS Code después de instalar.

Comprueba, una línea cada vez:

```powershell
git --version
gh --version
code --version
python --version
```

Si Python ofrece `py` en vez de `python`, usa `py --version` y el mismo comando en los pasos siguientes. Si `code` falta, abre VS Code desde Inicio y revisa PATH.

## 2. SDK de Flutter, con Dart incluido

Descarga el SDK **stable** para tu sistema desde la [instalación manual oficial](https://docs.flutter.dev/install/manual). Usa la versión acordada por el profesor si existe; no instales otra para “estar más actualizado”.

Extrae el ZIP con el Explorador en una carpeta de usuario sin espacios, por ejemplo `C:\src\flutter`, con permiso de escritura. Si no puedes escribir en `C:\src`, elige otra ruta propia sin espacios; no ejecutes Flutter permanentemente como administrador. La carpeta final debe contener `bin\flutter.bat`, no `flutter\flutter\bin` por error.

En **Editar las variables de entorno de esta cuenta > Path > Editar > Nuevo**, añade `C:\src\flutter\bin` (o tu ruta real), conservando las entradas existentes. Reabre terminal y editor. No reemplaces PATH ni uses `setx PATH` para reconstruirlo.

```powershell
Get-Command flutter
Get-Command dart
flutter --version
dart --version
flutter doctor -v
```

La primera ejecución puede descargar componentes. No instales un SDK Dart separado: utiliza el que acompaña a Flutter. [PATH oficial](https://docs.flutter.dev/install/add-to-path).

## 3. Editor

En Extensiones de VS Code instala **Flutter**, del publicador Dart Code; añade su soporte Dart. Si el editor pide localizar el SDK, selecciona la carpeta `flutter`, no `bin`.

Cuando `code` esté disponible también puedes usar:

```powershell
code --install-extension Dart-Code.flutter
```

[Flutter en VS Code](https://docs.flutter.dev/tools/vs-code). La extensión no instala por sí sola todo el SDK Android ni las herramientas de Windows desktop.

## 4. Elige destinos

- **Web:** instala un navegador compatible y sigue la sección web de [plataformas](plataformas.md).
- **Android:** instala Android Studio/SDK y un emulador o conecta un teléfono siguiendo [plataformas](plataformas.md). Para emulador habilita virtualización y Windows Hypervisor Platform; reinicia si se solicita.
- **Windows desktop:** requiere **Visual Studio**, distinto de VS Code, con la carga **Desarrollo para el escritorio con C++**. Su instalador selecciona compilador y SDK de Windows necesarios. Comprueba la sección Visual Studio de `flutter doctor -v`. [Guía oficial](https://docs.flutter.dev/platform-integration/windows/setup).
- **iOS/macOS:** no se compilan localmente aquí; necesitan un Mac.

No necesitas Android Studio si tu práctica es únicamente web, ni Visual Studio si no construyes Windows desktop. Instala solo los destinos acordados.

## 5. Salida esperada

```powershell
flutter doctor -v
flutter devices
```

Debe funcionar el toolchain del destino elegido. Una advertencia de Visual Studio no bloquea una práctica solo web/Android. Continúa con [Codex o Claude Code](agentes-e-instalacion.md) y la [primera app](plataformas.md#primera-app-y-comprobaciones).
