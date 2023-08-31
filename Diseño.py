#para abrir la aplicación grafica se agrega la extencion pyw 


from tkinter import *

raiz=Tk()

raiz.title("VENTANA DE PRUEBA")#TITULO DE VENTANA.
#raiz.resizable(1,1)#ventanas de redimención
raiz.iconbitmap("gato.png")#esto es para poner el icono en la barra de busqueda esto tiene que estar en icon
#raiz.geometry("650x350") #definsir el ancho de la pantalla
raiz.config(bg="blue")#para poner los colores.
miFrame = Frame( width=500, height=400) #fijamos la funcion frame en una variable.
miFrame.pack() #enpaquetamos el frame

miFrame.config(bg="red")

miFrame.config(width= "650",height="350")
miFrame.config(bd = 35)#para poner el borde

miFrame.config(relief="groove")#para cambiar el borde
mensaje = "mesajes de felicitaciones"
miLabel = Label(miFrame, text=mensaje,fg="red",font=("Comic Sans MS",18)).place(x= 40,y = 10)#nos permite poner el texto en cualquier parte del frame

cuadroTexto = Entry(raiz) 
cuadroTexto.pack()

print(cuadroTexto)
raiz.mainloop() #es un metodo infinito.

