# Solicitar el nombre del destinatario
nombre = input("Por favor, introduce tu nombre: ")

# Mensaje de cumpleaños personalizado usando f-strings
mensaje_cumpleanos = f"""
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
[Nombre de tu Empresa]
"""

# Imprimir el mensaje de cumpleaños
print(mensaje_cumpleanos)