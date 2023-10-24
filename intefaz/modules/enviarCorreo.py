from email.message import EmailMessage
import ssl
import smtplib
from base_de_datos import BaseDeDatos
from datetime import datetime
import time
import random
import string

class EnviadorDeCorreos:
    def __init__(self):
        self.email_emisor = 'trabajosgrupalesdelcole@gmail.com'
        self.email_contrasena ='dysa uxym osmb wuci'
        self.email_contrasena = 'dysa uxym osmb wuci'
    

        self.nombre = None 
    def set_nombre(self,nombre):
        self.nombre = nombre
        


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

    def enviar_codigo_verificacion (self, email_receptor):
        """Envía un código de verificación al correo del receptor y espera su confirmación."""
    def enviar_codigo_verificacion(self, email_receptor):
        codigo_verificacion = self.generar_codigo_verificacion()
        print(f"Enviando código de verificación a {email_receptor}")
        try:
            self.enviar_correo(email_receptor, "Código de verificación", f"Tu código de verificación es {codigo_verificacion}")
        except Exception as e:
            print(f"Error al enviar correo: {e}")
            return False
        
        return codigo_verificacion
    def comparar_codigos(self,codigo_verificacion,codigo_usuario):
        return codigo_verificacion

    def comparar_codigos(self, codigo_verificacion, codigo_usuario):
        
        if codigo_verificacion == codigo_usuario:
        # Los códigos son iguales, la verificación es exitosa
            return True
        else:
            # Los códigos no son iguales, la verificación falla
            return False

    def programar_correo(self):
        db = BaseDeDatos()
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

    def mensaje_personalisado(self):
        db = BaseDeDatos()
        recipients = db.obtener_datos()
        ahora = datetime.now()
        
        mensaje_cumpleanos_hombre = """Asunto: Felicitaciones de Cumpleaños

        Estimado {nombre},


        En este día especial, queremos expresar nuestro reconocimiento por tu dedicación y contribución significativa a nuestra empresa. Tu capacidad para superar desafíos con determinación y tu compromiso con la excelencia son inspiradores. Eres un miembro valioso de nuestro equipo y estamos agradecidos por tu arduo trabajo y dedicación continua.

        Nos alegra ver cómo has crecido en nuestra empresa y cómo has contribuido a nuestra cultura empresarial con tus sólidas relaciones interpersonales y actitud positiva. Te enviamos este ramo de felicidad y nuestros mejores deseos en tu cumpleaños. Que este nuevo año de vida te traiga éxito en tus proyectos, buena salud y momentos felices con tus seres queridos.

        Esperamos que este cumpleaños sea el comienzo de un año lleno de logros y momentos inolvidables. Valoramos enormemente tu trabajo y esperamos celebrar más éxitos juntos.

        ¡Feliz cumpleaños, {nombre}! Que tengas un día maravilloso y un año lleno de éxito y felicidad.

        Con aprecio, La empresa VISGALI"""

        

        mensaje_cumpleanos_mujer = """Asunto: Felicitaciones de Cumpleaños

        Estimada {nombre},

        En este día lleno de alegría y celebración, queremos detenernos un momento para reconocer y honrar a una empleada excepcional: tú. Hoy, estamos celebrando no solo tu cumpleaños, sino también tu valiosa contribución a nuestra empresa y equipo.

        Tu dedicación incansable, tu profesionalismo ejemplar y tu actitud positiva son verdaderamente inspiradores para todos nosotros. Eres mucho más que una empleada; eres una parte fundamental de nuestro equipo, y estamos increíblemente agradecidos por tenerte con nosotros.

        En cada proyecto, en cada desafío, has demostrado ser una fuerza confiable y poderosa. Tu ética laboral y tu habilidad para superar obstáculos no tienen comparación. En este día especial, queremos expresarte nuestra más sincera gratitud por tu arduo trabajo y dedicación.

        Que este nuevo año en tu vida esté lleno de momentos inolvidables, logros personales y profesionales, y mucha felicidad. Esperamos que este día te brinde todo lo que mereces y más.

        ¡Que tengas un cumpleaños lleno de alegría, risas y amor! Disfruta cada momento de este día especial, porque te lo mereces. Estamos emocionados de compartir este día contigo y esperamos que este año esté lleno de éxito y realización personal para ti.

        Una vez más, ¡feliz cumpleaños, {nombre}! Que este sea el mejor año hasta ahora, y que sigamos celebrando muchos más juntos.

        Con aprecio, La empresa VISGALI"""


        for recipient in recipients:
            genero_recipient = recipient['genero']
            nombre_recipient = recipient['nombre']
            fecha_nacimiento = datetime.strptime(recipient['fecha_nacimiento'], '%d/%m/%Y')

            # Verificar si la fecha de nacimiento coincide con la fecha actual
            if fecha_nacimiento.month == ahora.month and fecha_nacimiento.day == ahora.day:

                #Aqui se define si el mesanje para un hombre o mujer(y que cada nombre sea diferente de cada persona)
                if genero_recipient == 'F':
                    mensaje = mensaje_cumpleanos_mujer.format(nombre=nombre_recipient)
                elif genero_recipient == 'M':
                    mensaje = mensaje_cumpleanos_hombre.format(nombre=nombre_recipient)
                else:
                    print(f"No se reconoce el género para {nombre_recipient}")

            

                # Aquí debes enviar el mensaje a través de tu método de envío de correo
                email_receptor = recipient['correo']
                self.enviar_correo(email_receptor, "Feliz cumpleaños", mensaje)
                print(nombre_recipient)  # Mover la impresión del nombre aquí
                print(f"Correo enviado a {email_receptor}")

        print("Saliendo del bucle")  # Esta línea se mueve fuera del bucle
        
        


