from twilio.rest import Client
from base_de_datos import BaseDeDatos

class WhatsAppBot:
    def __init__(self, account_sid, auth_token, db_file):
        self.client = Client(account_sid, auth_token)
        self.db = BaseDeDatos(db_file)

    def enviar_mensajes(self):
        # Obtener los datos de los destinatarios
        recipients = self.db.obtener_datos()

        # Enviar mensajes a cada destinatario
        for recipient in recipients:
            phone = recipient['numero']
            message = f"Hola {recipient['nombre']}, este es un mensaje de prueba"
            message = self.client.messages.create(
                to=f'whatsapp:{phone}',
                from_='whatsapp:+14155238886', # Número de teléfono de Twilio para WhatsApp
                body=message)
            print(f'Mensaje enviado a {phone}: {message.sid}')

# Crear una instancia de la clase WhatsAppBot
bot = WhatsAppBot('TU_ACCOUNT_SID', 'TU_AUTH_TOKEN', 'recipients.xlsx')

# Enviar mensajes a los destinatarios
bot.enviar_mensajes()
