import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def conectar():
    return sqlite3.connect("sistema_academico.db")

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            correo TEXT UNIQUE,
            contrasena TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alumno_id INTEGER,
            nombre TEXT,
            aula TEXT,
            hora_inicio TEXT,
            FOREIGN KEY(alumno_id) REFERENCES alumnos(id)
        )
    """)

    conn.commit()
    conn.close()

def guardar_cursos(alumno_id, cursos):
    conn = conectar()
    cursor = conn.cursor()
    for curso in cursos:
        cursor.execute(
            "INSERT INTO cursos (alumno_id, nombre, aula, hora_inicio) VALUES (?, ?, ?, ?)",
            (alumno_id, curso["nombre"], curso["aula"], curso["hora"])
        )
    conn.commit()
    conn.close()

def ventana_alumno(nombre, alumno_id):
    ventana = tk.Toplevel()
    ventana.title(f"Panel del alumno - {nombre}")
    ventana.geometry("430x500")

    tk.Label(ventana, text=f"Bienvenido, {nombre}", font=("Arial", 14, "bold")).pack(pady=5)

    frame = tk.Frame(ventana)
    frame.pack(anchor="w", padx=10, pady=10)

    filaArriba = tk.Frame(frame)
    filaArriba.pack(anchor="w", pady=5)

    tk.Button(filaArriba, text="Agregar curso", width=20,
              command=lambda: crear_formulario_cursos(combo, alumno_id, ventana)).pack(side="left", padx=5)

    combo = ttk.Combobox(filaArriba, values=list(range(1, 16)), width=5, state="readonly")
    combo.pack(side="left", padx=5)
    combo.current(0)

    tk.Button(frame, text="Quitar curso", width=20).pack(anchor="w", pady=5)
    tk.Button(frame, text="Modificar curso", width=20).pack(anchor="w", pady=5)

def crear_formulario_cursos(combo, alumno_id, ventana_padre):
    cantidad = int(combo.get())

    ventana_cursos = tk.Toplevel(ventana_padre)
    ventana_cursos.title(f"Registrar {cantidad} curso(s)")
    ventana_cursos.geometry("600x400")

    tk.Label(ventana_cursos, text=f"Ingresar datos de {cantidad} curso(s)",
             font=("Arial", 12, "bold")).pack(pady=10)

    contenedor = tk.Frame(ventana_cursos)
    contenedor.pack(pady=5)

    entradas = []  # para almacenar los Entry de cada curso

    # Crear dinámicamente los campos
    for i in range(cantidad):
        fila = tk.Frame(contenedor)
        fila.pack(anchor="w", pady=5)

        tk.Label(fila, text=f"Curso {i+1}:", width=10).pack(side="left")
        nombre_entry = tk.Entry(fila, width=20)
        nombre_entry.pack(side="left", padx=5)

        tk.Label(fila, text="Aula:", width=6).pack(side="left")
        aula_entry = tk.Entry(fila, width=10)
        aula_entry.pack(side="left", padx=5)

        tk.Label(fila, text="Hora inicio:", width=10).pack(side="left")
        hora_entry = tk.Entry(fila, width=10)
        hora_entry.pack(side="left", padx=5)

        entradas.append((nombre_entry, aula_entry, hora_entry))

    def guardar_todos():
        cursos = []
        for nombre_entry, aula_entry, hora_entry in entradas:
            nombre = nombre_entry.get().strip()
            aula = aula_entry.get().strip()
            hora = hora_entry.get().strip()

            if not nombre or not aula or not hora:
                messagebox.showerror("Error", "Por favor completa todos los campos antes de guardar.")
                return

            cursos.append({"nombre": nombre, "aula": aula, "hora": hora})

        guardar_cursos(alumno_id, cursos)
        messagebox.showinfo("Éxito", f"Se guardaron {len(cursos)} curso(s) correctamente.")
        ventana_cursos.destroy()

    tk.Button(ventana_cursos, text="Guardar todos", fg="white",
              width=20, command=guardar_todos).pack(pady=15)

