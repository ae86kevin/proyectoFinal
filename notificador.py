import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

CORREO_EMISOR = "ae86mm@gmail.com"
CONTRASENA = os.getenv("PASSWORD")

def enviar_correo(destinatario, asunto, mensaje):
    try:
        msg = MIMEText(mensaje)
        msg["Subject"] = asunto
        msg["From"] = CORREO_EMISOR
        msg["To"] = destinatario

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(CORREO_EMISOR, CONTRASENA)
            server.send_message(msg)

        print(f"Correo enviado a {destinatario}")
        return True
    except Exception as e:
        print("completado ", e)
        return False
