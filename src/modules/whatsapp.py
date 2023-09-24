from base_de_datos import BaseDeDatos
from automatizacionWhat import Automatizacion  # Importa la clase Automatizacion
import time

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

# Crear una instancia de la clase WhatsAppBot
archivo = "G:\Proyecto final\Proyecto-Datos-y-algoritmo\src\personas.xlsx"
bot = WhatsAppBot(archivo)

# Enviar mensajes a los destinatarios
bot.enviar_mensajes()
