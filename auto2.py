from email.message import EmailMessage
import ssl
import smtplib

class Mensaje:
    def __init__(self, emisor, receptor, asunto, cuerpo):
        self.emisor = emisor
        self.receptor = receptor
        self.asunto = asunto
        self.cuerpo = cuerpo

class EnviarMensaje:
    def __init__(self, emisor, contrasena):
        self.emisor = emisor
        self.contrasena = contrasena

    def enviar(self, mensaje):
        em = EmailMessage()
        em['From'] = self.emisor
        em['To'] = mensaje.receptor
        em['Subject'] = mensaje.asunto
        em.set_content(mensaje.cuerpo)

        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(self.emisor, self.contrasena)
            smtp.sendmail(self.emisor, mensaje.receptor, em.as_string())

# Datos de autenticación
email_emisor = 'trabajosgrupalesdelcole@gmail.com'
email_contrasena = 'eqnclstodvineoub'

# Crear instancia de EnviarMensaje
enviador = EnviarMensaje(email_emisor, email_contrasena)

# Crear instancia de Mensaje
asunto = 'Felicitaciones'
cuerpo = """
¡Felicitaciones por tus logros en la empresa!

Atentamente,
El equipo de la empresa
"""
mensaje = Mensaje(email_emisor, 'destinatario@example.com', asunto, cuerpo)

# Enviar el mensaje
enviador.enviar(mensaje)