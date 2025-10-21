import sqlite3

DB_NAME = "sistema_academico.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS docentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alumno_id INTEGER,
            docente_id INTEGER,
            nombre TEXT NOT NULL,
            aula TEXT NOT NULL,
            hora_inicio TEXT NOT NULL,
            FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
            FOREIGN KEY (docente_id) REFERENCES docentes(id)
        )
    """)

    conn.commit()
    conn.close()
