import platform
import socket
import os
import subprocess  # <--- NUEVO: Para ejecutar comandos del sistema
from datetime import datetime

def obtener_info_sistema():
    """Recopila información básica del SO y Hardware."""
    print("--- INICIANDO AUDITORÍA DE ACTIVOS ---")
    print(f"Fecha: {datetime.now()}")
    
    # Información del Sistema Operativo
    sistema = platform.system()
    release = platform.release()
    version = platform.version()
    
    # Información de Red
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print(f"\n[+] SISTEMA OPERATIVO:")
    print(f"    OS: {sistema}")
    print(f"    Versión: {release} - {version}")
    
    print(f"\n[+] RED:")
    print(f"    Hostname: {hostname}")
    print(f"    IP Local: {ip_address}")

def obtener_usuarios(): # <--- NUEVA FUNCIÓN
    """Obtiene la lista de usuarios del sistema."""
    print(f"\n[+] AUDITORÍA DE USUARIOS:")
    
    sistema = platform.system()
    
    try:
        if sistema == "Windows":
            # Ejecuta el comando 'net user' de Windows y captura el resultado
            # net user es el comando estándar para listar cuentas
            resultado = subprocess.run(["net", "user"], capture_output=True, text=True, shell=True)
            print(resultado.stdout)
        else:
            # Lógica simple para Linux (lee el archivo /etc/passwd)
            resultado = subprocess.run(["cut", "-d:", "-f1", "/etc/passwd"], capture_output=True, text=True)
            print("Lista de usuarios (Linux):")
            print(resultado.stdout)
            
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")

if __name__ == "__main__":
    obtener_info_sistema()
    obtener_usuarios() # <--- Llamamos a la nueva función
    