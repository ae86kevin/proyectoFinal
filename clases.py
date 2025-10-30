import sqlite3
from baseDatos import conectar

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
    def registrar(nombre, correo, contrasena):
        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO alumnos (nombre, correo, contrasena) VALUES (?, ?, ?)",
                (nombre, correo, contrasena)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()






    @staticmethod
    def iniciar_sesion(nombre, contrasena):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, contrasena FROM alumnos WHERE nombre = ?", (nombre,))
        fila = cursor.fetchone()
        conn.close()
        if not fila:
            return None
        ingreso = fila[2]
        if ingreso == contrasena:
            return (fila[0], fila[1])
        return None



class Docente(Usuario):
    @staticmethod
    def registrar(nombre, correo, contrasena):
        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO docentes (nombre, correo, contrasena) VALUES (?, ?, ?)",
                (nombre, correo, contrasena)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()






    @staticmethod
    def iniciar_sesion(nombre, contrasena):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, contrasena FROM docentes WHERE nombre = ?", (nombre,))
        fila = cursor.fetchone()
        conn.close()
        if not fila:
            return None
        ingreso2 = fila[2]
        if ingreso2 == contrasena:
            return (fila[0], fila[1])
        return None
