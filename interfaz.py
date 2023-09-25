from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton
from tkinter import PhotoImage
import time
import tkinter as tk


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
    root.update() # Actualiza la interfaz

    # Simula un tiempo de carga
    root.update
    time.sleep(2)

    if usuario_ingresado in usuarios and contrasena_ingresada == usuarios[usuario_ingresado]:
        resultado_label.configure(text="Inicio de sesión exitoso para {}".format(usuario_ingresado))
    else:
        resultado_label.configure(text="Inicio de sesión fallido. Verifica tus credenciales.")

c_negro = '#010101'
c_morado = "#7f5af0"
c_verde = "#2cb67d"

root = CTk()
root.geometry('500x600+350+20')  # Tamaño de la pantalla
root.minsize(480, 500)
root.config(bg=c_negro)
root.title('Inicio de sesion')

# Ruta de la imagen
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



