
""" import pywhatkit

#usaremos este metedo de la libreria se nesecitaran 4 
#parametros nr telefono, mensaje, tiempo en horas y min
x=0
for i in range(4):
    x = x+1
    texto = f"prueba{x}"
    pywhatkit.sendwhatmsg("+51 997 322 971",texto,9,2 )

# ahora agreamos parametros, tiempo de espera para que el mensaaje sea enviado, 
#El otro es es si queremos cerar el whatsap, ademas cerar la pestaña
pywhatkit.sendwhatmsg("+51 997 322 971","hola",8,35,15,True,2)  """
import pywhatkit as kit
import time

# Número de veces que deseas enviar el mensaje con imagen
num_envios = 5
x = 1
y = 40
for i in range(num_envios):
    texto = f"Prueba {i + 1}"
    imagen_path = "gato.png"  # Ruta de la imagen que deseas enviar
    y +=1
    # Enviar mensaje con imagen adjunta
    kit.sendwhatmsg("+51 997 322 971", texto, int(x), int(y))

    # Espera un tiempo antes de enviar el siguiente mensaje con imagen
    if i < num_envios - 1:
        tiempo_espera = 1  # Tiempo en segundos
        time.sleep(tiempo_espera)