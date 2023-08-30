from registro_persona import *
from persona import *
from tkinter import *
# DANDO NOMBRES DE LOS OBJETOS
registro = RegistroPersona()

#--------------------- Crear objeto de la clase RegistroPersona

raiz = Tk()
raiz.title("menu")
raiz.config(background= "blue")



#CREANDO LABELS Y ENTRYS..
miFrame = Frame(width=500, height=400)
miFrame.config(bg="red")
nombre_label = Label(miFrame, text="Nombre y apellido:")
nombre_entry = Entry(miFrame)
edad_label = Label(miFrame, text="Edad:")
edad_entry = Entry(miFrame)
codigo_label = Label(miFrame, text="Código:")
codigo_entry = Entry(miFrame)
correo_label = Label(miFrame, text="Correo electrónico:")
correo_entry = Entry(miFrame)
numero_label = Label(miFrame, text="Numero:")
numero_entry = Entry(miFrame)
fecha_nacimiento_label = Label(miFrame,text="Fecha de nacimiento(dd/mm/aaaa): ")
fecha_nacimiento_entry = Entry(miFrame)
genero_label = Label(miFrame, text="Genero(F/M): ")
genero_entry = Entry(miFrame)

codigo_eliminar_label = Label(raiz, text="Código a eliminar:")
codigo_eliminar_entry = Entry(raiz)
codigo = codigo_eliminar_entry.get()




#-------------------------------------BOTON PARA MOSTRAR LOS BOTONES DE INICIO---------------------+

def mostrar_botones():
    agregarPersona.pack()
    eliminarPersona.pack()
    mostrarPersonas.pack()
    buscarPersona.pack()
    salir_button.pack()

#----------------------------------------ELIMINAR BOTONES--------------------------------------------
def eliminar_botones():
    agregarPersona.pack_forget()
    eliminarPersona.pack_forget()
    mostrarPersonas.pack_forget()
    buscarPersona.pack_forget()
    

   
#----------------------------------------OCULTAR FICHA DE AGREGAAR PERSONAS--------------------------------------------
def ocultar_campos():
    nombre_label.pack_forget()
    nombre_entry.pack_forget()
    edad_label.pack_forget()
    edad_entry.pack_forget()
    codigo_label.pack_forget()
    codigo_entry.pack_forget()
    correo_label.pack_forget()
    correo_entry.pack_forget()
    numero_label.pack_forget()
    genero_label.pack_forget()
    fecha_nacimiento_label.pack_forget()
    numero_entry.pack_forget()
    genero_entry.pack_forget()
    fecha_nacimiento_entry.pack_forget()

#----------------------------BOTON PARA ENTRAR AL BOTON PARA AGREGAR PERSONAS-------------------------------

def entrar_al_boton_agregarPersona():
    eliminar_botones()
    miFrame.pack()
    nombre_label.pack()
    nombre_entry.pack()
    edad_label.pack()
    edad_entry.pack()
    codigo_label.pack()
    codigo_entry.pack()
    correo_label.pack()
    correo_entry.pack()
    numero_label.pack()
    numero_entry.pack()
    genero_label.pack()
    genero_entry.pack()
    fecha_nacimiento_label.pack()
    fecha_nacimiento_entry.pack()
    botton_agregar_persona.pack()
#-------------------------------------BOTON PARA AGREGAR PERSONAS---------------------------
def agregarPersona_click():
    
        nombre = nombre_entry.get()
        codigo = codigo_entry.get()
        edad = edad_entry.get()
        correo = correo_entry.get()
        numero = numero_entry.get()
        genero = genero_entry.get()
        fecha_nacimiento = fecha_nacimiento_entry.get()
    
        persona = Persona(nombre, codigo, edad, correo, numero, genero, fecha_nacimiento)
        registro.agregar_persona(persona)
        
    
#-----------------------------BOTON PARA ENTRAR AL BOTTON PARA MOSTRAR PERSONAS--------------------------------

def entrar_al_boton_mostrarPersonas():
    eliminar_botones()
    detalles_personas = registro.mostrar_personas()
    for detalles in detalles_personas:
        label = Label(miFrame, text=detalles)
        label.pack()
#---------------------------------BOTTON PARA ENTRAR A ELIMINAR PERSONAS ----------------------------
def entrar_al_boton_eliminarPersonas():
    eliminar_botones()
    codigo_eliminar_label.pack()
    codigo_eliminar_entry.pack()
    registro.eliminar_persona(codigo)
#--------------------------- 
def entrar_al_boton_buscarPersonas():
    eliminar_botones()

#--------------------------------boton salir----------------------------------------------------------
def cerrar_ventana():
   raiz.destroy()

#--------------------------------boton retroceder----------------------------------------------------------
def retroceder():
    ocultar_campos()
    mostrar_botones()

# -----------------------------agregando botoones -------------------------------------------------------
agregarPersona = Button(raiz, text="Agregar Persona",command=entrar_al_boton_agregarPersona)
eliminarPersona = Button(raiz, text="Eliminar persona",command=entrar_al_boton_eliminarPersonas)
mostrarPersonas = Button(raiz, text= " Mostrar Personas",command= entrar_al_boton_mostrarPersonas)
buscarPersona = Button(raiz, text="Buscar persona ",command=entrar_al_boton_buscarPersonas)
salir_button = Button(raiz, text="Salir", command=cerrar_ventana)
volver_al_menu_guardarDatos = Button(raiz, text="volver al menu y guardar los datos ")
boton_retroceder = Button(raiz, text="Retroceder", command=retroceder)
botton_agregar_persona= Button(miFrame, text="Agregar", command=agregarPersona_click)
boton_retroceder.pack()



#-----------------------------------FRAME PRINCIPAL------------------------------------------------------
mostrar_botones()



# Iniciar bucle principal
raiz.mainloop()
