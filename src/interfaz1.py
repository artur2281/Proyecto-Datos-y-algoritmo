import tkinter as tk
from tkinter import messagebox
from src.modules.registro_persona import RegistroPersona
from src.modules.persona import Persona
from src.modules.base_de_datos import BaseDeDatos
from src.modules.enviarCorreo import EnviadorDeCorreos
from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton
from tkinter import PhotoImage
import time
#----------------------FUNCION PARA INGRESAR------------------------------
# Define los usuarios y contraseñas válidos en un diccionario
usuarios = {
    "ELIA": "111",
    "TEVIS": "222",
    "ABIGAIL": "333"
}

# Función para verificar la autenticación
def iniciar_sesion():
    usuario_ingresado = entry_usuario.get()
    contrasena_ingresada = entry_contrasena.get()

    resultado_label.configure(text="Iniciando sesión...")  # Muestra un mensaje de carga
    root.update() #Actualiza la interfaz

    #Tiempo de carga
    root.update() 
    time.sleep(3)

    if usuario_ingresado in usuarios and contrasena_ingresada == usuarios[usuario_ingresado]:
        resultado_label.configure(text="Inicio de sesión exitoso para {}".format(usuario_ingresado))
    else:
        resultado_label.configure(text="Inicio de sesión fallido. Verifica tus credenciales.")


c_negro = '#010101'
c_morado = "#7f5af0"
c_verde = "#2cb67d"

root = CTk()
root.geometry('500x600+350+20')  #Tamño de la pantalla
root.minsize(480, 500)
root.config(bg=c_negro)
root.title('Inicio de sesion')

#Ruta de la imagen
logo = PhotoImage(file='images/logo.png')

frame = CTkFrame(root, fg_color=c_negro)
frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

frame.columnconfigure([0, 1], weight=1)
frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# usamos CTkLabel para la imagen
CTkLabel(frame, image=logo).grid(columnspan=2, row=0)

# Para las ventanas de usuario y contraseña
entry_usuario = CTkEntry(frame, font=('sans serif', 12), placeholder_text='Usuario',
    border_color=c_verde, fg_color=c_negro, width=220, height=40)
entry_usuario.grid(columnspan=2, row=1, padx=4, pady=4)

# Usamos * para ocultar la contraseña con asteriscos
entry_contrasena = CTkEntry(frame, font=('sans serif', 12), placeholder_text='Contraseña',
    border_color=c_verde, fg_color=c_negro, width=220, height=40, show='*')
entry_contrasena.grid(columnspan=2, row=2, padx=4, pady=4)

bt_iniciar = CTkButton(frame, font=('sans serif', 12), border_color=c_verde, fg_color=c_negro,
    hover_color=c_verde, corner_radius=12, border_width=2, text='INICIAR SESIÓN',
    height=40, command=iniciar_sesion)
bt_iniciar.grid(columnspan=2, row=3, pady=4, padx=4)

# Etiqueta para mostrar el resultado
resultado_label = CTkLabel(frame, font=('sans serif', 12), fg_color=c_negro)
resultado_label.grid(columnspan=2, row=5, pady=4, padx=4)
root.call('wm', 'iconphoto', root._w, logo)

# Ejecutar la aplicación
root.mainloop()
#--------------------FUNCION DE OPCIONES---------------------------------------------
def show_options():
    button_agregar.grid(row=5, column=0)
    button_eliminar.grid(row=5, column=1)
    button_mostrar.grid(row=6, column=0)
    button_buscar.grid(row=6, column=1)
#---------------------BOTON RETROCEDER-------------------------------------------------
def back():
    clear_fields()
    hide_options()
    show_options()
    hide_agregar_persona_screen()
#----------------------OCULTAR BOTONES
def hide_options():
    button_agregar.grid_forget()
    button_eliminar.grid_forget()
    button_mostrar.grid_forget()
    button_buscar.grid_forget()
#-----------------ocultar FICHERO DE AGREGAR PERSONA---------------------
def hide_agregar_persona_screen():
    label_nombre.grid_forget()
    entry_nombre.grid_forget()

    label_edad.grid_forget()
    entry_edad.grid_forget()

    label_codigo.grid_forget()
    entry_codigo.grid_forget()

    label_correo.grid_forget()
    entry_correo.grid_forget()

    label_numero.grid_forget()
    entry_numero.grid_forget()

    label_genero.grid_forget()
    entry_genero.grid_forget()

    label_fecha_nacimiento.grid_forget()
    entry_fecha_nacimiento.grid_forget()

    button_confirmar.grid_forget()
    button_retroceder.grid_forget()
#----------------FICHA PARA AGREGAR personas------------
def agregar_persona():
    hide_options()
    label_nombre.grid(row=0, column=0)
    entry_nombre.grid(row=0, column=1)

    label_edad.grid(row=1, column=0)
    entry_edad.grid(row=1, column=1)

    label_codigo.grid(row=2, column=0)
    entry_codigo.grid(row=2, column=1)

    label_correo.grid(row=3, column=0)
    entry_correo.grid(row=3, column=1)

    label_numero.grid(row=4, column=0)
    entry_numero.grid(row=4, column=1)

    label_genero.grid(row=5, column=0)
    entry_genero.grid(row=5, column=1)

    label_fecha_nacimiento.grid(row=6, column=0)
    entry_fecha_nacimiento.grid(row=6, column=1)

    button_confirmar.grid(row=7, column=0, columnspan=2)
    button_retroceder.grid(row=8,column = 0, columnspan=3)

#----------------CONFIRMAR AGREGAR PERSONA-------------------------
def confirmar_agregar_persona():
    nombre = entry_nombre.get()
    edad = int(entry_edad.get())
    codigo = entry_codigo.get()
    correo = entry_correo.get()
    numero = entry_numero.get()
    genero = entry_genero.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    op_correo = var.get()
    if op_correo == 1:
        correo = correo + "@gmail.com"
    if op_correo == 2:
        correo = correo + "@hotmail.com"
    if op_correo == 3:
        correo = correo + "@yahoo.com" 

    persona = Persona(nombre, codigo, edad, correo, numero, genero, fecha_nacimiento)
    registro.agregar_persona(persona)
    enviador_de_correos.enviar_correo(correo, "Registro exitoso", "Has sido registrado exitosamente.")

    messagebox.showinfo("Éxito", "Persona agregada exitosamente")
    clear_fields()
    show_options()
#---------------------fUNCION PARA ELIMINAR PERSONA---------------------
def eliminar_persona():
    hide_options()
    label_codigo.grid(row=0, column=0)
    entry_codigo.grid(row=0, column=1)
    button_confirmar.grid(row=1, column=0, columnspan=2)
    button_retroceder.grid(row= 2, column=0, columnspan=2)
#----------------------CONFIRMACION DE ELIMINACION DE PERSONAS----------------------------------------
def confirmar_eliminar_persona():
    codigo = entry_codigo.get()
    registro.eliminar_persona(codigo)
    messagebox.showinfo("Éxito", "Persona eliminada exitosamente")
    clear_fields()
    show_options()
#-----------------------------MOSTRAR PERSONAS---------------------
def mostrar_personas():
    hide_options()
    personas = registro.mostrar_personas()
    messagebox.showinfo("Personas registradas", personas)
    show_options()
    button_retroceder.grid_forget()
#----------------------FUNCION PARA BUSCAR PERSONA-------------------------------------------------
def buscar_persona():
    hide_options()
    label_codigo.grid(row=0, column=0)
    entry_codigo.grid(row=0, column=1)
    button_confirmar.grid(row=1, column=0, columnspan=2)
    button_retroceder.grid(row =2, column=0, columnspan=2)
#----------------------CONFIRMAR PARA BUSCAR PERSONA -------------------------------------------------
def confirmar_buscar_persona():
    codigo = entry_codigo.get()
    persona = registro.buscar_persona_por_codigo(codigo)
    messagebox.showinfo("Persona encontrada", persona)
    clear_fields()
    show_options()
#---------------------PARA LIMPIAR LLA PANTALLA ------------------------------------------------------------------
def clear_fields():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_codigo.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_numero.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_fecha_nacimiento.delete(0, tk.END)

registro = RegistroPersona()
enviador_de_correos = EnviadorDeCorreos('trabajosgrupalesdelcole@gmail.com', 'eqnclstodvineoub')

root = tk.Tk()
root.title("Registro de personas")
#-----------------------------Entrando texto -----------------------------------------
label_nombre = tk.Label(root, text="Nombre y apellido")
label_edad = tk.Label(root, text="Edad")
label_codigo = tk.Label(root, text="Código")
label_correo = tk.Label(root, text="Correo electrónico (sin @gmail.com)")
label_numero = tk.Label(root, text="Número")
label_genero = tk.Label(root, text="Género")
label_fecha_nacimiento = tk.Label(root, text="Fecha de nacimiento")
#----------------Cuadros para rrellenar-----------------------------------------------------
entry_nombre = tk.Entry(root)
entry_edad = tk.Entry(root)
entry_codigo = tk.Entry(root)
entry_correo = tk.Entry(root)
entry_numero = tk.Entry(root)
entry_genero = tk.Entry(root)
entry_fecha_nacimiento = tk.Entry(root)

var = tk.IntVar(value=1)
R1 = tk.Radiobutton(root, text="gmail", variable=var, value=1)
R2 = tk.Radiobutton(root, text="hotmail", variable=var, value=2)
R3 = tk.Radiobutton(root, text="yahoo", variable=var, value=3)
#-------------------------------Agregando botones-----------------------------------
button_agregar = tk.Button(root, text="Agregar persona", command=agregar_persona)
button_eliminar = tk.Button(root, text="Eliminar persona", command=eliminar_persona)
button_mostrar = tk.Button(root, text="Mostrar personas", command=mostrar_personas)
button_buscar = tk.Button(root, text="Buscar persona", command=buscar_persona)
button_retroceder = tk.Button(root,text = " Retroceder ", command=back )

button_confirmar = tk.Button(root, text="Confirmar", command=confirmar_agregar_persona)

root.withdraw()

login_window = tk.Tk()
login_window.title("Login")
#_---------login--------------------------------------------
label_username = tk.Label(login_window, text="Username")
label_username.grid(row=0, column=0)
entry_username = tk.Entry(login_window)
entry_username.grid(row=0, column=1)

label_password = tk.Label(login_window, text="Password")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(login_window, show="*")
entry_password.grid(row=1, column=1)

button_login = tk.Button(login_window, text="Login", command=login)
button_login.grid(row=2, column=0, columnspan=2)

login_window.mainloop()
#------------------------MAIN---------------------------------------------
