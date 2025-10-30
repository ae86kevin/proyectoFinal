import tkinter as tk
from tkinter import messagebox
from clases import Alumno
from ventanPrincipal import abrir_panel_principal


def ventana_registro_alumno(principal):
    win = tk.Toplevel(principal)
    win.title("Registro de Alumno")
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
            messagebox.showwarning("Campos vacios", "Completa todos los campos.")
            return


        elif etiqueta1 != etiqueta2:
             messagebox.showwarning("Error", "Las contraseñas no coinciden.")
             return


        elif Alumno.registrar(nombre, correo, etiqueta1):
             messagebox.showinfo("Exito", "Alumno registrado correctamente.")
             win.destroy()

        else:
            messagebox.showerror("Error", "Correo ya registrado")

    tk.Button(win, text="Registrar", command=registrar, fg="white", bg="green").pack(pady=10)



def ventana_login_alumno(principal):
    win = tk.Toplevel(principal)
    win.geometry("500x420")
    win.title("Inicio de Sesión")
    win.config(bg="#f4f6f7")

    tk.Label(
        win,
        text="Inicio de sesión",
        font=("Arial", 18, "bold"),
        bg="#f4f6f7",
        fg="#2c3e50"
    ).pack(pady=10)

    tk.Label(
        win,
        text="Usuario:",
        font=("Arial", 13, "bold"),
        bg="#f4f6f7",
        fg="#2c3e50"
    ).pack(pady=10)

    entry_nombre = tk.Entry(win, font=("Arial", 14))
    entry_nombre.pack(pady=5)

    tk.Label(
        win,
        text="Contraseña:",
        font=("Arial", 13, "bold"),
        bg="#f4f6f7",
        fg="#2c3e50"
    ).pack(pady=10)

    entry_pass = tk.Entry(win, show="*", font=("Arial", 14))
    entry_pass.pack(pady=5)

    def login():
        nombre = entry_nombre.get().strip()
        contrasena = entry_pass.get()

        alumno = Alumno.iniciar_sesion(nombre, contrasena)

        if alumno:
            win.destroy()
            abrir_panel_principal(principal, alumno, "Alumno")
        else:
            messagebox.showerror("Error", "Nombre o contraseña incorrectos.")

    tk.Button(
        win,
        text="Iniciar Sesión",
        command=login,
        fg="white",
        bg="#2c3e50",
        activebackground="#34495e",
        activeforeground="white",
        font=("Arial", 13, "bold"),
        width=18,
        bd=3
    ).pack(pady=30)

    def volver():
        win.destroy()

    def salir():
        win.destroy()
        principal.destroy()


    tk.Button(
        win,
        text="Volver",
        bg="#f39c12",
        fg="white",
        font=("Arial", 10, "bold"),
        command=volver,
        bd=0,
        cursor="hand2",

    ).place(x=60,y=370,width=100,height=35)

    tk.Button(
        win,
        text="Salir",
        bg="#e74c3c",
        fg="white",
        font=("Arial", 10, "bold"),
        command=salir,
        bd=0,
        relief="flat",
        cursor="hand2"
    ).place(x=340, y=370, width=100, height=35)

