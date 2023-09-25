from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl, QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore
from PyQt5.QtGui import QDesktopServices
from PyQt5.uic import loadUi
from registro_persona import RegistroPersona
#iniciar la apli
class VentanaPrincipal():
    def __init__(self):
        super(VentanaPrincipal,self).__init__()
        login =loadUi("G:\Proyecto final\Proyecto-Datos-y-algoritmo\images\diseñofeliciaciones\login.ui",self)
        menu =loadUi("G:\Proyecto final\Proyecto-Datos-y-algoritmo\images\diseñofeliciaciones\menu.ui",self)
        
        self.registro_persona = RegistroPersona()
    
      

    
app = QtWidgets.QApplication([])
#Cargar archivos


# En el manejador de eventos del botón (por ejemplo, dentro de una función)
def facebook_url():
    url = QUrl("https://www.facebook.com/vendoabus")  # Cambia la URL por la que desees abrir
    QDesktopServices.openUrl(url)
def twiter_url():
    url = QUrl("https://twitter.com/bi_bgl")  # Cambia la URL por la que desees abrir
    QDesktopServices.openUrl(url)
def instagram_url():
    url = QUrl("https://www.instagram.com/abigail_bgl/")  # Cambia la URL por la que desees abrir
    QDesktopServices.openUrl(url)
# Conecta el botón a la función que abrirá la URL
login.pushButton_5.clicked.connect(facebook_url)
login.pushButton_2.clicked.connect(twiter_url)
login.pushButton_3.clicked.connect(facebook_url)
login.pushButton_4.clicked.connect(instagram_url)


# Función para mostrar la ventana del menú
def gui_menu():
    login.hide()  # Oculta la ventana de inicio de sesión
    menu.show()   # Muestra la ventana del menú

# Función para manejar el inicio de sesión
def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()

    if len(name) == 0 or len(password) == 0:
        print("Ingresa los datos")
    elif name == "abi" and password == "1234":
        gui_menu()  # Mostrar el menú si las credenciales son correctas
    else:
        print("Credenciales incorrectas")  # Manejar credenciales incorrectas aquí


def registrar_persona():
    
    nombre = menu.lineEdit.text()
    codigo = menu.lineEdit_2.text()
    edad = menu.lineEdit_3.text()
    correo = menu.lineEdit_4.text()
    numero = menu.lineEdit_5.text()
    genero = menu.lineEdit_6.text()
    fecha_nacimiento = menu.lineEdit_7.text()
    if len(nombre)==0 or len(codigo)==0 or len(edad)== 0 or len(correo) == 0 or len(numero)== 0 or len(genero)==0 or len(fecha_nacimiento)==0 :
        print("ingrese los datos")   
    else:
        rg = RegistroPersona()
        rg.agregar_persona(nombre, codigo, edad, correo, numero, genero, fecha_nacimiento)
        menu.label_10.setText("Persona registrada correctamente")
        print("ingrese los datos")

def acceder_registrarPesona():
    menu.page_1registrar.show()
def acceder_buscarPersona():
    menu.page_buscar.show()
def buscar_perosna():
    if menu.pushButton_7buscar.isChecked():
        # Mostrar la ventana Page1Registrar

        menu.page_2buscar.show()
        nombre = menu.lineEdit_8.text()
        codigo = menu.lineEdit_9.text()
        edad = menu.lineEdit_10.text()
        correo = menu.lineEdit_11.text()
        numero = menu.lineEdit_12.text()
        genero = menu.lineEdit_13.text()
        fecha_nacimiento = menu.lineEdit_14.text()

        rg = RegistroPersona()
        rg.buscar_persona(nombre, codigo, edad, correo, numero, genero, fecha_nacimiento)
        print("persona registradacorectamente")

# Conectar el botón de inicio de sesión a la función gui_login
login.pushButton.clicked.connect(gui_login)

#botones del menu
menu.pushButton_REGISTRAR.clicked.connect(acceder_registrarPesona)
menu.pushButton_BUSCAR.clicked.connect(acceder_buscarPersona)

#botones de registrar
menu.pushButton_6registrar.clicked.connect(registrar_persona)

# Ejecutar la aplicación
login.show()
app.exec_()


