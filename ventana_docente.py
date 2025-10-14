import tkinter as tk
from tkinter import messagebox
from clases import Docente
from ventanPrincipal import abrir_panel_principal

def ventana_registro_docente(master):

    win = tk.Toplevel(master)
    win.title("Registro de Docente")
    win.geometry("400x300")

    tk.Label(win, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(win)
    entry_nombre.pack(pady=5)

    tk.Label(win, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(win)
    entry_correo.pack(pady=5)

    def registrar():
        nombre = entry_nombre.get().strip()
        correo = entry_correo.get().strip()

        if not nombre or not correo:
            messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
            return

        if Docente.registrar(nombre, correo):
            messagebox.showinfo("Éxito", "Docente registrado correctamente.")
            win.destroy()
        else:
            messagebox.showerror("Error", "El correo ya está registrado.")

    tk.Button(win, text="Registrar", command=registrar, bg="#1abc9c", fg="white").pack(pady=20)


def ventana_login_docente(master):

    win = tk.Toplevel(master)
    win.title("Login de Docente")
    win.geometry("400x250")

    tk.Label(win, text="Correo:").pack(pady=10)
    entry_correo = tk.Entry(win)
    entry_correo.pack(pady=5)

    def login():
        correo = entry_correo.get().strip()
        docente = Docente.iniciar_sesion(correo)

        if docente:
            messagebox.showinfo("Bienvenido", f"Hola {docente[1]} 👋")
            win.destroy()
            abrir_panel_principal(master, docente, "Docente")
        else:
            messagebox.showerror("Error", "Correo no encontrado.")

    tk.Button(win, text="Iniciar Sesión", command=login, bg="#3498db", fg="white").pack(pady=20)
