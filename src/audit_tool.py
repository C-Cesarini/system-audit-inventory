import platform
import socket
import os
from datetime import datetime

def obtener_info_sistema():
    """Recopila información básica del SO y Hardware."""
    print("--- INICIANDO AUDITORÍA DE ACTIVOS ---")
    print(f"Fecha: {datetime.now()}")
    
    # Información del Sistema Operativo
    sistema = platform.system()
    release = platform.release()
    version = platform.version()
    
    # Información de Red (Hostname y IP local)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print(f"\n[+] SISTEMA OPERATIVO:")
    print(f"    OS: {sistema}")
    print(f"    Versión: {release} - {version}")
    
    print(f"\n[+] RED:")
    print(f"    Hostname: {hostname}")
    print(f"    IP Local: {ip_address}")

    # Aquí agregaremos más funciones luego (usuarios, firewall, etc.)

if __name__ == "__main__":
    obtener_info_sistema()
    