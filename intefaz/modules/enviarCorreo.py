from email.message import EmailMessage
import ssl
import smtplib
from modules.base_de_datos import BaseDeDatos
from datetime import datetime
import time
import random
import string

class EnviadorDeCorreos:
    def __init__(self, email_emisor, email_contrasena):
        self.email_emisor = email_emisor
        self.email_contrasena = email_contrasena
    

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

    def verificar_correo(self, email_receptor,codigo_usuario):
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

    def mensaje_personalisado(self):
        db = BaseDeDatos("G:\Proyecto final\Proyecto-Datos-y-algoritmo\intefaz\personas.xlsx")
        recipients = db.obtener_datos()
        
        mensaje_cumpleanos_hombre = """
        Asunto: Felicitaciones de Cumpleaños

        Estimado {nombre},

        En este día tan especial, queremos tomar un momento para celebrar contigo y desearte un 
        cumpleaños lleno de alegría y momentos inolvidables. Queremos reconocer y apreciar 
        sinceramente tu dedicación y contribución significativa a nuestro equipo y empresa.

        {nombre}, tu capacidad para enfrentar desafíos con determinación y tu compromiso con la 
        excelencia son verdaderamente inspiradores. Has demostrado ser un miembro valioso de nuestro 
        equipo, y estamos agradecidos por tu arduo trabajo y tu dedicación continua.

        Es un placer para nosotros ver cómo has prosperado y has crecido en nuestra empresa. Tu 
        habilidad para establecer relaciones sólidas con tus compañeros de trabajo y tu actitud 
        positiva han contribuido significativamente a nuestra cultura empresarial. Estamos encantados 
        de que hayas encontrado un hogar en nuestro equipo.

        En tu día especial, te enviamos este ramo de felicidad y nuestros mejores deseos. Que este 
        nuevo año de vida te traiga éxito en tus proyectos, salud para disfrutarlo y momentos felices 
        con tus seres queridos.

        Que este cumpleaños sea solo el comienzo de un año lleno de logros, aprendizajes y momentos 
        inolvidables. Apreciamos todo lo que haces y esperamos seguir celebrando tus éxitos junto a ti.

        ¡Feliz cumpleaños, {nombre}! Que tengas un día maravilloso y un año lleno de éxito y felicidad.

        Con aprecio,
        VISGALI
        """

        mensaje_cumpleanos_mujer = """
        Asunto: Felicitaciones de Cumpleaños

        Estimada {nombre},

        En este día lleno de alegría y celebración, queremos detenernos un momento para 
        reconocer y honrar a una empleada excepcional: tú. Hoy, estamos celebrando no 
        solo tu cumpleaños, sino también tu valiosa contribución a nuestra empresa y equipo.

        Tu dedicación incansable, tu profesionalismo ejemplar y tu actitud positiva son 
        verdaderamente inspiradores para todos nosotros. Eres mucho más que una empleada; 
        eres una parte fundamental de nuestro equipo, y estamos increíblemente agradecidos 
        por tenerte con nosotros.

        En cada proyecto, en cada desafío, has demostrado ser una fuerza confiable y poderosa. 
        Tu ética laboral y tu habilidad para superar obstáculos no tienen comparación. En este 
        día especial, queremos expresarte nuestra más sincera gratitud por tu arduo trabajo y 
        dedicación.

        Que este nuevo año en tu vida esté lleno de momentos inolvidables, logros personales y 
        profesionales, y mucha felicidad. Esperamos que este día te brinde todo lo que mereces 
        y más.

        ¡Que tengas un cumpleaños lleno de alegría, risas y amor! Disfruta cada momento de este 
        día especial, porque te lo mereces. Estamos emocionados de compartir este día contigo y 
        esperamos que este año esté lleno de éxito y realización personal para ti.

        Una vez más, ¡feliz cumpleaños, {nombre}! Que este sea el mejor año hasta ahora, y que 
        sigamos celebrando muchos más juntos.

        Con aprecio,
        VISGALI
        """

        for recipient in recipients:
            genero_recipient = recipient['genero']
            nombre_recipient = recipient['nombre']
            nombre = nombre_recipient
            print(nombre_recipient)

            if genero_recipient == 'F':
                mensaje = mensaje_cumpleanos_mujer.format(nombre=nombre)
                return   mensaje
            elif genero_recipient == 'M':
                mensaje = mensaje_cumpleanos_hombre.format(nombre=nombre)
                return mensaje
            else:
                print("No se reconoce el género")
