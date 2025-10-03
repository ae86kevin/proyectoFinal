import tkinter as tk
from tkinter import messagebox

def abrir_ventana_rol(master):

    siguiente = tk.Toplevel(master)
    siguiente.title("Quin eres ?")
    siguiente.geometry("400x300")

    label = tk.Label(siguiente, text="Quien eres ?", font=("Arial", 16, "bold"))
    label.pack(pady=20)

    btn_alumno = tk.Button(siguiente, text="Alumno", width=15, height=3, command=lambda: seleccionar_rol("Alumno"))
    btn_alumno.pack(pady=10)

    btn_catedratico = tk.Button(siguiente, text="Catedrático", width=15, height=3, command=lambda: seleccionar_rol("Catedrático"))
    btn_catedratico.pack(pady=10)

def seleccionar_rol(rol):
    messagebox.showinfo("Rol seleccionado", f"Has seleccionado: {rol}")
