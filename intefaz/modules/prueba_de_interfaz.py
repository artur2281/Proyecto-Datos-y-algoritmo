from tkinter import messagebox
from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton
from tkinter import PhotoImage
import time
import tkinter as tk

# Función para configurar el estilo de los widgets
def configurar_widget(widget):
    widget.configure(
        font=('sans serif', 12),
        bg=c_verde,  # Color de fondo verde
        fg=c_verde,  # Color del texto verde
        border_width=0,  # Ancho del borde igual a 0 para eliminarlo
        width=220,  # Ancho ajustable según tu preferencia
        height=40  # Altura ajustable según tu preferencia
    )

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
        abrir_menu_principal()  # Llama a la función para abrir el menú principal
    else:
        resultado_label.configure(text="Inicio de sesión fallido. Verifica tus credenciales.")

# Variables globales para los botones y etiqueta del menú principal
boton_agregar = None
boton_mostrar = None
boton_eliminar = None
boton_buscar = None
boton_editar = None
boton_salir = None
resultado_label_menu = None

# Funciones para las opciones del menú
def abrir_menu_principal():
    global boton_agregar, boton_mostrar, boton_eliminar, boton_buscar, boton_editar, boton_salir, resultado_label_menu

    # Ocultar la ventana de inicio de sesión
    root.withdraw()

    # Crear una ventana secundaria para el menú principal
    menu_principal = tk.Toplevel()
    menu_principal.geometry('500x500')  # Tamaño de la ventana del menú principal
    menu_principal.title('Menú Principal')

    # Encabezado "Menu de Opciones"
    CTkLabel(menu_principal, text="Menu de Opciones", font=('sans serif', 16)).pack(pady=10)

    # Funciones para las opciones del menú
    def agregar():
        resultado_label_menu.configure(text="Opción Agregar seleccionada")

    def mostrar():
        resultado_label_menu.configure(text="Opción Mostrar seleccionada")

    def eliminar():
        resultado_label_menu.configure(text="Opción Eliminar seleccionada")

    def buscar():
        resultado_label_menu.configure(text="Opción Buscar seleccionada")

    def editar():
        resultado_label_menu.configure(text="Opción Editar seleccionada")

    def salir():
        menu_principal.destroy()  # Cerrar la ventana del menú principal
        root.deiconify()  # Mostrar la ventana de inicio de sesión nuevamente

    # Crear botones para las opciones del menú
    boton_agregar = CTkButton(menu_principal, text="Agregar", command=agregar, width=15, height=2)
    boton_mostrar = CTkButton(menu_principal, text="Mostrar", command=mostrar, width=15, height=2)
    boton_eliminar = CTkButton(menu_principal, text="Eliminar", command=eliminar, width=15, height=2)
    boton_buscar = CTkButton(menu_principal, text="Buscar", command=buscar, width=15, height=2)
    boton_editar = CTkButton(menu_principal, text="Editar", command=editar, width=15, height=2)
    boton_salir = CTkButton(menu_principal, text="Salir", command=salir, width=15, height=2)

    # Configurar el estilo de los botones
    for boton in [boton_agregar, boton_mostrar, boton_eliminar, boton_buscar, boton_editar, boton_salir]:
        configurar_widget(boton)
        boton.pack(pady=5)

    # Etiqueta para mostrar el resultado en el menú principal
    resultado_label_menu = CTkLabel(menu_principal, font=('sans serif', 12))
    resultado_label_menu.pack(pady=10)

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




