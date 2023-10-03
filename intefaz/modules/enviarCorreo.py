from email.message import EmailMessage
import ssl
import smtplib
from base_de_datos import BaseDeDatos
from datetime import datetime
import time
import random
import string
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

    def generar_codigo_verificacion(self, longitud=6):
        """Genera un código de verificación aleatorio."""
        return ''.join(random.choice(string.digits) for _ in range(longitud))

    def verificar_correo(self, email_receptor):
        """Envía un código de verificación al correo del receptor y espera su confirmación."""
        codigo_verificacion = self.generar_codigo_verificacion()
        print(f"Enviando correo a {email_receptor} ")
        try:
            self.enviar_correo(email_receptor, "Código de verificación", f"Tu código de verificación es {codigo_verificacion}")
        except Exception as e:
            print(f"Error al enviar correo: {e}")
            return False
        codigo_usuario = input("Introduce el código de verificación que has recibido en tu correo: ")
        return codigo_verificacion == codigo_usuario

    
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

    