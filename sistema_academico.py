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




