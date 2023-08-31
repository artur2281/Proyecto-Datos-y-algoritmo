import tkinter as tk
from tkinter import messagebox
from registro_persona import RegistroPersona
from persona import Persona
from base_de_datos import BaseDeDatos
from enviarCorreo import EnviadorDeCorreos

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "TEVIS" and password == "12345":
        root.deiconify()
        login_window.destroy()
        show_options()
    else:
        messagebox.showerror("Error", "Incorrect username or password")

def show_options():
    button_agregar.grid(row=5, column=0)
    button_eliminar.grid(row=5, column=1)
    button_mostrar.grid(row=6, column=0)
    button_buscar.grid(row=6, column=1)

def hide_options():
    button_agregar.grid_forget()
    button_eliminar.grid_forget()
    button_mostrar.grid_forget()
    button_buscar.grid_forget()

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

def eliminar_persona():
    hide_options()
    label_codigo.grid(row=0, column=0)
    entry_codigo.grid(row=0, column=1)
    button_confirmar.grid(row=1, column=0, columnspan=2)

def confirmar_eliminar_persona():
    codigo = entry_codigo.get()
    registro.eliminar_persona(codigo)
    messagebox.showinfo("Éxito", "Persona eliminada exitosamente")
    clear_fields()
    show_options()

def mostrar_personas():
    hide_options()
    personas = registro.mostrar_personas()
    messagebox.showinfo("Personas registradas", personas)
    show_options()

def buscar_persona():
    hide_options()
    label_codigo.grid(row=0, column=0)
    entry_codigo.grid(row=0, column=1)
    button_confirmar.grid(row=1, column=0, columnspan=2)

def confirmar_buscar_persona():
    codigo = entry_codigo.get()
    persona = registro.buscar_persona_por_codigo(codigo)
    messagebox.showinfo("Persona encontrada", persona)
    clear_fields()
    show_options()

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

label_nombre = tk.Label(root, text="Nombre y apellido")
label_edad = tk.Label(root, text="Edad")
label_codigo = tk.Label(root, text="Código")
label_correo = tk.Label(root, text="Correo electrónico (sin @gmail.com)")
label_numero = tk.Label(root, text="Número")
label_genero = tk.Label(root, text="Género")
label_fecha_nacimiento = tk.Label(root, text="Fecha de nacimiento")

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

button_agregar = tk.Button(root, text="Agregar persona", command=agregar_persona)
button_eliminar = tk.Button(root, text="Eliminar persona", command=eliminar_persona)
button_mostrar = tk.Button(root, text="Mostrar personas", command=mostrar_personas)
button_buscar = tk.Button(root, text="Buscar persona", command=buscar_persona)

button_confirmar = tk.Button(root, text="Confirmar", command=confirmar_agregar_persona)

root.withdraw()

login_window = tk.Tk()
login_window.title("Login")

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