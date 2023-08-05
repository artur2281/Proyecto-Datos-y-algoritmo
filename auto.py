# Enviar un mensaje usando python
from email.message import EmailMessage # para definir los mensajes
import ssl #para la seguridad 
import smtplib # para hacer el envio

email_emisor='trabajosgrupalesdelcole@gmail.com'
email_contrasena = 'eqnclstodvineoub'
email_receptor  = '25072005abigail@gmail.com'


asunto = 'mensaje de prueba nr no sedafafa'
cuerpo = """
Este mensajee s de prueba felicitaciónes

"""
em=EmailMessage() #esto es un objeto
em['From'] = email_emisor # esto es el emisor
em['To'] = email_receptor
em['Subject'] = asunto # Hay un problema con asunto 
em.set_content(cuerpo)


#as_string transforma un objeto a una cadena de texto


contexto = ssl.create_default_context()# el ssl conexion segura de la limbreria ssl
#enviar el correo
""" Primero se tiene que definir el servidor luego el puerto
y finalmente el contexto"""

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp: 
    smtp.login(email_emisor,email_contrasena) #esto ayuda a logearnos
    smtp.sendmail(email_emisor,email_receptor,em.as_string())