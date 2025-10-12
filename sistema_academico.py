import tkinter as tk
from ventana_alumno import ventana_alumno
from tkinter import messagebox
import sqlite3

DB_NAME = "sistema_academico.db"

def crear_tablas():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT UNIQUE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS docentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT UNIQUE NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Crear tablas al iniciar
crear_tablas()


class Curso:
    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula
        self.horario = None

    def modificar_horario(self, nuevo_horario):
        self.horario = nuevo_horario

    def modificar_aula(self, nueva_aula):
        self.aula = nueva_aula


class Usuario:
    def __init__(self, nombre="", correo=""):
        self.nombre = nombre
        self.correo = correo
        self.cursos = []
        self.notificaciones = True

    def registrar_curso(self, curso: Curso):
        self.cursos.append(curso)

    def modificar_curso(self, i, nuevo_curso: Curso):
        if 0 <= i < len(self.cursos):
            self.cursos[i] = nuevo_curso

    def activar_notificaciones(self):
        self.notificaciones = True

    def desactivar_notificaciones(self):
        self.notificaciones = False


class Alumno(Usuario):
    @staticmethod
    def registrar(nombre, correo):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO alumnos (nombre, correo) VALUES (?, ?)", (nombre, correo))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def iniciar_sesion(correo):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alumnos WHERE correo = ?", (correo,))
        resultado = cursor.fetchone()
        conn.close()
        return resultado is not None


class Docente(Usuario):
    @staticmethod
    def registrar(nombre, correo):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO docentes (nombre, correo) VALUES (?, ?)", (nombre, correo))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def iniciar_sesion(correo):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM docentes WHERE correo = ?", (correo,))
        resultado = cursor.fetchone()
        conn.close()
        return resultado is not None


def ventana_registro_alumno():
    def guardar():
        nombre = entry_nombre.get()
        correo = entry_correo.get()
        if not nombre or not correo:
            messagebox.showwarning("Error", "Debe llenar todos los campos")
            return
        if Alumno.registrar(nombre, correo):
            messagebox.showinfo("Éxito", f"Alumno {nombre} registrado correctamente.")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "El correo ya está registrado.")

    ventana = tk.Toplevel()
    ventana.title("Registro de Alumnos")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack(pady=5)

    tk.Label(ventana, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)

    tk.Button(ventana, text="Registrar", command=guardar).pack(pady=20)


def ventana_login_alumno():
    def login():
        correo = entry_correo.get()
        if Alumno.iniciar_sesion(correo):
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre FROM alumnos WHERE correo = ?", (correo,))
            alumno = cursor.fetchone()
            conn.close()

            messagebox.showinfo("Bienvenido", f"Hola {alumno[1]}")
            ventana.destroy()
            ventana_alumno(alumno[1], alumno[0])

        else:
            messagebox.showwarning("Error", "Correo no encontrado. Intente de nuevo.")

    ventana = tk.Toplevel()
    ventana.title("Login Alumno")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)

    tk.Button(ventana, text="Iniciar sesión", command=login).pack(pady=20)


def ventana_registro_docente():
    def guardar():
        nombre = entry_nombre.get()
        correo = entry_correo.get()
        if not nombre or not correo:
            messagebox.showwarning("Error", "Debe llenar todos los campos")
            return
        if Docente.registrar(nombre, correo):
            messagebox.showinfo("Éxito", f"Docente {nombre} registrado correctamente.")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "El correo ya está registrado.")

    ventana = tk.Toplevel()
    ventana.title("Registro Docente")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack(pady=5)

    tk.Label(ventana, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)

    tk.Button(ventana, text="Registrar", command=guardar).pack(pady=20)


def ventana_login_docente():
    def login():
        correo = entry_correo.get()
        if Docente.iniciar_sesion(correo):
            messagebox.showinfo("Bienvenido", "Docente")
            ventana.destroy()
        else:
            messagebox.showwarning("Error", "Correo no encontrado. Intente de nuevo.")

    ventana = tk.Toplevel()
    ventana.title("Login Docente")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)

    tk.Button(ventana, text="Iniciar sesión", command=login).pack(pady=20)
