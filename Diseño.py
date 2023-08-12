from tkinter import *

raiz=Tk()

raiz.title("VENTANA DE PRUEBA")#TITULO DE VENTANA.
raiz.resizable(1,1)#ventanas de redimención
raiz.iconbitmap("gato.png")#esto es para poner el icono en la barra de busqueda esto tiene que estar en icon
raiz.geometry("650x350") #definsir el ancho de la pantalla
raiz.config(bg="blue")
raiz.mainloop() #es un metodo infinito.

