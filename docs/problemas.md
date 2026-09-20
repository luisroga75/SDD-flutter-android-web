# Resolver problemas sin desconfigurar el equipo

[Inicio](../README.md). Empieza por copiar el error y el comando concreto; no reinstales todo.

| Problema | Primera comprobación |
| --- | --- |
| No encuentra flutter/dart | PATH apunta al `bin` del SDK real; reabre terminal/editor; evita doble carpeta `flutter/flutter` |
| Varias versiones Flutter | Windows: `Get-Command flutter -All`; Unix: `command -v flutter`; alinea editor, terminal y versión del equipo |
| Acceso denegado en caché | SDK en carpeta escribible por el usuario; no ejecutes Flutter/VS Code con sudo como arreglo |
| Java/Gradle falla en Android | `flutter doctor -v` muestra Java efectivo; no asumas que es el de `java -version` |
| SDK o cmdline-tools ausentes | Instala con SDK Manager de Studio y confirma ruta, no solo PATH |
| Licencias Android pendientes | `flutter doctor --android-licenses`; lee y acepta las necesarias |
| sdkmanager obsoleto | Atiende la ayuda de la instalación actual/Android CLI; no reutilices flags antiguos; la guía usa Studio |
| AVD vacío | Crear uno en Device Manager; descargar emulador no crea un teléfono |
| Emulador sin aceleración | WHPX/KVM/hipervisor macOS, BIOS/UEFI y permisos; no HAXM antiguo ni chmod 777 |
| Dispositivo unauthorized | Desbloquear teléfono y aceptar la huella; revisar cable de datos/controlador |
| Doctor muestra un destino que no usaré | No es necesario preparar todos; resuelve los avisos relevantes al alcance |
| Xcode requerido en Windows/Ubuntu | Necesitas un Mac para compilar iOS localmente; no hay paquete sustituto |
| Falla plugin en web | Verifica plataformas soportadas y alternativa; no todo plugin móvil soporta navegador |
| `source ~/.bashrc` falla en Fish | No mezcles shells; usa Bash para esta guía o adapta con `set -gx` y `fish_add_path` |
| Skill no aparece | Carpeta correcta, entrada SKILL.md, nueva sesión, ausencia de duplicados y políticas del centro |
| Claude no lee AGENTS | Importa `@AGENTS.md` desde CLAUDE.md preservando contenido previo |
| GitHub dice not found | Cuenta correcta, invitación privada aceptada y `gh auth status` |
| Instalador dice que ya existe | Es una protección; revisa y respalda tu versión antes de actualizar |
| Auditor falla en app recién creada | Aún no hay documentos SDD; no significa que Flutter esté mal instalado |
| Auditor pasa pero app falla | Solo comprueba estructura documental, no ejecuta Flutter ni verifica semántica |

Las carpetas de configuración y comandos varían entre shell y sistema. No pegues una salida con tokens ni información personal en incidencias. Adjunta versiones, error depurado y destino, sin credenciales.
