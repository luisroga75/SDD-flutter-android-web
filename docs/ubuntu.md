# Preparar Ubuntu para Flutter SDD

[Inicio](../README.md) · Después: [plataformas](plataformas.md) y [agentes](agentes-e-instalacion.md).

Ruta para Ubuntu Desktop con soporte, x86_64, terminal Bash. ARM necesita revisar compatibilidad del destino y sus SDKs; no presupongas que el mismo paquete sirve. No uses los comandos de PowerShell ni cargues `.bashrc` desde Fish.

## 1. Herramientas básicas

```bash
sudo apt update
sudo apt install git curl ca-certificates unzip xz-utils zip libglu1-mesa python3 bubblewrap
sudo apt install gh
git --version
gh --version
python3 --version
```

Si `gh` no tiene candidato, sigue la [instalación APT de GitHub CLI](https://github.com/cli/cli/blob/trunk/docs/install_linux.md); no uses repositorios de terceros desconocidos. Python 3.9+ sirve al instalador/auditor. `bubblewrap` se incluye para el sandbox de Codex; no deshabilites protecciones del sistema para trabajar. [Sandbox de Codex](https://learn.chatgpt.com/docs/sandboxing).

Instala [VS Code para Debian/Ubuntu](https://code.visualstudio.com/docs/setup/linux) con su `.deb` oficial: ábrelo con el instalador gráfico, o desde su carpeta ejecuta `sudo apt install ./ARCHIVO_REAL.deb`, sustituyendo el nombre. Después comprueba `code --version`.

## 2. SDK Flutter

Desde la [instalación manual](https://docs.flutter.dev/install/manual), descarga el SDK stable para tu arquitectura (o la versión de la clase). Con el gestor de archivos extrae `flutter` en `~/develop`, creando la carpeta si es necesario. La ruta debe acabar en `~/develop/flutter/bin/flutter`.

Abre `code ~/.bashrc` y añade este bloque una vez:

```bash
export PATH="$HOME/develop/flutter/bin:$PATH"
```

Guarda y carga la configuración desde Bash:

```bash
source ~/.bashrc
command -v flutter
flutter --version
dart --version
flutter doctor -v
code --install-extension Dart-Code.flutter
```

No uses `sudo flutter`: las cachés del SDK deben pertenecer a tu usuario. Dart está incluido. Cierra y abre VS Code, o inícialo desde esta terminal con `code .` en la carpeta de tu app.

## 3. Herramientas del destino

Para **web** instala Chrome u otro navegador soportado por Flutter. Para **Android** sigue [plataformas](plataformas.md).

Para **Linux desktop**, instala el toolchain que recoge la [guía Flutter Linux](https://docs.flutter.dev/platform-integration/linux/setup):

```bash
sudo apt install clang cmake ninja-build pkg-config libgtk-3-dev libstdc++-12-dev
```

Si un paquete no existe para tu versión de Ubuntu, verifica el equivalente compatible y la documentación vigente; no descargues bibliotecas de una distribución obsoleta. `flutter doctor -v` debe reconocer el toolchain Linux. Esto no prepara builds Windows o iOS.

## 4. KVM si utilizarás emulador Android

Activa virtualización Intel VT-x/AMD-V en BIOS/UEFI si hace falta. Después:

```bash
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients cpu-checker
sudo usermod -aG kvm "$USER"
```

Cierra **la sesión gráfica de Ubuntu**, vuelve a entrar y comprueba:

```bash
id -nG
ls -l /dev/kvm
kvm-ok
```

No apliques permisos `777` a `/dev/kvm`. Dentro de una máquina virtual, el host debe permitir virtualización anidada; un teléfono físico puede ser alternativa. [KVM Ubuntu](https://help.ubuntu.com/community/KVM/Installation).

Para un teléfono Android USB, la [guía de dispositivos](https://developer.android.com/studio/run/device) describe reglas udev y el grupo `plugdev`; utiliza el paquete `android-sdk-platform-tools-common` de Ubuntu cuando corresponda. No ejecutes todo el editor como root para acceder al teléfono.

## 5. Comprobación

```bash
flutter doctor -v
flutter devices
```

Revisa únicamente los destinos que vayas a usar. Una falta de Xcode aquí no se resuelve instalando más paquetes Linux. Continúa con [Codex o Claude Code](agentes-e-instalacion.md).
