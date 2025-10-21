import tkinter as tk
from tkinter import messagebox
from baseDatos import crear_tablas
from ventana_rol import abrir_ventana_rol

crear_tablas()

def mostrar_terminos():
    messagebox.showinfo(
        "Términos y condiciones",
        "Al utilizar Uscheduled, usted está aceptando los siguientes términos y condiciones...\n\n"
        "1. La aplicación puede enviarle notificaciones a su correo.\n"
        "2. Sus datos se usarán únicamente para enviar notificaciones.\n"
    )

root = tk.Tk()
root.title("Uschedelud")
root.geometry("500x400")
root.configure(bg="#e8f8f5")

tk.Label(
    root,
    text="USchedelud",
    font=("Arial", 36, "bold"),
    bg="#e8f8f5",
    fg="#2c3e50"
).pack(expand=True)

tk.Button(
    root,
    text="Términos y condiciones",
    command=mostrar_terminos,
    bg="#1abc9c",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="flat",
    cursor="hand2"
).pack(pady=20)

root.bind("<Return>", lambda event: abrir_ventana_rol(root))

root.mainloop()
