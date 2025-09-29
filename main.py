import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv()

email_sender="ae86mm@gmail.com"
password = os.getenv("PASSWORD")
email_reciver="ae86mm@gmail.com"

subject = "RECORDATORIO"
body=("ya no te quiero")

em=EmailMessage()
em["from"] = email_sender
em["to"] = email_reciver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()



with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(email_sender,password)
    smtp.sendmail(email_sender,email_reciver,em.as_string())




