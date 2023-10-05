from base_de_datos import BaseDeDatos
from whasapp import Automatizacion  # Importa la clase Automatizacion
import time
import datetime
from enviarCorreo import EnviadorDeCorreos
from registro_persona import RegistroPersona

class WhatsAppBot:
    def __init__(self, archivo_db):
        self.db = BaseDeDatos(archivo_db)
        self.automatizacion = Automatizacion()  # Crea una instancia de Automatizacion

    def enviar_mensajes(self):
        # Obtener los datos de los destinatarios
        recipients = self.db.obtener_datos()

        # Enviar mensajes a cada destinatario
        for recipient in recipients:
            phone = recipient['numero']
            nombre = recipient['nombre']
            ruta = r"G:\Proyecto final\Proyecto-Datos-y-algoritmo\images\logo.png"
            self.automatizacion.bot_whatsapp(phone, ruta, nombre)  # Llama al método de Automatizacion
            time.sleep(3)
            print("saliendo del bucle")
    def enviar_mensajes_condicionalmente(self):
    # Obtener la fecha actual
        fecha_actual = datetime.date.today()
        
        # Obtener los destinatarios
        recipients = self.db.obtener_datos()

        # Iterar a través de los destinatarios
        for recipient in recipients:
            fecha_recipient = recipient['fecha_nacimiento']  # Supongamos que 'fecha' es el campo con la fecha en tus datos
            print(fecha_actual)
            print(fecha_recipient)
            # Verificar si la fecha en los datos es igual a la fecha actual
            if fecha_recipient == fecha_actual:
                phone = recipient['numero']
                nombre = recipient['nombre']
                ruta = "G:\Proyecto final\Proyecto-Datos-y-algoritmo\images\logo.png"
                
                # Llamar al método de Automatizacion para enviar el mensaje
                self.automatizacion.bot_whatsapp(phone, ruta, nombre)
                
                time.sleep(3)
                print("Mensaje enviado a", nombre)
            else:
                print("Fecha en los datos no coincide con la fecha actual. Omitiendo.")










def enviadorCorreos():
    # Definir asunto y cuerpo del correo
    
    
    
    # Crear instancia de EnviadorDeCorreos
    enviador_de_correos = EnviadorDeCorreos()
    db = BaseDeDatos("G:\Proyecto final\Proyecto-Datos-y-algoritmo\intefaz\personas.xlsx")
    asunto = "Asunto del correo"
    cuerpo = enviador_de_correos.mensaje_personalisado()
    recipients= db.obtener_datos()

        # Enviar mensajes a cada destinatario
    for recipient in recipients:
        email_receptor = recipient['correo']
        ruta = "G:\Proyecto final\Proyecto-Datos-y-algoritmo\images\logo.png"
        try:
            # Enviar correo
            enviador_de_correos.enviar_correo(email_receptor, asunto, cuerpo)
            print(f"Correo enviado a {email_receptor}")
        except Exception as e:
            print(f"Error al enviar correo a {email_receptor}: {str(e)}") 
        time.sleep(3)
        print("saliendo del bucle")
    # Crear instancia de RegistroPersona para obtener los correos electrónicos
    #rp = RegistroPersona()
    
    # Obtener la lista de correos electrónicos
    #email_receptores = rp.extraer_emails()
    
    # Iterar a través de la lista de correos electrónicos y enviar correos a cada destinatario
"""    for email_receptor in email_receptores:
        try:
            # Enviar correo
            enviador_de_correos.enviar_correo(email_receptor, asunto, cuerpo)
            print(f"Correo enviado a {email_receptor}")
        except Exception as e:
            print(f"Error al enviar correo a {email_receptor}: {str(e)}") """





# Llamar a la función para enviar correos
enviadorCorreos()

# Crear una instancia de la clase WhatsAppBot
archivo = "G:\Proyecto final\Proyecto-Datos-y-algoritmo\intefaz\personas.xlsx"
# bot = WhatsAppBot(archivo)
#bot.enviar_mensajes_condicionalmente()
# Enviar mensajes a los destinatarios
#bot.enviar_mensajes()
