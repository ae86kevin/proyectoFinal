import tkinter as tk
from ventana_rol import abrir_ventana_rol
from tkinter import messagebox


def mostrar_terminos():
    messagebox.showinfo("terminos y condiciones", "************.")


def abrir_siguiente_ventana():
    abrir_ventana_rol(root)


root = tk.Tk()
root.title("Uschedelud")
root.geometry("500x400")

label_titulo = tk.Label(root, text="USchedelud", font=("Arial", 36, "bold"))
label_titulo.pack(expand=True)

btn_terminos = tk.Button(root, text="Terminos y condiciones", command=mostrar_terminos)
btn_terminos.pack(pady=20)

root.bind("<Return>", lambda event: abrir_siguiente_ventana())

root.mainloop()
