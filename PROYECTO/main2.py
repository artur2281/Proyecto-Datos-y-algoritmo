from registro_persona import RegistroPersona
from persona import Persona
from tkinter import *


# Crear objeto de la clase RegistroPersona
raiz = Tk()
raiz.title("Registro de Personas")

# Crear widgets
nombre_label = Label(raiz, text="Nombre y apellido:")
nombre_entry = Entry(raiz)
edad_label = Label(raiz, text="Edad:")
edad_entry = Entry(raiz)
codigo_label = Label(raiz, text="Código:")
codigo_entry = Entry(raiz)
correo_label = Label(raiz, text="Correo electrónico:")
correo_entry = Entry(raiz)
agregar_button = Button(raiz, text="Agregar Persona", command=agregar_persona)
codigo_eliminar_label = Label(raiz, text="Código a eliminar:")
codigo_eliminar_entry = Entry(raiz)
eliminar_button = Button(raiz, text="Eliminar Persona", command=eliminar_persona)
mostrar_button = Button(raiz, text="Mostrar Personas", command=mostrar_personas)

# Organizar widgets en la ventana
nombre_label.pack()
nombre_entry.pack()
edad_label.pack()
edad_entry.pack()
codigo_label.pack()
codigo_entry.pack()
correo_label.pack()
correo_entry.pack()
agregar_button.pack()
codigo_eliminar_label.pack()
codigo_eliminar_entry.pack()
eliminar_button.pack()
mostrar_button.pack()

# Iniciar bucle principal
raiz.mainloop()
