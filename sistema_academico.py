import tkinter as tk
from tkinter import messagebox
import os

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

    def modificar_cursos(self, i, nuevo_curso: Curso):
        if 0 <= i < len(self.cursos):
            self.cursos[i] = nuevo_curso

    def activar_notificaciones(self):
        self.notificaciones = True

    def desactivar_notificaciones(self):
        self.notificaciones = False

    def guardar_en_archivo(self, archivo):
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(f"{self.nombre},{self.correo}\n")

    @staticmethod
    def verificar_correo(archivo, correo):
        if not os.path.exists(archivo):
            return False
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                _, correo_guardado = linea.strip().split(",")
                if correo == correo_guardado:
                    return True
        return False


class Alumno(Usuario):
    ARCHIVO = "registroalumno.txt"

    def registrar(self):
        self.guardar_en_archivo(self.ARCHIVO)

    @classmethod
    def iniciar_sesion(cls, correo):
        return cls.verificar_correo(cls.ARCHIVO, correo)


class Docente(Usuario):
    ARCHIVO = "registrodocente.txt"

    def registrar(self):
        self.guardar_en_archivo(self.ARCHIVO)

    @classmethod
    def iniciar_sesion(cls, correo):
        return cls.verificar_correo(cls.ARCHIVO, correo)


def ventana_registro_alumno():
    def guardar():
        nombre = entry_nombre.get()
        correo = entry_correo.get()
        if not nombre or not correo:
            messagebox.showwarning("Error", "Debe llenar todos los campos")
            return
        alumno = Alumno(nombre, correo)
        alumno.registrar()
        messagebox.showinfo("Éxito", f"Alumno {nombre} registrado")
        ventana.destroy()

    ventana = tk.Toplevel()
    ventana.title("Registro Alumno")
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
            messagebox.showinfo("Bienvenido", "  Alumno")
            ventana.destroy()
        else:
            messagebox.showwarning("Error", "Intente de nuevo")

    ventana = tk.Toplevel()
    ventana.title("Login Alumno")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)

    tk.Button(ventana, text="Iniciar sesion", command=login).pack(pady=20)


def ventana_registro_docente():
    def guardar():
        nombre = entry_nombre.get()
        correo = entry_correo.get()
        if not nombre or not correo:
            messagebox.showwarning("Error", "Debe llenar todos los campos")
            return
        docente = Docente(nombre, correo)
        docente.registrar()
        messagebox.showinfo("Éxito", f"Docente {nombre} registrado")
        ventana.destroy()

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
            messagebox.showinfo("Bienvenido", " Docente")
            ventana.destroy()
        else:
            messagebox.showwarning("Error", "Intente de nuevo")

    ventana = tk.Toplevel()
    ventana.title("Login Docente")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)

    tk.Button(ventana, text="Iniciar sesion", command=login).pack(pady=20)
