from base_de_datos import BaseDeDatos
from whasapp import Automatizacion  # Importa la clase Automatizacion
import time
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
            ruta = "G:\Proyecto final\Proyecto-Datos-y-algoritmo\images\logo.png"
            self.automatizacion.bot_whatsapp(phone, ruta, nombre)  # Llama al método de Automatizacion
            time.sleep(3)
            print("saliendo del bucle")


def enviadorCorreos():
    # Definir asunto y cuerpo del correo
    asunto = "Asunto del correo"
    cuerpo = "Cuerpo del correo"
    
    # Crear instancia de EnviadorDeCorreos
    enviador_de_correos = EnviadorDeCorreos('trabajosgrupalesdelcole@gmail.com', 'dysa uxym osmb wuci')
    
    # Crear instancia de RegistroPersona para obtener los correos electrónicos
    rp = RegistroPersona()
    
    # Obtener la lista de correos electrónicos
    email_receptores = rp.extraer_emails()
    
    # Iterar a través de la lista de correos electrónicos y enviar correos a cada destinatario
    for email_receptor in email_receptores:
        try:
            # Enviar correo
            enviador_de_correos.enviar_correo(email_receptor, asunto, cuerpo)
            print(f"Correo enviado a {email_receptor}")
        except Exception as e:
            print(f"Error al enviar correo a {email_receptor}: {str(e)}")

# Llamar a la función para enviar correos
enviadorCorreos()

# Crear una instancia de la clase WhatsAppBot
archivo = "personas.xlsx"
bot = WhatsAppBot(archivo)

# Enviar mensajes a los destinatarios
bot.enviar_mensajes()
