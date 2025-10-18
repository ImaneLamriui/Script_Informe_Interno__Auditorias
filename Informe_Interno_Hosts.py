#!/usr/bin/env python3
"""
hosts_demo.py
Script simplificado para generar CSV de hosts, PDF textual y HTML interactivo.
Datos: hostname, IP, RDNS (ficticios).
"""

import csv, os, random, webbrowser
from fpdf import FPDF
from datetime import datetime


# Configuración y datos

CSV_FILE = "hosts_demo.csv"
PDF_FILE = "hosts_demo.pdf"
HTML_FILE = "hosts_demo.html"
NUM_HOSTS = 30

domains = ["demo.local", "lab.internal", "corp.example", "service.test"]
products = ["panel", "api", "db", "git", "admin", "portal"]


# Crear CSV de ejemplo

with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["hostname","ip","rdns"])
    for _ in range(NUM_HOSTS):
        sub = random.choice(products) + str(random.randint(1,99))
        domain = random.choice(domains)
        hostname = f"{sub}.{domain}"
        if random.random() < 0.55:
            ip = f"192.0.{random.randint(0,255)}.{random.randint(1,254)}"
            rdns = f"host-{random.randint(100,999)}.{domain}"
        else:
            ip = "N/A"
            rdns = "N/A"
        writer.writerow([hostname, ip, rdns])

print(f"[ok] CSV de ejemplo creado: {CSV_FILE}")


# Leer CSV

hosts = []
with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        hosts.append({
            "hostname": row["hostname"],
            "ip": row["ip"],
            "rdns": row["rdns"]
        })


# Generar PDF textual

pdf = FPDF(unit="mm", format="A4")
pdf.set_auto_page_break(True, margin=12)
pdf.add_page()
pdf.set_font("Courier", "B", 14)
pdf.cell(0, 10, "Hosts Demo Enriquecidos", ln=True, align="C")
pdf.ln(2)
pdf.set_font("Courier", "", 9)
meta = f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  |  Total hosts: {len(hosts)}"
pdf.multi_cell(0, 6, meta)
pdf.ln(4)

for h in hosts:
    line = f"Hostname: {h['hostname']}  |  IP: {h['ip']}  |  RDNS: {h['rdns']}"
    pdf.multi_cell(0, 5, line)

pdf.output(PDF_FILE)
print(f"[ok] PDF textual generado: {PDF_FILE}")

# ----------------------------
# Generar HTML y abrir en navegador
# ----------------------------
with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write("<html><body><h2>Informe Interno de Hosts – Versión Auditoría</h2><table border='1' cellpadding='4'>")
    f.write("<tr><th>Hostname</th><th>IP</th><th>RDNS</th></tr>")
    for h in hosts:
        f.write(f"<tr><td>{h['hostname']}</td><td>{h['ip']}</td><td>{h['rdns']}</td></tr>")
    f.write("</table></body></html>")

webbrowser.open(f"file://{os.path.abspath(HTML_FILE)}")
print(f"[ok] HTML generado y abierto en navegador: {HTML_FILE}")
