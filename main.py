import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
import time
from datetime import datetime
import interfaz as interfaz





load_dotenv()
email_sender = "ae86mm@gmail.com"
password = os.getenv("PASSWORD")
email_reciver = "kf.tlopez@udeo.edu.gt"

subject = "anda a clase"
body = "tarea"

em = EmailMessage()
em["from"] = email_sender
em["to"] = email_reciver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

FechaEnvio = "2025-09-30 20:00:00"
fecha_objetivo = datetime.strptime(FechaEnvio, "%Y-%m-%d %H:%M:%S")

print(f" {FechaEnvio} ")

while datetime.now() < fecha_objetivo:
    time.sleep(1)

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())
    print("correo enviado")

