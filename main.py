import tkinter as tk
from ventana_rol import abrir_ventana_rol
from tkinter import messagebox

def mostrar_terminos():
    messagebox.showinfo("Términos y condiciones", "************.")

root = tk.Tk()
root.title("Uschedelud")
root.geometry("500x400")

tk.Label(root, text="USchedelud", font=("Arial", 36, "bold")).pack(expand=True)
tk.Button(root, text="Términos y condiciones", command=mostrar_terminos).pack(pady=20)





root.bind("<Return>", lambda event: abrir_ventana_rol(root))
root.mainloop()


