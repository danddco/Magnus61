import sqlite3
from cdMx_sql import cr_sql
from datetime import date
from cdMx_web_Arriba import webarriba
from cdMx_web_Abajo import webabajo

def WebComFta():
    # Consulta SQL
    sel_cr_1 = " "
    sel_cr_2 = " ORDER by cr_fecha DESC LIMIT 80"
    rows = cr_sql(sel_cr_1, sel_cr_2)

    # Fecha actual
    fecha_actual = date.today().strftime("%Y-%m-%d")

    # Encabezado HTML
    html = webarriba()
    html += """
    <style>
        table {
            border-collapse: collapse;
            width: 90%;
            margin: auto;
            font-size: 14px;
            font-weight: bold;
            text-align: left;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
            text-align: center;
        }
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        .alerta {
            background-color: #f8d7da;
            color: #721c24;
        }
        .bajo {
            background-color: #fff3cd;
        }
        /* Filas alternas más contrastadas */
        tbody tr:nth-child(odd) {
            background-color: #ffffff;
        }
        tbody tr:nth-child(even) {
            background-color: #d9d9d9; /* gris más fuerte */
        }
        /* Efecto hover */
        tbody tr:hover {
            background-color: #bfbfbf;
            cursor: pointer;
        }
    </style>

    <h2 style="text-align:center;">Componentes Facturados</h2>
    <table>
        <thead>
            <tr>
                <th>Fecha</th>
                <th>idE</th>
                <th>Descripción</th>
                <th>LCSC</th>
                <th>Ctdad</th>
                <th>Observaciones</th>
            </tr>
        </thead>
        <tbody>
    """

    # Filas dinámicas
    for row in rows:
        clase = "bajo"  # Ajusta la lógica según tus reglas
        html += f"""
        <tr class="{clase}">
            <td style="text-align:right;">{row[2]}</td>
            <td style="text-align:left;font-size:18px;">{row[3]}</td>
            <td style="text-align:left;font-size:28px;font-weight:bold;">{row[4]}</td>
            <td style="text-align:left;">{row[5]}</td>
            <td style="text-align:right;font-size:28px;font-weight:bold;">{row[6]}</td>
            <td style="text-align:left;">{row[9]}</td>
        </tr>
        """

    # Cierre HTML
    html += """
        </tbody>
    </table>
    """
    html += webabajo()

    # Guardar archivo en la carpeta indicada
    nombre_archivo = r"comp_facturados.html"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Página web generada como {nombre_archivo}")
WebComFta()
