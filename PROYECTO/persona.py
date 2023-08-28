class Persona:
    nombre= ""
    codigo = 0
    edad = 0
    correo = ""
    numero = 0
    genero = ""
    fecha_nacimiento = ""

    #Constructor
    def __init__(self, nombre, codigo, edad, correo, numero, genero, fecha_nacimiento):
        self.nombre = nombre
        self.codigo = codigo
        self.edad = edad
        self.correo = correo
        self.numero = numero
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_correo(self):
        return self.correo

    def set_correo(self, correo):
        self.correo = correo

    def get_numero(self):
        return self.numero
    
    def set_numero(self, numero):
        self.numero = numero
    
    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento