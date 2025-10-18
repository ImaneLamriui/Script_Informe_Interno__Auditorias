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



📂 Uso
1️⃣ Generar un CSV de ejemplo

```
python Informe_Interno_Hosts.py --sample hosts_demo.csv



2️⃣ Crear el PDF a partir del CSV

```
python Informe_Interno_Hosts.py --input hosts_demo.csv --output informe_hosts.pdf


El script genera un archivo PDF con la estructura:

Informe Interno de Hosts – Versión Auditoría
---------------------------------------------
Hostname: panel8.lab.internal  |  IP: 192.0.211.244  |  RDNS: host-961.lab.internal
Hostname: admin25.service.test  |  IP: 192.0.122.54  |  RDNS: host-269.service.test

### Aplicaciones Prácticas

Inventario de infraestructura en auditorías técnicas.

Generación automatizada de reportes para equipos de ciberseguridad.

Documentación de entornos internos y laboratorios de pruebas.

⚠️ Nota

Este script no realiza escaneo de red ni extracción de datos reales.
Debe usarse únicamente con información legítima o ficticia, con fines educativos y de documentación.
