# Solicitar el nombre del destinatario
nombre = input("Por favor, introduce tu nombre: ")

# Mensaje de cumpleaños personalizado usando f-strings
mensaje_cumpleanos = f"""
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
[Nombre de tu Empresa]
"""

# Imprimir el mensaje de cumpleaños
print(mensaje_cumpleanos)
