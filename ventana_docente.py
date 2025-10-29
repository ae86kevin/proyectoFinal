import tkinter as tk
from tkinter import messagebox
from clases import Docente
from ventanPrincipal import abrir_panel_principal

def ventana_registro_docente(master):
    win = tk.Toplevel(master)
    win.title("Registro de Docente")
    win.geometry("500x420")



    tk.Label(win, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(win)
    entry_nombre.pack(pady=5)




    tk.Label(win, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(win)
    entry_correo.pack(pady=5)



    tk.Label(win, text="Contrasena:").pack(pady=5)
    entry_pass = tk.Entry(win, show="*")
    entry_pass.pack(pady=5)

    tk.Label(win, text="Confirmar contrasena:").pack(pady=5)
    entry_pass2 = tk.Entry(win, show="*")
    entry_pass2.pack(pady=5)

    def registrar():
        nombre = entry_nombre.get().strip()
        correo = entry_correo.get().strip()
        etiqueta1 = entry_pass.get()
        etiqueta2 = entry_pass2.get()

        if not nombre or not correo or not etiqueta1 or not etiqueta2:
            messagebox.showwarning("Campos vacios", "Debe de completar los campos.")
            return
        if etiqueta1 != etiqueta2:
            messagebox.showwarning("Error", "Las contraseñas no coinciden.")
            return

        if Docente.registrar(nombre, correo, etiqueta1):
            messagebox.showinfo("Exito", "Docente registrado correctamente.")
            win.destroy()
        else:
            messagebox.showerror("Error", "El correo ya registrado.")

    tk.Button(win,text="Registrar",command=registrar, fg="white",bg="green").pack(pady=10)

def ventana_login_docente(principal):
    win = tk.Toplevel(principal)
    win.geometry("400x250")

    tk.Label(win, text="Nombre:").pack(pady=10)
    entry_nombre= tk.Entry(win)
    entry_nombre.pack(pady=5)


    tk.Label(win, text="Contraseña:").pack(pady=5)
    entry_pass = tk.Entry(win, show="*")
    entry_pass.pack(pady=5)



    def login():
        nombre = entry_nombre.get().strip()
        contrasena = entry_pass.get()
        docente = Docente.iniciar_sesion(nombre, contrasena)

        if docente:
            win.destroy()
            abrir_panel_principal(principal, docente, "Docente")
        else:
            messagebox.showerror("Error", "Nombre o contraseña incorrectos.")

    tk.Button(win, text="Iniciar Sesión", command=login, fg="white", bg="green").pack(pady=10)
