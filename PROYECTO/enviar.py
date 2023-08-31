from email.message import EmailMessage
import ssl
from datetime import datetime
import time
import smtplib
from base_de_datos import BaseDeDatos
class EnviadorDeCorreos:
    def __init__(self, email_emisor, email_contrasena):
        self.email_emisor = email_emisor
        self.email_contrasena = email_contrasena

    def enviar_correo(self, direccion, asunto, cuerpo):
        email_receptor = direccion

        em = EmailMessage()
        em['From'] = self.email_emisor
        em['To'] = email_receptor
        em['Subject'] = asunto
        em.set_content(cuerpo)

        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(self.email_emisor, self.email_contrasena)
            smtp.sendmail(self.email_emisor, email_receptor, em.as_string())
            
    def autenticar(self, email_receptor, codigo):
        em = EmailMessage()
        em['From'] = self.email_emisor
        em['To'] = email_receptor
        em['Subject'] = "Codigo de autenticacion"
        em.set_content(codigo)

        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(self.email_emisor, self.email_contrasena)
            smtp.sendmail(self.email_emisor, email_receptor, em.as_string())
    
    def auto_envio(self, email_receptor, fecha_nacimiento):
        em = EmailMessage()
        em['From'] = self.email_emisor
        em['To'] = email_receptor
        em['Subject'] = "Feliz cumpleaños"
        em.set_content("Feliz cumpleaños")

        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(self.email_emisor, self.email_contrasena)
            smtp.sendmail(self.email_emisor, email_receptor, em.as_string())


    def programar_correo(emisor, receptor, fecha_nacimiento):
        while True:
            ahora = datetime.now()
            if ahora.month == fecha_nacimiento.month and ahora.day == fecha_nacimiento.day:
                emisor.auto_envio(receptor, fecha_nacimiento)
                print(f"Correo enviado a {receptor} en {ahora}")
                time.sleep(60*60*24) # dormir durante un día
            else:
                time.sleep(60) # dormir durante un minuto

