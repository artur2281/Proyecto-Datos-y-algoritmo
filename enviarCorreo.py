from email.message import EmailMessage
import ssl
import smtplib
from base_de_datos import BaseDeDatos
from datetime import datetime
import time

class EnviadorDeCorreos:
    def __init__(self, email_emisor, email_contrasena):
        self.email_emisor = email_emisor
        self.email_contrasena = email_contrasena

    def enviar_correo(self, email_receptor, asunto, cuerpo):
        em = EmailMessage()
        em['From'] = self.email_emisor
        em['To'] = email_receptor
        em['Subject'] = asunto
        em.set_content(cuerpo)

        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(self.email_emisor, self.email_contrasena)
            smtp.sendmail(self.email_emisor, email_receptor, em.as_string())

    def programar_correo(self):
        db = BaseDeDatos('personas.xlsx')
        while True:
            ahora = datetime.now()
            destinatarios = db.obtener_datos()
            for destinatario in destinatarios:
                fecha_nacimiento = datetime.strptime(destinatario['fecha_nacimiento'], '%d/%m/%Y')
                if fecha_nacimiento.month == ahora.month and fecha_nacimiento.day == ahora.day:
                    email_receptor = destinatario['correo']
                    self.enviar_correo(email_receptor, "Feliz cumpleaños", "Feliz cumpleaños")
                    print(f"Correo enviado a {email_receptor} en {ahora}")
            time.sleep(60*60*24) # dormir durante un día
