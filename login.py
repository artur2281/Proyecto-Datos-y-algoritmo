from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

#iniciar la apli

app = QtWidgets.QApplication([])
#Cargar archivos

login = uic.loadUi("G:\Proyecto final\Proyecto-Datos-y-algoritmo\images\diseñofeliciaciones\login.ui")
menu = uic.loadUi("G:\Proyecto final\Proyecto-Datos-y-algoritmo\images\diseñofeliciaciones\menu.ui")

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

# Conectar el botón de inicio de sesión a la función gui_login
login.pushButton.clicked.connect(gui_login)

# Ejecutar la aplicación
login.show()
app.exec_()


