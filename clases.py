from baseDatos import conectar


class Curso:
    def __init__(self, nombre, aula, horario=None):
        self.nombre = nombre
        self.aula = aula
        self.horario = horario


class Usuario:
    def __init__(self, nombre="", correo=""):
        self.nombre = nombre
        self.correo = correo
        self.cursos = []
        self.notificaciones = True

    def registrar_curso(self, curso):
        self.cursos.append(curso)

    def modificar_curso(self, i, nuevo_curso):
        if 0 <= i < len(self.cursos):
            self.cursos[i] = nuevo_curso


class Alumno(Usuario):
    @staticmethod
    def registrar(nombre, correo):
        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO alumnos (nombre, correo) VALUES (?, ?)", (nombre, correo))
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()

    @staticmethod
    def iniciar_sesion(correo):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre FROM alumnos WHERE correo = ?", (correo,))
        alumno = cursor.fetchone()
        conn.close()
        return alumno


class Docente(Usuario):
    @staticmethod
    def registrar(nombre, correo):
        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO docentes (nombre, correo) VALUES (?, ?)", (nombre, correo))
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()

    @staticmethod
    def iniciar_sesion(correo):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM docentes WHERE correo = ?", (correo,))
        docente = cursor.fetchone()
        conn.close()
        return docente
