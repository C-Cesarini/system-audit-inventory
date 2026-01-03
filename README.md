# 🛡️ System Audit & Inventory Tool

![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

## 📋 Descripción

Esta es una herramienta de automatización desarrollada en **Python** para realizar auditorías básicas de sistemas y gestión de activos. 

El script permite a auditores y administradores de sistemas obtener rápidamente una "foto" del estado actual de un equipo, generando evidencia documental de forma automática.

### 🚀 Funcionalidades Principales

* **🕵️ Inventario de Activos:** Identificación automática del Sistema Operativo, versión y release.
* **🌐 Auditoría de Red:** Extracción de Hostname y dirección IP local.
* **👥 Gestión de Identidades:** Listado automático de usuarios del sistema (Windows/Linux) para detectar cuentas no autorizadas.
* **📄 Generación de Evidencia:** Creación automática de reportes `.txt` con fecha y hora (Timestamping) para trazabilidad.

## 🛠️ Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/C-Cesarini/system-audit-inventory.git](https://github.com/C-Cesarini/system-audit-inventory.git)
    cd system-audit-inventory
    ```

2.  **Ejecutar la herramienta:**
    ```bash
    python src/audit_tool.py
    ```

3.  **Verificar resultados:**
    El reporte se generará automáticamente en la carpeta `reports/` con el formato `reporte_auditoria_AAAAMMDD_HHMMSS.txt`.

## 🔒 Privacidad y Seguridad

Este proyecto incluye un archivo `.gitignore` configurado para **excluir** la carpeta de reportes (`reports/`) del control de versiones. Esto asegura que la información sensible recolectada durante las auditorías locales no sea expuesta en el repositorio público.

## 📝 Roadmap (Próximos pasos)

- [x] Inventario de Hardware/Software básico.
- [x] Listado de usuarios.
- [x] Exportación a .txt.
- [ ] Verificación de políticas de contraseñas.
- [ ] Chequeo de Firewall activo.

---
*Desarrollado con fines educativos y de auditoría.*
