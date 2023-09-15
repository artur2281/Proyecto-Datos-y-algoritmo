from base_de_datos import BaseDeDatos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from automatizacionWhat import botWhatsapp 
import time
class WhatsAppBot:
    def __init__(self, archivo_db):
        self.db = BaseDeDatos(archivo_db)

    def enviar_mensajes(self):
        # Obtener los datos de los destinatarios
    
        recipients =self.db.obtener_datos()

        # Enviar mensajes a cada destinatario
        for recipient in recipients:
            phone = recipient['numero']
            nombre = recipient['nombre']
            ruta = "G:\Proyecto final\Proyecto-Datos-y-algoritmo\images\logo.png"
            botWhatsapp(phone,ruta,nombre)


# Crear una instancia de la clase WhatsAppBot

bot = WhatsAppBot()
# Enviar mensajes a los destinatarios
bot.enviar_mensajes()
