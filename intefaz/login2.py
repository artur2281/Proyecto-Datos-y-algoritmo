import sys
from PyQt5.QtWidgets import QWidget
from menu import *
from PyQt5.QtCore import QUrl, QPropertyAnimation, QEasingCurve,pyqtSignal
from PyQt5 import QtGui 
from login import *
from PyQt5.QtGui import QDesktopServices
from modules.registro_persona import RegistroPersona
from modules.persona import Persona
## librerias para las tablas
from PyQt5 import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem,QTableWidget
from modules.enviarCorreo import EnviadorDeCorreos


class Login(QtWidgets.QMainWindow):
	# Definir una señal personalizada para inicio de sesión exitoso
	inicio_sesion_exitoso = pyqtSignal()

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
		self.login= self.ui_login.pushButton.clicked.connect(self.gui_login)

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
			print("Credenciales correctas")
			self.hide()
			mi_app = MiApp()
			mi_app.show()
			
			return  True
		else:
			print("Credenciales incorrectas")
			
        
		return False

class MiApp(QtWidgets.QMainWindow):
	registro = RegistroPersona()
	model = QStandardItemModel()
	envi = EnviadorDeCorreos('trabajosgrupalesdelcole@gmail.com', 'dysa uxym osmb wuci')

	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow() # intanciamos las clases
		
		# Crear un modelo de datos
		self.model.setHorizontalHeaderLabels(["NOMBRE", "EDAD", "CODIGO", "CORREO", "TELEFONO", "GENERO", "NACIMIENTO"])
		#configurar el nodelo dde datos para la tabla
		
	
		
		self.ui.setupUi(self)
		

		
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
		self.ui.boton_volver.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1registrar))
		#aceder a los botones 
		self.ui.pushButton_6registrar.clicked.connect(self.registrar_persona)
		self.ui.pushButton_buscareliminar.clicked.connect(self.mostrar_tabla_eliminarPersona)
		self.ui.pushButton_botonelimnar.clicked.connect(self.eliminar_persona)
		self.ui.pushButton_9botonbuscar.clicked.connect(self.mostrarTabla_buscar_persona)
		self.ui.bt_REFRESCAR.clicked.connect(self.mostrarTabla_base_datos)
		self.ui.pushButton_8actualizar.clicked.connect(self.actualizar_informacin)
		
		#control barra de titulos
		self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
		self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
		self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
		self.ui.pushButton.clicked.connect(lambda: self.close())

		self.ui.bt_restaurar.hide()

		#menu lateral
		self.ui.bt_menu.clicked.connect(self.mover_menu)



	##--------------------FUNCIONES PARA LOS BOTONES DENTRO -------------------------------------------------------
	def registrar_persona(self):
		
		if True:
			nombre = self.ui.lineEdit1nombre.text()
			edad = self.ui.lineEdit_2edad.text()
			codigo = self.ui.lineEdit_3codigo.text()
			telefono = self.ui.lineEdit_4correo.text()
			correo = self.ui.lineEdit_5telefono.text()
			genero = self.ui.lineEdit_6genero.text()
			nacimiento = self.ui.lineEdit_7nacimiento.text()
			self.ui.stackedWidget.setCurrentWidget(self.ui.verificacion_correo)
			while True:
				codigo_verificacion = self.ui.codigo_intro.text()
				
				self.envi.verificar_correo(correo)
				if self.envi.generar_codigo_verificacion() == codigo_verificacion:
					self.ui.codigo_verificacion.setText("Correo verificado")
					persona = Persona(nombre, codigo, edad, correo, telefono, genero, nacimiento)
					self.registro.agregar_persona(persona)
					break
		else :
			print("no se pudo registrar")

			
		
	def buscar_eliminar(self):
		codigo = self.ui.lineEdit_17ingresarcodigoeliminar.text()
		self.mostrar_tablas(codigo)

	def actualizar_informacin(self):
		codigo = self.ui.lineEdit_9codigoactualizar.text()
		nombre = self.ui.lineEdit_1nombreact.text()
		edad = self.ui.lineEdit_2edadactualizar.text()
		correo = self.ui.lineEdit_4correoactualizar.text()
		telefono = self.ui.lineEdit_5telefonoactualizar.text()
		genero = self.ui.lineEdit_6generoactualizar.text()
		nacimiento = self.ui.lineEdit_7nacimientoactualizar.text()
		nueva_informacion = {'nombre': nombre, 'edad': edad, 'correo': correo, 'numero': telefono, 'genero': genero, 'fecha_nacimiento': nacimiento}
		self.registro.editar_persona(codigo, nueva_informacion)
		self.ui.label_20.setText("Persona editada exitosamente")
	def eliminar_persona(self):
		codigo = self.ui.lineEdit_17ingresarcodigoeliminar.text()
		self.registro.eliminar_persona(codigo)
		self.ui.label_25.setText("Persona eliminada exitosamente")
	def mostrarTabla_buscar_persona(self):
		codigo = self.ui.lineEdit_16ingresarcodigobuscar.text()
		per_encon,num_personasEncontradas = self.registro.buscar_persona_por_codigo(codigo)

		# Obtener el número de filas de la persona encontrada
		i = len(per_encon)
		print("i es igual a:")
		print(i)
		self.ui.tablebuscarpersona.setRowCount(num_personasEncontradas)

		
		if per_encon is not None:
			# Limpiamos cualquier contenido previo en la tabla
			self.ui.tablebuscarpersona.clearContents()
			print(f"Nombre de la persona encontrada: {per_encon[0]}")
			

			tablerow = 0
			
			# Mostramos los datos de la persona encontrada en la tabla
			for row in per_encon:
				self.ui.tablebuscarpersona.setItem(tablerow, 0, QTableWidgetItem(per_encon[0]))
				self.ui.tablebuscarpersona.setItem(tablerow, 1, QTableWidgetItem(str(per_encon[2])))
				self.ui.tablebuscarpersona.setItem(tablerow, 2, QTableWidgetItem(per_encon[1]))
				self.ui.tablebuscarpersona.setItem(tablerow, 3, QTableWidgetItem(per_encon[3]))
				self.ui.tablebuscarpersona.setItem(tablerow, 4, QTableWidgetItem(per_encon[4]))
				self.ui.tablebuscarpersona.setItem(tablerow, 5, QTableWidgetItem(per_encon[5]))
				self.ui.tablebuscarpersona.setItem(tablerow, 6, QTableWidgetItem(per_encon[6]))

				tablerow += 1
		else:
			print(f"No se encontró a {codigo} en el registro.")

	def mostrarTabla_base_datos(self):
		table, num_personas = self.registro.mostrar_personas()
		#establecemos el numero de filas
		self.ui.tableBASEDEDATOS.setRowCount(num_personas)
		#Iteramos sobre filas y columnas 
		for row_index, persona_data in enumerate(table):
			for col_index, data in enumerate(persona_data):
				#creamos un objeto y lo configuramos para que imprima
				item = QTableWidgetItem(str(data))
				# Establecemos el elemento en la celda de la tabla.

				self.ui.tableBASEDEDATOS.setItem(row_index, col_index, item)




	def mostrar_tabla_eliminarPersona(self):
		codigo = self.ui.lineEdit_17ingresarcodigoeliminar.text()
		per_encon,num_personasEncontradas = self.registro.buscar_persona_por_codigo(codigo)

		# Obtener el número de filas de la persona encontrada
		i = len(per_encon)
		print("i es igual a:")
		print(i)
		self.ui.tableelimnarpersona.setRowCount(num_personasEncontradas)

		if per_encon is not None:
			# Limpiamos cualquier contenido previo en la tabla
			self.ui.tableelimnarpersona.clearContents()
			print(f"Nombre de la persona encontrada: {per_encon[0]}")
			

			tablerow = 0
			
			# Mostramos los datos de la persona encontrada en la tabla
			for row in per_encon:
				self.ui.tableelimnarpersona.setItem(tablerow, 0, QTableWidgetItem(per_encon[0]))
				self.ui.tableelimnarpersona.setItem(tablerow, 1, QTableWidgetItem(str(per_encon[2])))
				self.ui.tableelimnarpersona.setItem(tablerow, 2, QTableWidgetItem(per_encon[1]))
				self.ui.tableelimnarpersona.setItem(tablerow, 3, QTableWidgetItem(per_encon[3]))
				self.ui.tableelimnarpersona.setItem(tablerow, 4, QTableWidgetItem(per_encon[4]))
				self.ui.tableelimnarpersona.setItem(tablerow, 5, QTableWidgetItem(per_encon[5]))
				self.ui.tableelimnarpersona.setItem(tablerow, 6, QTableWidgetItem(per_encon[6]))

				tablerow += 1
		else:
			print(f"No se encontró a {codigo} en el registro.")

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





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Crear una instancia de la ventana de inicio de sesión
    login = Login()
    login.show()
    mi_app = MiApp()
    

    """ # Iniciar el bucle de eventos de la aplicación
    while login.login:
        # Procesar eventos
        app.processEvents()

        # Verificar si el usuario ha iniciado sesión
        
        if login.gui_login() is True:
            # Ocultar la ventana de inicio de sesión
            login.hide()
            # Mostrar la ventana de la aplicación principal
            mi_app.show()
            break

        # Comprobar si el usuario ha cerrado la aplicación
         """

    sys.exit(app.exec_())
