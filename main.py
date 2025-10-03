import tkinter as tk
from ventana_rol import abrir_ventana_rol
from tkinter import messagebox

def mostrar_terminos():
    messagebox.showinfo("Términos y Condiciones", "****.")

def abrir_siguiente_ventana(event=None):
    abrir_ventana_rol(root)


root = tk.Tk()
root.title("Schedelud")
root.geometry("500x400")

label_titulo = tk.Label(root, text="Schedelud", font=("Arial", 36, "bold"))
label_titulo.pack(expand=True)

btn_terminos = tk.Button(root, text="Términos y Condiciones", command=mostrar_terminos)
btn_terminos.pack(pady=20)

root.bind('<Return>', abrir_siguiente_ventana)

root.mainloop()
