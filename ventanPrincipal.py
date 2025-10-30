import tkinter as tk
from tkinter import messagebox, ttk
from baseDatos import conectar
from notificador import enviar_correo
import schedule
import threading
import time
import re

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(60)

threading.Thread(target=run_schedule, daemon=True).start()

def abrir_panel_principal(master, usuario, rol):
    ventana = tk.Toplevel(master)
    ventana.title("UOscheduled")
    ventana.geometry("500x400")
    ventana.configure(bg="#f8f9fa")

    if isinstance(usuario, dict):
        nombre_usuario = usuario.get("nombre", "Usuario")
        usuario_id = usuario.get("id")
    else:
        nombre_usuario = usuario[1] if usuario and len(usuario) > 1 else "Usuario"
        usuario_id = usuario[0] if usuario else None

    tk.Label(ventana,
             text=f"Bienvenido:",
             font=("Arial", 12, "bold"),
             bg="#f8f9fa",
             fg="#2c3e50").place(x=40, y=20)
    tk.Label(ventana,
             text=nombre_usuario,
             font=("Arial", 12),
             bg="#f8f9fa",
             fg="#16a085").place(x=140, y=20)

    def crear_boton(texto, comando=None):
        return tk.Button(
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

    y = 80
    espacio = 60

    tk.Label(ventana, text="Cantidad:").place(x=320, y=y + 5)
    combo_cantidad = ttk.Combobox(ventana, values=[str(i) for i in range(0, 16)], width=3)
    combo_cantidad.place(x=400, y=y + 5)
    combo_cantidad.set("0")

    def agregar_cursos():
        try:
            cantidad = int(combo_cantidad.get())
        except ValueError:
            messagebox.showerror("Error", "Selecciona una cantidad válida.")
            return
        if cantidad <= 0:
            messagebox.showwarning("Atención", "Selecciona al menos 1 curso.")
            return
        abrir_formulario_cursos(usuario_id, cantidad, rol)

    def listar_cursos():
        conn = conectar()
        cursor = conn.cursor()
        if rol.lower() == "alumno":
            cursor.execute("SELECT id, nombre, aula, hora_inicio, dias_semana FROM cursos WHERE alumno_id=?", (usuario_id,))
        else:
            cursor.execute("SELECT id, nombre, aula, hora_inicio, dias_semana FROM cursos WHERE docente_id=?", (usuario_id,))
        cursos = cursor.fetchall()
        conn.close()
        return cursos

    def modificar_curso():
        cursos = listar_cursos()
        if not cursos:
            messagebox.showinfo("Sin cursos", "No tienes cursos asignados.")
            return

        win = tk.Toplevel(ventana)
        win.title("Modificar / Eliminar curso")
        win.geometry("400x400")

        tk.Label(win, text="Selecciona un curso").pack(pady=10)
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
        tk.Label(win, text="Nuevo horario (HH:MM):").pack()
        entry_hora = tk.Entry(win)
        entry_hora.pack(pady=5)

        def validar_hora(hora):
            return bool(re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", hora))

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
            if not validar_hora(hora):
                messagebox.showerror("Error", "Ingrese la hora en formato 24h (HH:MM)")
                return

            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("UPDATE cursos SET nombre=?, aula=?, hora_inicio=? WHERE id=?",
                           (nombre, aula, hora, curso_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Curso modificado correctamente.")
            win.destroy()

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
            messagebox.showinfo("Éxito", "Curso eliminado correctamente.")
            win.destroy()

        tk.Button(win, text="Guardar cambios", bg="#16a085", fg="white", command=guardar).pack(pady=10)
        tk.Button(win, text="Eliminar curso", bg="#e74c3c", fg="white", command=eliminar).pack(pady=10)

    crear_boton("Agregar Cursos", agregar_cursos).place(x=110, y=y)
    crear_boton("Modificar / Eliminar", modificar_curso).place(x=110, y=y + espacio)
    crear_boton("Mostrar cursos", lambda: mostrar_cursos_popup()).place(x=110, y=y + espacio * 2)

    def mostrar_cursos_popup():
        cursos = listar_cursos()
        if not cursos:
            messagebox.showinfo("Cursos", "No hay cursos registrados.")
            return
        win = tk.Toplevel(ventana)
        win.title("Cursos Registrados")
        win.geometry("400x300")
        tk.Label(win, text="Cursos registrados:").pack(pady=10)
        lista = tk.Listbox(win, width=50, height=12)
        lista.pack(pady=10)
        for c in cursos:
            lista.insert(tk.END, f"{c[1]} - Aula: {c[2]} - Días: {c[4]}")

    def salir():
        master.destroy()

    def volver():
        ventana.destroy()
        messagebox.showinfo("Volver", "Regresando al menú...")

    crear_boton("Salir", salir).place(x=100, y=340)
    crear_boton("Volver", volver).place(x=260, y=340)
    ventana.resizable(False, False)

def abrir_formulario_cursos(usuario_id, cantidad, rol):
    win = tk.Toplevel()
    win.title(f"Agregar {cantidad} curso(s)")
    win.geometry("780x600")

    tk.Label(win, text=f"Agregar {cantidad} curso(s)", font=("Arial", 12, "bold")).pack(pady=10)

    contenedor_canvas = tk.Frame(win)
    contenedor_canvas.pack(fill="both", expand=True)

    canvas = tk.Canvas(contenedor_canvas)
    scrollbar = tk.Scrollbar(contenedor_canvas, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    entradas = []

    for i in range(cantidad):
        frame = tk.LabelFrame(scrollable_frame, text=f"Curso {i + 1}", padx=10, pady=10)
        frame.pack(fill="x", pady=8, padx=10)

        tk.Label(frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=3)
        nombre = tk.Entry(frame, width=20)
        nombre.grid(row=0, column=1, padx=5, pady=3)

        tk.Label(frame, text="Aula:").grid(row=1, column=0, padx=5, pady=3)
        aula = tk.Entry(frame, width=10)
        aula.grid(row=1, column=1, padx=5, pady=3)

        frame_dias = tk.Frame(frame)
        frame_dias.grid(row=2, column=0, columnspan=3, pady=8)

        dias_horas = []
        for dia in dias_semana:
            sub = tk.Frame(frame_dias)
            sub.pack(anchor="w", pady=2)
            var_dia = tk.BooleanVar()
            chk = tk.Checkbutton(sub, text=dia, variable=var_dia)
            chk.pack(side="left")
            tk.Label(sub, text="Hora (HH:MM):").pack(side="left", padx=3)
            entry_hora = tk.Entry(sub, width=8)
            entry_hora.pack(side="left", padx=3)
            dias_horas.append((dia, var_dia, entry_hora))

        entradas.append((nombre, aula, dias_horas))

    def validar_hora(hora):
        return bool(re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", hora))

    def guardar_todos():
        conn = conectar()
        cursor = conn.cursor()
        cursos_guardados = []

        for nombre, aula, dias_horas in entradas:
            n = nombre.get().strip()
            a = aula.get().strip()
            if not n or not a:
                messagebox.showwarning("Campos vacíos", "Completa todos los campos antes de guardar.")
                return

            dias_y_horas_validos = []
            for dia, var, entry_hora in dias_horas:
                if var.get():
                    h = entry_hora.get().strip()
                    if not validar_hora(h):
                        messagebox.showerror("Error", f"Hora inválida para {dia} en curso '{n}'.")
                        return
                    dias_y_horas_validos.append(f"{dia}:{h}")

            if not dias_y_horas_validos:
                messagebox.showwarning("Falta información", f"Selecciona al menos un día y hora para el curso '{n}'.")
                return

            texto_dias = ", ".join(dias_y_horas_validos)

            if rol.lower() == "alumno":
                cursor.execute(
                    "INSERT INTO cursos (alumno_id, nombre, aula, hora_inicio, dias_semana) VALUES (?, ?, ?, ?, ?)",
                    (usuario_id, n, a, None, texto_dias)
                )
            else:
                cursor.execute(
                    "INSERT INTO cursos (docente_id, nombre, aula, hora_inicio, dias_semana) VALUES (?, ?, ?, ?, ?)",
                    (usuario_id, n, a, None, texto_dias)
                )

            cursos_guardados.append((n, a, dias_y_horas_validos))

        conn.commit()
        conn.close()

        conn = conectar()
        cursor = conn.cursor()
        if rol.lower() == "alumno":
            cursor.execute("SELECT correo, nombre FROM alumnos WHERE id=?", (usuario_id,))
        else:
            cursor.execute("SELECT correo, nombre FROM docentes WHERE id=?", (usuario_id,))
        usuario_info = cursor.fetchone()
        conn.close()

        if usuario_info:
            correo_destino, nombre_usuario = usuario_info
            dias_funcion = {
                "Lunes": schedule.every().monday,
                "Martes": schedule.every().tuesday,
                "Miércoles": schedule.every().wednesday,
                "Jueves": schedule.every().thursday,
                "Viernes": schedule.every().friday,
                "Sábado": schedule.every().saturday,
                "Domingo": schedule.every().sunday,
            }

            for curso, aula, dias_horas in cursos_guardados:
                for dh in dias_horas:
                    dia, hora = dh.split(":", 1)
                    mensaje = f"Hola {nombre_usuario},\n\nTu curso {curso} (Aula: {aula}) empieza a las {hora}."
                    if dia in dias_funcion:
                        dias_funcion[dia].at(hora).do(
                            lambda c=correo_destino, m=mensaje: enviar_correo(c, "Recordatorio de curso", m)
                        )



        messagebox.showinfo("Éxito", "Cursos guardados y notificaciones programadas.")
        win.destroy()

    tk.Button(win, text="Guardar todos", bg="#1abc9c", fg="white", command=guardar_todos).pack(pady=15)
