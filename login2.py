import sys
import typing

from PyQt5.QtWidgets import QWidget
from menu import *
from PyQt5 import QtCore
from PyQt5.QtCore import QUrl, QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtGui, QtWidgets
from login import *
from PyQt5.QtGui import QDesktopServices
class Login(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui_login = Ui_Form()  # Crear una instancia de la interfaz de usuario de login
		self.ui_login.setupUi(self)  # Configurar la interfaz de usuario
	
		# Conecta el botón a la función que abrirá la URL
		self.ui_login.pushButton_5.clicked.connect(self.facebook_url)
		self.ui_login.pushButton_2.clicked.connect(self.twiter_url)
		self.ui_login.pushButton_3.clicked.connect(self.facebook_url)
		self.ui_login.pushButton_4.clicked.connect(self.instagram_url)
		# Conecta el botón de inicio de sesión a la función que manejará el inicio de sesión

	#botones del menu
	def facebook_url(self):
		url = QUrl("https://www.facebook.com/vendoabus")  # Cambia la URL por la que desees abrir
		QDesktopServices.openUrl(url)
	def twiter_url(self):
		url = QUrl("https://twitter.com/bi_bgl")  # Cambia la URL por la que desees abrir
		QDesktopServices.openUrl(url)
	def instagram_url(self):
		url = QUrl("https://www.instagram.com/abigail_bgl/")  # Cambia la URL por la que desees abrir
		QDesktopServices.openUrl(url)

	# Función para manejar el inicio de sesión
	def gui_login(self):
		name = self.ui_login.lineEdit.text()
		password = self.ui_login.lineEdit_2.text()

		if len(name) == 0 or len(password) == 0:
			print("Ingresa los datos")
		elif name == "abi" and password == "1234":
			self.aceder_menu()
	


class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow() # intanciamos las clases
		

		self.ui.setupUi(self)
		 #incializamos las ventanas
		self.ui_login.setupUi(self)
		#eliminar barra y de titulo - opacidad
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setWindowOpacity(1)
		#SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)
		# mover ventana
		self.ui.frame_superior.mouseMoveEvent = self.mover_ventana
		#acceder a las paginas
		self.ui.pushButton_REGISTRAR.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1registrar))
		self.ui.pushButton_BASEDEDATOS.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageDATOS))	
		self.ui.pushButton_ACTUALIZAR.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_actualizar))
		self.ui.pushButton_BUSCAR.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_buscar))			
		self.ui.pushButton_ELIMINAR.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_eliminar))	

		#control barra de titulos
		self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
		self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
		self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
		self.ui.pushButton.clicked.connect(lambda: self.close())

		self.ui.bt_restaurar.hide()

		#menu lateral
		self.ui.bt_menu.clicked.connect(self.mover_menu)
		
	def control_bt_minimizar(self):
		self.showMinimized()		

	def  control_bt_normal(self): 
		self.showNormal()		
		self.ui.bt_restaurar.hide()
		self.ui.bt_maximizar.show()

	def  control_bt_maximizar(self): 
		self.showMaximized()
		self.ui.bt_maximizar.hide()
		self.ui.bt_restaurar.show()

	def mover_menu(self):
		if True:			
			width = self.ui.frameLateral.width()
			normal = 0
			if width==0:
				extender = 200
			else:
				extender = normal
			self.animacion = QPropertyAnimation(self.ui.frameLateral, b'minimumWidth')
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start()
	## SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
	## mover ventana
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()
	def mover_ventana(self, event):
		if self.isMaximized() == False:			
			if event.buttons() == QtCore.Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()

		if event.globalPos().y() <=20:
			self.showMaximized()
		else:
			self.showNormal()


def aceder_menu():
		login = Login()
		login.hide()  # Ocultar la ventana de inicio de sesión
		mi_app = MiApp()  # Crear una instancia de la ventana del menú
		mi_app.show()  # Mostrar la ventana del menú



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
	from PyQt5.QtWidgets import QWidget

	from menu import *
	from PyQt5 import QtCore
	from PyQt5.QtCore import QUrl, QPropertyAnimation, QEasingCurve
	from PyQt5 import QtCore, QtGui, QtWidgets
	from login import *
	from PyQt5.QtGui import QDesktopServices


	class Login(QtWidgets.QMainWindow):
		def __init__(self):
			pass

		# botones del menu
		def facebook_url(self):
			pass

		def twiter_url(self):
			pass

		def instagram_url(self):
			pass

		# Función para manejar el inicio de sesión
		def gui_login(self):
			pass


	class MiApp(QtWidgets.QMainWindow):
		def __init__(self):
			pass

		def control_bt_minimizar(self):
			pass

		def control_bt_normal(self):
			pass

		def control_bt_maximizar(self):
			self.showMaximized()
			self.ui.bt_maximizar.hide()
			self.ui.bt_restaurar.show()

		def mover_menu(self):
			if True:
				width = self.ui.frameLateral.width()
				normal = 0
				if width == 0:
					extender = 200
				else:
					extender = normal
				self.animacion = QPropertyAnimation(self.ui.frameLateral, b'minimumWidth')
				self.animacion.setDuration(300)
				self.animacion.setStartValue(width)
				self.animacion.setEndValue(extender)
				self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
				self.animacion.start()

		# SizeGrip
		def resizeEvent(self, event):
			rect = self.rect()
			self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

		# mover ventana
		def mousePressEvent(self, event):
			self.clickPosition = event.globalPos()

		def mover_ventana(self, event):
			if self.isMaximized() == False:
				if event.buttons() == QtCore.Qt.LeftButton:
					self.move(self.pos() + event.globalPos() - self.clickPosition)
					self.clickPosition = event.globalPos()
					event.accept()

			if event.globalPos().y() <= 20:
				self.showMaximized()
			else:
				self.showNormal()


	def aceder_menu():
		login = Login()
		login.hide()  # Ocultar la ventana de inicio de sesión
		mi_app = MiApp()  # Crear una instancia de la ventana del menú
		mi_app.show()  # Mostrar la ventana del menú


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	# BEGIN: ed8c6549bwf9
	login = Login()
	# END: ed8c6549bwf9


    # Conectar la señal inicio_sesion_exitoso de la ventana de inicio de sesión
    # para crear una instancia de MiApp después del inicio de sesión exitoso
	def abrir_mi_app():
        nonlocal mi_app  # Utilizamos nonlocal para modificar la variable mi_app fuera de esta función
        mi_app = MiApp()  # Crear una instancia de MiApp
        mi_app.show()  # Mostrar la ventana de MiApp

    login.inicio_sesion_exitoso.connect(abrir_mi_app)

    sys.exit(app.exec_())