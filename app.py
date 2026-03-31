import tkinter as tk
from tkinter import messagebox
from datetime import date
import subprocess
import re

archivo_html = "Ivan_Fashident.html"

def actualizar():
    try:
        fab = int(entry_fab.get())
        env = int(entry_env.get())
        hoy = date.today().isoformat()

        # ===== LEER HTML =====
        with open(archivo_html, "r", encoding="utf-8") as f:
            contenido = f.read()

        # ===== REEMPLAZOS =====
        contenido = re.sub(r'(<div class="valor" id="fabricacion">)(.*?)(</div>)',
                          rf'\1{fab}\3', contenido)

        contenido = re.sub(r'(<div class="valor" id="envio">)(.*?)(</div>)',
                          rf'\1{env}\3', contenido)

        contenido = re.sub(r'(<div class="fecha" id="fecha_fab">)(.*?)(</div>)',
                          rf'\1{hoy}\3', contenido)

        contenido = re.sub(r'(<div class="fecha" id="fecha_envio">)(.*?)(</div>)',
                          rf'\1{hoy}\3', contenido)

        # ===== GUARDAR HTML =====
        with open(archivo_html, "w", encoding="utf-8") as f:
            f.write(contenido)

        # ===== GIT =====
        subprocess.run("git add .", shell=True)
        subprocess.run('git commit -m "Actualización desde app"', shell=True)
        subprocess.run("git push", shell=True)

        messagebox.showinfo("Éxito", "🚀 Página actualizada en internet")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ===== INTERFAZ =====
ventana = tk.Tk()
ventana.title("Control de Producción")
ventana.geometry("300x200")

tk.Label(ventana, text="En Fabricación").pack(pady=5)
entry_fab = tk.Entry(ventana)
entry_fab.pack()

tk.Label(ventana, text="Listas para enviar").pack(pady=5)
entry_env = tk.Entry(ventana)
entry_env.pack()

tk.Button(ventana, text="Actualizar Web", command=actualizar, bg="green", fg="white").pack(pady=20)

ventana.mainloop()