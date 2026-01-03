import platform
import socket
import os
import subprocess
from datetime import datetime

# Definimos dónde se guardarán los reportes
CARPETA_REPORTES = "reports"

def obtener_info_sistema():
    """Recopila información básica del SO y Hardware y la devuelve como texto."""
    reporte = ""
    reporte += "--- INICIANDO AUDITORÍA DE ACTIVOS ---\n"
    reporte += f"Fecha de ejecución: {datetime.now()}\n"
    
    # Información del Sistema Operativo
    sistema = platform.system()
    release = platform.release()
    version = platform.version()
    
    # Información de Red
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    reporte += f"\n[+] SISTEMA OPERATIVO:\n"
    reporte += f"    OS: {sistema}\n"
    reporte += f"    Versión: {release} - {version}\n"
    
    reporte += f"\n[+] RED:\n"
    reporte += f"    Hostname: {hostname}\n"
    reporte += f"    IP Local: {ip_address}\n"
    
    return reporte

def obtener_usuarios():
    """Obtiene la lista de usuarios y la devuelve como texto."""
    reporte = f"\n[+] AUDITORÍA DE USUARIOS:\n"
    
    sistema = platform.system()
    
    try:
        if sistema == "Windows":
            # Ejecuta 'net user'
            resultado = subprocess.run(["net", "user"], capture_output=True, text=True, shell=True)
            reporte += resultado.stdout
        else:
            # Linux: lee /etc/passwd
            resultado = subprocess.run(["cut", "-d:", "-f1", "/etc/passwd"], capture_output=True, text=True)
            reporte += "Lista de usuarios (Linux):\n"
            reporte += resultado.stdout
            
    except Exception as e:
        reporte += f"Error al obtener usuarios: {e}\n"
        
    return reporte

def guardar_evidencia(contenido):
    """Guarda el texto acumulado en un archivo .txt con fecha y hora."""
    
    # 1. Asegurar que la carpeta 'reports' exista. Si no, la crea.
    if not os.path.exists(CARPETA_REPORTES):
        os.makedirs(CARPETA_REPORTES)

    # 2. Crear un nombre de archivo único: reporte_20251208_193022.txt
    nombre_archivo = f"reporte_auditoria_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    ruta_completa = os.path.join(CARPETA_REPORTES, nombre_archivo)

    # 3. Escribir el contenido en el archivo
    with open(ruta_completa, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
    
    print(f"\n[v] EVIDENCIA GUARDADA EXITOSAMENTE EN: {ruta_completa}")

if __name__ == "__main__":
    # Paso 1: Recolectar toda la información en una variable
    informe_final = obtener_info_sistema()
    informe_final += obtener_usuarios()
    
    # Paso 2: Mostrar en pantalla (para feedback inmediato)
    print(informe_final)
    
    # Paso 3: Generar el archivo de evidencia
    guardar_evidencia(informe_final)
    
    