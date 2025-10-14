import tkinter as tk
from ventana_alumno import ventana_registro_alumno, ventana_login_alumno
from ventana_docente import ventana_registro_docente, ventana_login_docente

def abrir_ventana_rol(master):

    siguiente = tk.Toplevel(master)
    siguiente.title("¿Quién eres?")
    siguiente.geometry("400x300")
    siguiente.configure(bg="#f4f6f7")

    tk.Label(
        siguiente,
        text="¿Quién eres?",
        font=("Arial", 18, "bold"),
        bg="#f4f6f7",
        fg="#2c3e50"
    ).pack(pady=20)

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

    tk.Button(siguiente, text="Alumno", command=lambda: mostrar_opciones(siguiente, "Alumno"), **estilo_boton).pack(pady=10)
    tk.Button(siguiente, text="Docente", command=lambda: mostrar_opciones(siguiente, "Docente"), **estilo_boton).pack(pady=10)


def mostrar_opciones(ventana, rol):

    parent = ventana.master
    ventana.destroy()

    ventana_opciones = tk.Toplevel(parent)
    ventana_opciones.title(f"Opciones para {rol}")
    ventana_opciones.geometry("450x400")
    ventana_opciones.configure(bg="#ecf0f1")

    tk.Label(
        ventana_opciones,
        text=f"Selecciona una opción ({rol})",
        font=("Arial", 16, "bold"),
        bg="#ecf0f1",
        fg="#2c3e50"
    ).pack(pady=20)

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
        tk.Button(ventana_opciones, text="Registrarse", command=lambda: ventana_registro_alumno(parent), **estilo_boton).pack(pady=10)
        tk.Button(ventana_opciones, text="Iniciar sesión", command=lambda: ventana_login_alumno(parent), **estilo_boton).pack(pady=10)
    else:
        tk.Button(ventana_opciones, text="Registrarse", command=lambda: ventana_registro_docente(parent), **estilo_boton).pack(pady=10)
        tk.Button(ventana_opciones, text="Iniciar sesión", command=lambda: ventana_login_docente(parent), **estilo_boton).pack(pady=10)

    def volver():
        ventana_opciones.destroy()
        abrir_ventana_rol(parent)

    def salir():
        parent.destroy()

    tk.Button(ventana_opciones, text="Volver", bg="#f39c12", fg="white", font=("Arial", 10, "bold"),
              command=volver, bd=0, relief="flat", cursor="hand2").place(x=20, y=340, width=100, height=35)
    tk.Button(ventana_opciones, text="Salir", bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
              command=salir, bd=0, relief="flat", cursor="hand2").place(x=330, y=340, width=100, height=35)
