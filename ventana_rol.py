import tkinter as tk
from tkinter import messagebox
from sistema_academico import (
    ventana_registro_alumno,
    ventana_login_alumno,
    ventana_registro_docente,
    ventana_login_docente,
    Alumno,
    Docente,
    Curso
)





def abrir_ventana_rol(master):
    siguiente = tk.Toplevel(master)
    siguiente.title("¿Quien eres?")
    siguiente.geometry("400x300")

    label = tk.Label(siguiente, text="¿Quien eres?", font=("Arial", 16, "bold"))
    label.pack(pady=20)

    btn_alumno = tk.Button(
        siguiente, text="Alumno", width=15, height=3,
        command=lambda: mostrar_opciones(siguiente, "Alumno")
    )
    btn_alumno.pack(pady=10)



    btn_docente = tk.Button(
        siguiente, text="Docente", width=15, height=3,
        command=lambda: mostrar_opciones(siguiente, "Docente")
    )
    btn_docente.pack(pady=10)




def mostrar_opciones(ventana, rol):
    ventana.destroy()
    ventana_opciones = tk.Toplevel()
    ventana_opciones.title(f"Opciones para {rol}")
    ventana_opciones.geometry("400x400")

    label = tk.Label(
        ventana_opciones, text=f"Selecciona ",
        font=("Arial", 16, "bold")
    )
    label.pack(pady=20)

    if rol == "Alumno":
        btn_registro = tk.Button(
            ventana_opciones, text="Registrarse", width=20, height=2,
            command=ventana_registro_alumno
        )
        btn_iniciar_sesion = tk.Button(
            ventana_opciones, text="Iniciar sesión", width=20, height=2,
            command=ventana_login_alumno
        )




    else:
        btn_registro = tk.Button(
            ventana_opciones, text="Registrarse", width=20, height=2,
            command=ventana_registro_docente
        )
        btn_iniciar_sesion = tk.Button(
            ventana_opciones, text="Iniciar sesión", width=20, height=2,
            command=ventana_login_docente
        )
        btn_gestion = tk.Button(
            ventana_opciones, text="Gestionar Cursos", width=20, height=2,
            command=lambda: gestionar_cursos("Docente")
        )

    btn_registro.pack(pady=5)
    btn_iniciar_sesion.pack(pady=5)
    btn_gestion.pack(pady=5)

    btn_regresar = tk.Button(
        ventana_opciones, text="Regresar", width=20, height=2,
        command=ventana_opciones.destroy
    )
    btn_regresar.pack(pady=20)


def gestionar_cursos(rol):
    ventana_gestion = tk.Toplevel()
    ventana_gestion.title(f"Gestión de Cursos - {rol}")
    ventana_gestion.geometry("400x400")

    label = tk.Label(ventana_gestion, text=f"Gestión de Cursos ({rol})", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    tk.Label(ventana_gestion, text="Nombre del curso:").pack(pady=5)
    entry_curso = tk.Entry(ventana_gestion)
    entry_curso.pack(pady=5)

    tk.Label(ventana_gestion, text="Número de aula:").pack(pady=5)
    entry_aula = tk.Entry(ventana_gestion)
    entry_aula.pack(pady=5)

    def agregar_curso():
        nombre = entry_curso.get()
        aula = entry_aula.get()
        if not nombre or not aula:
            messagebox.showwarning("Error", "Debe llenar todos los campos.")
            return

        curso = Curso(nombre, aula)

        if rol == "Alumno":
            alumno = Alumno("Temp", "temp@correo.com")  # demo
            alumno.registrar_curso(curso)
        else:
            docente = Docente("Temp", "docente@correo.com")  # demo
            docente.registrar_curso(curso)

        messagebox.showinfo("Éxito", f"Curso '{nombre}' agregado correctamente.")

    def activar_notificaciones():
        if rol == "Alumno":
            alumno = Alumno("Temp", "temp@correo.com")
            alumno.activar_notificaciones()
        else:
            docente = Docente("Temp", "docente@correo.com")
            docente.activar_notificaciones()
        messagebox.showinfo("Notificaciones", "Notificaciones activadas.")

    def desactivar_notificaciones():
        if rol == "Alumno":
            alumno = Alumno("Temp", "temp@correo.com")
            alumno.desactivar_notificaciones()
        else:
            docente = Docente("Temp", "docente@correo.com")
            docente.desactivar_notificaciones()
        messagebox.showinfo("Notificaciones", "Notificaciones desactivadas.")

    btn_agregar = tk.Button(ventana_gestion, text="Agregar curso", command=agregar_curso)
    btn_agregar.pack(pady=10)

    btn_activar = tk.Button(ventana_gestion, text="Activar notificaciones", command=activar_notificaciones)
    btn_activar.pack(pady=10)

    btn_desactivar = tk.Button(ventana_gestion, text="Desactivar notificaciones", command=desactivar_notificaciones)
    btn_desactivar.pack(pady=10)

    btn_cerrar = tk.Button(ventana_gestion, text="Cerrar", command=ventana_gestion.destroy)
    btn_cerrar.pack(pady=20)
