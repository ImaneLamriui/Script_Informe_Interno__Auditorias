# Script_Informe_Interno_Hosts_Auditor
# 🧾 Informe Interno de Hosts – Versión Auditoría

Este proyecto demuestra cómo generar un **informe técnico en PDF** a partir de un archivo CSV con datos de hosts (nombre, IP, RDNS).  
Está diseñado para **auditorías, inventarios de red y procesos de documentación técnica**.

## 🚀 Características

- Lee archivos CSV con las columnas: `hostname`, `ip`, `rdns`.
- Genera un **PDF textual profesional**, con formato tipo log técnico.
- Incluye control de errores y mensajes claros.
- No requiere dependencias complejas (solo `fpdf`).
- Compatible con Python 3.x y Windows/Linux.
## ⚙️ Instalación

```
pip install fpdf==1.7.2
