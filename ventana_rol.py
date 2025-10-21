import tkinter as tk
from ventana_alumno import ventana_registro_alumno, ventana_login_alumno
from ventana_docente import ventana_registro_docente, ventana_login_docente

def abrir_ventana_rol(master):

    master.withdraw()


    siguiente = tk.Toplevel(master)
    siguiente.geometry("400x300")
    siguiente.configure(bg="#f4f6f7")

    tk.Label(
        siguiente,
        text="¿Quien eres?",
        font=("Arial", 18, "bold"),
        bg="#f4f6f7",
        fg="#2c3e50"
    ).pack(pady=20)

    estilo_boton = {
        "width": 15,
        "height": 2,
        "font": ("Arial", 12, "bold"),
        "background": "#3498db",
        "foreground": "white",
        "activebackground": "#2980b9",
        "activeforeground": "white",
        "relief": "flat",
        "cursor": "hand2"
    }

    tk.Button(siguiente, text="Alumno", command=lambda: mostrarOpciones(siguiente, "Alumno"), **estilo_boton).pack(pady=10)
    tk.Button(siguiente, text="Docente", command=lambda: mostrarOpciones(siguiente, "Docente"), **estilo_boton).pack(pady=10)


def mostrarOpciones(ventana, rol):

    principal = ventana.master
    ventana.destroy()

    ventanaOpciones = tk.Toplevel(principal)
    ventanaOpciones.geometry("450x400")
    ventanaOpciones.configure(bg="#ecf0f1")

    tk.Label(
        ventanaOpciones,
        text=f"Selecciona una opcion",
        font=("Arial", 16, "bold"),
        bg="#ecf0f1",
        fg="#2c3e50"
    ).pack(pady=20)

    estilo_boton = {
        "width": 20,
        "height": 2,
        "font": ("Arial",22 , "bold"),
        "bg": "#1abc9c",
        "fg": "white",
        "activebackground": "#16a085",
        "activeforeground": "white",
        "bd": 0,
        "relief": "flat",
        "cursor": "hand2"
    }

    if rol == "Alumno":
        tk.Button(ventanaOpciones,
                  text="Registrarse",
                  font=("Arial", 12, "bold"),
                  bg="#3498db",
                  fg="white",
                  activebackground="#16a085",
                  activeforeground="white",
                  bd=0,
                  relief="flat",
                  cursor="hand2",
                  width=20,
                  height=2,
                  command=lambda:
                  ventana_registro_alumno(principal),
                  ).pack(pady=10)


        tk.Button(ventanaOpciones,
                  text="Iniciar sesion",
                  font=("Arial", 12, "bold"),
                  bg="#3498db",
                  fg="white",
                  activebackground="#16a085",
                  activeforeground="white",
                  bd=0,
                  relief="flat",
                  cursor="hand2",
                  width=20,
                  height=2,

                  command=lambda: ventana_login_alumno(principal),).pack(pady=10)
    else:
        tk.Button(ventanaOpciones, text="Registrarse",
                  command=lambda: ventana_registro_docente(principal), ).pack(pady=10)

        tk.Button(ventanaOpciones, text="Iniciar sesión",
                  command=lambda: ventana_login_docente(principal),).pack(pady=10)




    def volver():
        ventanaOpciones.destroy()
        abrir_ventana_rol(principal)




    def salir():
        ventanaOpciones.destroy()
        principal.destroy()




    tk.Button(ventanaOpciones, text="Volver",
              bg="#f39c12",
              fg="white",
              font=("Arial", 10, "bold"),
              command=volver, bd=0, relief="flat", cursor="hand2").place(x=20, y=340, width=100, height=35)

    tk.Button(ventanaOpciones, text="Salir",
              bg="#e74c3c",
              fg="white",
              font=("Arial", 10, "bold"),
              command=salir, bd=0, relief="flat", cursor="hand2").place(x=330, y=340, width=100, height=35)
