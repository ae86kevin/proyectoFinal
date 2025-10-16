import tkinter as tk
from tkinter import messagebox, ttk
from clases import Alumno
from baseDatos import conectar

def abrir_panel_principal(master, usuario, rol):
    ventana = tk.Toplevel(master)
    ventana.title("Panel Principal")
    ventana.geometry("500x500")
    ventana.configure(bg="#f8f9fa")

    nombre_usuario = usuario[1] if usuario and len(usuario) > 1 else "Usuario"

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

    def crear_boton(texto, comando=None):
        boton = tk.Button(
            ventana,
            text=texto,
            font=("Arial", 11, "bold"),
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

    def agregar_cursos():
        win = tk.Toplevel(ventana)
        win.title("Agregar Curso")
        win.geometry("400x250")

        tk.Label(win, text="Nombre del curso:").pack(pady=5)
        entry_nombre = tk.Entry(win)
        entry_nombre.pack(pady=5)

        tk.Label(win, text="Aula:").pack(pady=5)
        entry_aula = tk.Entry(win)
        entry_aula.pack(pady=5)

        tk.Label(win, text="Hora de inicio:").pack(pady=5)
        entry_hora = tk.Entry(win)
        entry_hora.pack(pady=5)

        def guardar():
            nombre = entry_nombre.get().strip()
            aula = entry_aula.get().strip()
            hora = entry_hora.get().strip()

            if not nombre or not aula or not hora:
                messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
                return

            conn = conectar()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO cursos (alumno_id, nombre, aula, hora_inicio) VALUES (?, ?, ?, ?)",
                (usuario[0], nombre, aula, hora)
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Curso agregado correctamente.")
            win.destroy()

        tk.Button(win, text="Guardar curso", bg="#1abc9c", fg="white", command=guardar).pack(pady=20)

    def listar_cursos():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, aula, hora_inicio FROM cursos WHERE alumno_id=?", (usuario[0],))
        cursos = cursor.fetchall()
        conn.close()
        return cursos

    def modificar_curso():
        cursos = listar_cursos()
        if not cursos:
            messagebox.showinfo("Sin cursos", "No tienes cursos asignados.")
            return

        win = tk.Toplevel(ventana)
        win.title("Modificar curso")
        win.geometry("400x400")

        tk.Label(win, text="Selecciona un curso para modificar").pack(pady=10)
        lista = tk.Listbox(win, width=45, height=10)
        lista.pack(pady=10)

        for c in cursos:
            lista.insert(tk.END, f"{c[0]} - {c[1]} ({c[2]})")

        tk.Label(win, text="Nuevo nombre:").pack()
        entry_nombre = tk.Entry(win)
        entry_nombre.pack(pady=5)

        tk.Label(win, text="Nueva aula:").pack()
        entry_aula = tk.Entry(win)
        entry_aula.pack(pady=5)

        tk.Label(win, text="Nuevo horario:").pack()
        entry_hora = tk.Entry(win)
        entry_hora.pack(pady=5)

        def eliminar():
            seleccion = lista.curselection()
            if not seleccion:
                messagebox.showwarning("Atención", "Selecciona un curso.")
                return
            curso_id = cursos[seleccion[0]][0]
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cursos WHERE id=?", (curso_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Curso eliminado.")
            win.destroy()

        def guardar():
            seleccion = lista.curselection()
            if not seleccion:
                messagebox.showwarning("Atención", "Selecciona un curso.")
                return

            curso_id = cursos[seleccion[0]][0]
            nombre = entry_nombre.get().strip()
            aula = entry_aula.get().strip()
            hora = entry_hora.get().strip()

            if not nombre or not aula or not hora:
                messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
                return

            conn = conectar()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE cursos SET nombre=?, aula=?, hora_inicio=? WHERE id=?",
                (nombre, aula, hora, curso_id)
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Curso modificado correctamente.")
            win.destroy()

        tk.Button(win, text="Eliminar curso", bg="#e74c3c", fg="white", command=eliminar).pack(pady=5)
        tk.Button(win, text="Guardar cambios", bg="#16a085", fg="white", command=guardar).pack(pady=5)

    crear_boton("Agregar Curso", agregar_cursos).place(x=110, y=y)
    crear_boton("Modificar Curso", modificar_curso).place(x=110, y=y + espacio)

    def salir():
        master.destroy()

    def volver():
        ventana.destroy()
        messagebox.showinfo("Volver", "Volviendo al menú anterior...")

    crear_boton("Salir", salir).place(x=100, y=420)
    crear_boton("Volver", volver).place(x=260, y=420)

    ventana.resizable(False, False)
