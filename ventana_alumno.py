import tkinter as tk
from tkinter import messagebox
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
            descripcion TEXT,
            FOREIGN KEY(alumno_id) REFERENCES alumnos(id)
        )
    """)

    conn.commit()
    conn.close()


def ventana_alumno(nombre, alumno_id):
    ventana = tk.Toplevel()
    ventana.title(f"Panel del alumno - {nombre}")
    ventana.geometry("400x350")
    ventana.config(bg="#e0f7fa")

    tk.Label(ventana, text=f"Bienvenido, {nombre} ", font=("Arial", 14, "bold"), bg="#e0f7fa").pack(pady=15)

    frame = tk.Frame(ventana, bg="#e0f7fa")
    frame.pack(pady=10)

