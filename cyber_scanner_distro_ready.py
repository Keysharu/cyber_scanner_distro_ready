import os
import platform
import subprocess
import sys
from datetime import datetime

# Paleta de colores ANSI estilo Terminal Cyberpunk / Metal Gear Solid
GREEN = "\033[1;32m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
MAGENTA = "\033[1;35m"
RESET = "\033[0m"


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def ejecutar_comando_cmd(comando):
    """Ejecuta un comando del sistema de forma segura y devuelve su salida."""
    try:
        resultado = subprocess.run(
            comando, shell=True, capture_output=True, text=True, check=True
        )
        return resultado.stdout.strip()
    except Exception:
        return "No disponible"


def mostrar_banner_marca():
    """Despliega la identidad visual de El taller de la gatita tech."""
    print(f"{MAGENTA}")
    print("      /\\_/\\")
    print("     ( o.o )  <-- [ GATITA_TECH_OS v3.0_DISTRO_READY ]")
    print("      > ^ <")
    print(f"{CYAN}==================================================================")
    print(f"{YELLOW}          ⚡ EL TALLER DE LA GATITA TECH // HARDWARE AUDIT ⚡      ")
    print(f"                       [ Operadora: Keysharu ]            ")
    print(f"{CYAN}=================================================================={RESET}")
    print(f"Fecha del escaneo táctico: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(
        f"Estado del motor: {GREEN}SECURO / PROTOCOLO NATIVO SIN DEPENDENCIAS{RESET}\n"
    )


def escanear_sistema_y_cpu():
    print(f"{CYAN}[⚙️] SUBSISTEMA LOGÍSTICO Y PROCESAMIENTO{RESET}")
    print(f" ├── OS: {platform.system()} {platform.release()} (v{platform.version()})")
    print(f" ├── Arquitectura: {platform.machine()}")

    if platform.system() == "Windows":
        nombre_cpu = ejecutar_comando_cmd("wmic cpu get name /value").replace(
            "Name=", ""
        )
        nucleos = ejecutar_comando_cmd(
            "wmic cpu get numberOfCores /value"
        ).replace("NumberOfCores=", "")
        print(f" ├── Procesador: {nombre_cpu}")
        print(f" └── Núcleos Físicos: {nucleos}")
    else:
        print(f" ├── Procesador: {platform.processor()}")
        print(f" └── Núcleos: Detectados por arquitectura nativa")
    print("-" * 60)


def escanear_graficos():
    print(f"{CYAN}[🎮] SUBSISTEMA GRÁFICO (GPU & PANTALLAS){RESET}")
    if platform.system() == "Windows":
        # Interceptar el chip de vídeo para prever compatibilidad de drivers en la distro
        gpu_info = ejecutar_comando_cmd("wmic path Win32_VideoController get name /value").replace("Name=", "")
        # Limpiar saltos de línea extra para mantener el formato limpio
        gpu_limpia = " | ".join([line.strip() for line in gpu_info.split('\n') if line.strip()])
        print(f" └── Controlador Gráfico Detectado: {GREEN}{gpu_limpia}{RESET}")
    else:
        print(" └── Controlador Gráfico: Modo Live/Nativo Simplificado")
    print("-" * 60)


def escanear_memoria():
    print(f"{CYAN}[🧠] SUBSISTEMA DE MEMORIA VOLÁTIL (RAM){RESET}")
    if platform.system() == "Windows":
        mem_kb = ejecutar_comando_cmd(
            "wmic computersystem get totalphysicalmemory /value"
        ).replace("TotalPhysicalMemory=", "")
        try:
            total_gb = int(mem_kb) / (1024**3)
            print(f" └── RAM Física Total Instalada: {GREEN}{total_gb:.2f} GB{RESET}")
        except ValueError:
            print(" └── RAM Física Total: No se pudo calcular")
    else:
        print(" └── RAM Física Total: Módulo nativo restringido en esta plataforma")
    print("-" * 60)


def escanear_almacenamiento():
    print(f"{CYAN}[💾] SUBSISTEMA DE ALMACENAMIENTO (DISCOS){RESET}")
    if platform.system() == "Windows":
        salida_discos = ejecutar_comando_cmd(
            "wmic logicaldisk get caption,size,freespace"
        )
        print(f" └── Análisis de particiones activas:\n{salida_discos}")
    else:
        print(" └── Análisis de almacenamiento: Modo nativo simplificado")
    print("-" * 60)


def escanear_conectividad_y_dock():
    print(f"{CYAN}[🌐] SUBSISTEMA DE CONECTIVIDAD (RED, BLUETOOTH & BUS DOCK){RESET}")
    if platform.system() == "Windows":
        # 1. Escanear adaptadores de red físicos (Revelará el chip Ethernet del puerto RJ-45 de tu Base)
        net_adapters = ejecutar_comando_cmd('wmic path Win32_NetworkAdapter where "PhysicalAdapter=True" get Name, Manufacturer')
        lineas_net = "\n".join([f"      ├── {l.strip()}" for l in net_adapters.split('\n')[1:] if l.strip()])
        print(f" ├── Adaptadores Físicos de Red Detectados:\n{GREEN}{lineas_net}{RESET}")
        
        # 2. Escanear el controlador Bluetooth (Vital para el emparejamiento del mando de Xbox)
        bt_info = ejecutar_comando_cmd('wmic path Win32_PnPEntity where "Description like \'%bluetooth%\'" get Name')
        lineas_bt = ", ".join([l.strip() for l in bt_info.split('\n')[1:] if l.strip()])
        if lineas_bt:
            print(f" └── Hardware Bluetooth en Bus: {YELLOW}{lineas_bt}{RESET}")
        else:
            print(f" └── Hardware Bluetooth en Bus: {RED}No detectado de forma lógica o desactivado.{RESET}")
    else:
        print(" └── Red y Enlaces: Modo de compatibilidad Live")
    print("-" * 60)


def escanear_energia():
    print(f"{CYAN}[⚡] SUBSISTEMA DE ENERGÍA Y FLUJO{RESET}")
    if platform.system() == "Windows":
        comando_bat = "powershell -Command \"Get-CimInstance -ClassName Win32_Battery | Select-Object -ExpandProperty EstimatedChargeRemaining\""
        carga = ejecutar_comando_cmd(comando_bat)

        if carga == "" or "No disponible" in carga or not carga.isdigit():
            print(
                f" └── Estado: {GREEN}Modo Estación de Trabajo (PC de Sobremesa). Alimentación AC Estable.{RESET}"
            )
        else:
            print(f" ├── Dispositivo: Unidad Portátil Detectada")
            print(f" └── Capacidad de la Batería: {YELLOW}{carga}%{RESET}")
    else:
        print(f" └── Estado: Modo de compatibilidad energética por defecto")
    print("-" * 60)


def ejecutor_diagnostico():
    limpiar_pantalla()
    mostrar_banner_marca()

    escanear_sistema_y_cpu()
    escanear_graficos()      # Nueva capa de telemetría de vídeo
    escanear_memoria()
    escanear_almacenamiento()
    escanear_conectividad_y_dock() # Nueva capa de red, puertos de expansión y Bluetooth
    escanear_energia()

    print(
        f"\n{GREEN}[✓] Auditoría finalizada con éxito. Compilación lista para despliegue .EXE.{RESET}\n"
    )
    input("Presiona ENTER para cerrar el diagnóstico táctico...")


if __name__ == "__main__":
    ejecutor_diagnostico()
