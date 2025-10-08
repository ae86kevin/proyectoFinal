import tkinter as tk
from tkinter import messagebox
from sistema_academico import (
    ventana_registro_alumno,
    ventana_login_alumno,
    ventana_registro_docente,
    ventana_login_docente,
    Alumno,
    Docente,
    Curso
)

def abrir_ventana_rol(master):
    siguiente = tk.Toplevel(master)
    siguiente.title("¿Quién eres?")
    siguiente.geometry("400x300")
    siguiente.configure(bg="#f4f6f7")

    label = tk.Label(
        siguiente,
        text="¿Quién eres?",
        font=("Arial", 18, "bold"),
        bg="#f4f6f7",
        fg="#2c3e50"
    )
    label.pack(pady=20)

    estilo_boton = {
        "width": 15,
        "height": 2,
        "font": ("Arial", 12, "bold"),
        "bg": "#3498db",
        "fg": "white",
        "activebackground": "#2980b9",
        "activeforeground": "white",
        "bd": 0,
        "relief": "flat",
        "cursor": "hand2"
    }

    btn_alumno = tk.Button(
        siguiente, text="Alumno",
        command=lambda: mostrar_opciones(siguiente, "Alumno"),
        **estilo_boton
    )
    btn_alumno.pack(pady=10)

    btn_docente = tk.Button(
        siguiente, text="Docente",
        command=lambda: mostrar_opciones(siguiente, "Docente"),
        **estilo_boton
    )
    btn_docente.pack(pady=10)


def mostrar_opciones(ventana, rol):
    parent = ventana.master
    ventana.destroy()

    ventana_opciones = tk.Toplevel(parent)
    ventana_opciones.title(f"Opciones para {rol}")
    ventana_opciones.geometry("450x400")
    ventana_opciones.configure(bg="#ecf0f1")

    label = tk.Label(
        ventana_opciones,
        text=f"Selecciona una opción ({rol})",
        font=("Arial", 16, "bold"),
        bg="#ecf0f1",
        fg="#2c3e50"
    )
    label.pack(pady=20)

    estilo_boton = {
        "width": 20,
        "height": 2,
        "font": ("Arial", 11, "bold"),
        "bg": "#1abc9c",
        "fg": "white",
        "activebackground": "#16a085",
        "activeforeground": "white",
        "bd": 0,
        "relief": "flat",
        "cursor": "hand2"
    }

    if rol == "Alumno":
        btn_registro = tk.Button(ventana_opciones, text="Registrarse", command=ventana_registro_alumno, **estilo_boton)
        btn_login = tk.Button(ventana_opciones, text="Iniciar sesión", command=ventana_login_alumno, **estilo_boton)
    else:
        btn_registro = tk.Button(ventana_opciones, text="Registrarse", command=ventana_registro_docente, **estilo_boton)
        btn_login = tk.Button(ventana_opciones, text="Iniciar sesión", command=ventana_login_docente, **estilo_boton)

    btn_registro.pack(pady=10)
    btn_login.pack(pady=10)

    def volver():
        ventana_opciones.destroy()
        abrir_ventana_rol(parent)

    def salir():
        parent.destroy()

    btn_volver = tk.Button(
        ventana_opciones, text=" Volver",
        bg="#f39c12", fg="white", font=("Arial", 10, "bold"),
        activebackground="#e67e22", activeforeground="white",
        bd=0, relief="flat", cursor="hand2",
        command=volver
    )
    btn_volver.place(x=20, y=340, width=100, height=35)

    btn_salir = tk.Button(
        ventana_opciones, text="Salir ",
        bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
        activebackground="#c0392b", activeforeground="white",
        bd=0, relief="flat", cursor="hand2",
        command=salir
    )
    btn_salir.place(x=330, y=340, width=100, height=35)
