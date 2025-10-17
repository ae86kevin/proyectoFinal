import sqlite3
from baseDatos import conectar

DB_NAME = "sistema_academico.db"


class Curso:
    def __init__(self, nombre, aula, hora_inicio):
        self.nombre = nombre
        self.aula = aula
        self.hora_inicio = hora_inicio



class Usuario:
    def __init__(self, nombre="", correo=""):
        self.nombre = nombre
        self.correo = correo


class Alumno(Usuario):
    @staticmethod
    def registrar(nombre, correo):
        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO alumnos (nombre, correo) VALUES (?, ?)", (nombre, correo)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def iniciar_sesion(correo):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, correo FROM alumnos WHERE correo = ?", (correo,))
        alumno = cursor.fetchone()
        conn.close()
        return alumno

class Docente(Usuario):
    @staticmethod
    def registrar(nombre, correo):
        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO docentes (nombre, correo) VALUES (?, ?)", (nombre, correo)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def iniciar_sesion(correo):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, correo FROM docentes WHERE correo = ?", (correo,))
        docente = cursor.fetchone()
        conn.close()
        return docente
