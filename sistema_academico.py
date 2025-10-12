import tkinter as tk
from tkinter import messagebox
import os
import sqlite3

DB_NAME ="sitema_academico.db"

def crear_tablas():
    conn = sqlite3.connect(DB_NAME)
    cursor=conn.cursor()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE TEXT NOT NULL,
    CORREO TEXT NOT NULL,
    )
''')


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS docentes
    id integer PRIMARY KEY AUTOINCREMENT,
    nombre text NOT NULL,
    correo text NOT NULL,
    ''')


    conn.commit()
    conn.close()


    crear_tablas()



class Curso:
    def iniciar(self,nombre,curso):
        self.nombre=nombre
        self.curso=curso
        self.horario =None


    def modificar_horario(self,nuevo_horario):
        self.horario = nuevo_horario


    def modificar_curso(self,nueva_aula):
        self.aula = nueva_aula


class Usuario:
    def iniciar(self,nombre="",correo=""):
        self.nombre=nombre
        self.correo=correo
        self.cursos=[]
        self.notificaciones =True

    def registrar_curso(self,curso: Curso):
        self.cursos.append(curso)

    def modificar_curso(self, i , nuevo_curso: Curso):
        if 0 <= i < len(self.cursos):
            self.cursos[i]=nuevo_curso

    def activar_notificaciones(self):
        self.notificaciones =True

    def descactivar_notificaciones(self ):
        self.notificaciones =False


class Alumno(Usuario):
        @staticmethod
        def registrar(nombre,correo):
            conn = sqlite3.connect(DB_NAME)
            cursor=conn.cursor()
            try:
                cursor.execute("INSET INTO alumnos (nombre,correo) VALUES(?,?)",(nombre,correo))
                conn.commit()
                return True
            except sqlite3.OperationalError:
                return False
            finally:
                conn.close()

        @staticmethod
        def iniciar_sesion(correo):
            conn=sqlite3.connect(DB_NAME)
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM alumnos WHERE correo=?",(correo,))
            resultado=cursor.fetchone()
            conn.close()
            return resultado is not None



class Docente(Alumno):
        @staticmethod
        def registrar(nombre,correo):
            conn = sqlite3.connect(DB_NAME)
            cursor=conn.cursor()
            try:
                cursor.execute("INSERT INTO docente (nombre, correo) VALUES(?,?)",(nombre,correo))
                conn.commit()
                return True
            except sqlite3.OperationalError:
                return False
            finally:
                conn.close()

        @staticmethod
        def iniciar_sesion(correo):
            conn = sqlite3.connect(DB_NAME)
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM docentes WHERE correo=?",(correo,))
            resultado=cursor.fetchone()
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
            messagebox.showinfo("Exito", f"Alumno {nombre} registrado correctamente.")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "El correo ya está registrado.")

    ventana = tk.Toplevel()
    ventana.title("Registro de Alumnos")
    ventana.geometry("4000x300")


    tk.Label(ventana, text="Nombre:").pack(padx=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack(padx=5)

    tk.Label(ventana,text="Correo:").pack(padx=5)
    entry_correo=tk.Entry(ventana)
    entry_correo.pack(padx=5)

    tk.Button(ventana, text="Registrar", command=guardar).pack(pady=20)



def ventana_login_alumno():
    def login():
        correo =entry_correo.get()
        if Alumno.iniciar_sesion(correo):
            messagebox.showinfo("BIENVENIDO", "ALUMNO")
            ventana.destroy()
        else:
            messagebox.showinfo("Error","correo no encontrado. Intente de nuevo")










