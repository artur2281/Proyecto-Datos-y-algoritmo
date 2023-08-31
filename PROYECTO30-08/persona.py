#class Persona
class Persona:
    nombre = ""
    codigo = ""
    edad = ""
    correo = ""
    numero = ""
    genero = ""
    fecha_nacimiento = ""
    def __init__(self, nombre, codigo, edad, correo, numero, genero, fecha_nacimiento):
        self.nombre = nombre
        self.codigo = codigo
        self.edad = edad
        self.correo = correo
        self.numero = numero
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_codigo(self):
        return self._codigo

    def set_codigo(self, codigo):
        self._codigo = codigo

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def get_correo(self):
        return self._correo

    def set_correo(self, correo):
        self._correo = correo

    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero

    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        self._genero = genero

    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento
