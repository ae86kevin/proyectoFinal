import tkinter as tk
from tkinter import messagebox
from ventanPrincipal import abrir_panel_principal
from clases import Alumno


def ventana_registro_alumno(master):
    win = tk.Toplevel(master)
    win.title("Registro de Alumno")
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

        if Alumno.registrar(nombre, correo):
            messagebox.showinfo("Éxito", "Alumno registrado correctamente.")
            win.destroy()
        else:
            messagebox.showerror("Error", "El correo ya está registrado.")

    tk.Button(win, text="Registrar", command=registrar, fg="white", bg="green").pack(pady=20)


def ventana_login_alumno(master):
    win = tk.Toplevel(master)
    win.title("Login de Alumno")
    win.geometry("400x250")

    tk.Label(win, text="Correo:").pack(pady=10)
    entry_correo = tk.Entry(win)
    entry_correo.pack(pady=5)

    def login():
        correo = entry_correo.get().strip()
        alumno = Alumno.iniciar_sesion(correo)

        if alumno:
            win.destroy()
            abrir_panel_principal(master, alumno, "Alumno")
        else:
            messagebox.showerror("Error", "Correo no encontrado.")

    tk.Button(win, text="Iniciar Sesión", command=login, fg="white", bg="green").pack(pady=20)
