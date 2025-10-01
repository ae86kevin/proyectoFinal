class Alumno:
    def __init__(self, nombre, correo, cursos=None):
        self.nombre = nombre
        self.correo = correo
        self.cursos = cursos
        self.notificaciones_activas = False

    def MostrarInf(self):
        return {
            "Nombre": self.nombre,
            "Correo": self.correo,
            "Cursos": self.cursos,

        }

    def registrarCursos(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            print(f"{curso} registrado correctamente.")
        else:
            print(f"{curso} ya está registrado.")




    def modificarCursos(self, curso_antiguo, curso_nuevo):
        for i, curso in enumerate(self.cursos):
            if curso == curso_antiguo:
                self.cursos[i] = curso_nuevo
                print(f"Curso '{curso_antiguo}' modificado a '{curso_nuevo}'.")
                return
        print(f"El curso '{curso_antiguo}' no esta registrado.")





    def enviarRecordatorio(self, curso, fecha, hora):
        if curso in self.cursos:
            print(f" Recordatorio enviado a {self.correo}:")
            print(f"Curso: {curso} | Fecha: {fecha} | Hora: {hora}")
        else:
            print(f" No se puede enviar recordatorio. El curso '{curso}' no está registrado.")

    def activarNotificacion(self):
        self.notificaciones_activas = True
        print(" Notificaciones activadas.")




    def desactivarNotificacion(self):
        self.notificaciones_activas = False
        print(" Notificaciones desactivadas.")
