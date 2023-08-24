import pywhatkit

#usaremos este metedo de la libreria se nesecitaran 4 
#parametros nr telefono, mensaje, tiempo en horas y min
x=0
for i in range(4):
    x = x+1
    texto = f"prueba{x}"
    pywhatkit.sendwhatmsg("+51 997 322 971",texto,9,2 )

# ahora agreamos parametros, tiempo de espera para que el mensaaje sea enviado, 
#El otro es es si queremos cerar el whatsap, ademas cerar la pestaña
pywhatkit.sendwhatmsg("+51 997 322 971","hola",8,35,15,True,2)