import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("500x600")

label_bienvenida = tk.Label(
    ventana,
    text="Uscheduled",
    font=("Arial", 20)
)
label_bienvenida.place(relx=0.5, rely=0.5, anchor="center")





boton_terminos = tk.Button(
    ventana,
    text="Terminos y Condiciones",
    font=("Arial", 5)
)
boton_terminos.pack(side="bottom", pady=20)

ventana.mainloop()
