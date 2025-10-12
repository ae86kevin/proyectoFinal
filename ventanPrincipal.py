import tkinter as tk
from tkinter import messagebox

def abrir_panel_principal(master, nombre_usuario="Usuario"):
    ventana = tk.Toplevel(master)
    ventana.title("Panel Principal")
    ventana.geometry("400x400")
    ventana.configure(bg="#f8f9fa")


    tk.Label(
        ventana,
        text=f"Bienvenido:",
        font=("Arial", 12, "bold"),
        bg="#f8f9fa",
        fg="#2c3e50"
    ).place(x=40, y=20)

    tk.Label(
        ventana,
        text=nombre_usuario,
        font=("Arial", 12),
        bg="#f8f9fa",
        fg="#16a085"
    ).place(x=140, y=20)


    def crear_boton_outline(texto, comando=None):
        boton = tk.Button(
            ventana,
            text=texto,
            font=("Arial", 11, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50",
            activebackground="#f8f9fa",
            activeforeground="#16a085",
            relief="flat",
            bd=2,
            highlightthickness=2,
            highlightbackground="#16a085",
            highlightcolor="#16a085",
            cursor="hand2",
            width=18,
            height=1,
            command=comando
        )
        return boton


    y = 80
    espacio = 60

    btn_agregar = crear_boton_outline("Agregar Cursos", lambda: messagebox.showinfo("Agregar", "Función de agregar curso"))
    btn_agregar.place(x=110, y=y)

    btn_quitar = crear_boton_outline("Quitar cursos", lambda: messagebox.showinfo("Quitar", "Función de quitar curso"))
    btn_quitar.place(x=110, y=y + espacio)

    btn_modificar = crear_boton_outline("Modificar", lambda: messagebox.showinfo("Modificar", "Función de modificar curso"))
    btn_modificar.place(x=110, y=y + espacio * 2)


    def salir():
        master.destroy()

    def volver():
        ventana.destroy()
        messagebox.showinfo("Volver", "Volviendo al menú anterior...")

    btn_salir = crear_boton_outline("Salir", salir)
    btn_salir.place(x=80, y=320)

    btn_volver = crear_boton_outline("Volver", volver)
    btn_volver.place(x=220, y=320)


    ventana.update()
    ventana.resizable(False, False)
