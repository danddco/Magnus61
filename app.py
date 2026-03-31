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

        # ===== REEMPLAZOS SEGUROS =====
        contenido = re.sub(r'id="fabricacion">.*?<', f'id="fabricacion">{fab}<', contenido)
        contenido = re.sub(r'id="envio">.*?<', f'id="envio">{env}<', contenido)
        contenido = re.sub(r'id="fecha_fab">.*?<', f'id="fecha_fab">{hoy}<', contenido)
        contenido = re.sub(r'id="fecha_envio">.*?<', f'id="fecha_envio">{hoy}<', contenido)

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