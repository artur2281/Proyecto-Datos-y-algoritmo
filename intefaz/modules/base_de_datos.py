import openpyxl
from openpyxl import Workbook
from modules.persona import Persona

#from prettytable import PrettyTable

class BaseDeDatos:
    def __init__(self):
        self.archivo = "G:\Proyecto final\Proyecto-Datos-y-algoritmo\intefaz\personas.xlsx"
        self.personas = self.obtener_datos()
        datos = self.obtener_datos()
        if isinstance(datos, list) and all(isinstance(d, dict) for d in datos):
            self.personas = [Persona(**persona) for persona in datos]
        else:
            self.personas = []

    def obtener_datos(self):
        try:
            wb = openpyxl.load_workbook(self.archivo)
            sheet = wb.active
            datos = []
            for row in sheet.iter_rows(values_only=True):
                if row[0] != 'Nombre':
                    datos.append({'nombre': row[0], 'codigo': row[1], 'edad': row[2], 'correo': row[3], 'numero': row[4], 'genero': row[5], 'fecha_nacimiento': row[6]})
            return [Persona(**persona) for persona in datos]
        except FileNotFoundError:
            return []

    def guardar_datos(self):
        wb = Workbook()
        sheet = wb.active
        sheet.append(['Nombre', 'Codigo', 'Edad', 'Correo', 'Número', 'Género', 'Fecha de Nacimiento'])
        for persona in self.personas:
            sheet.append([persona.nombre, persona.codigo, persona.edad, persona.correo, persona.numero, persona.genero, persona.fecha_nacimiento])
        wb.save(self.archivo)

    def agregar_persona(self, persona):
        self.personas.append(persona)
        self.guardar_datos()

    def eliminar_persona(self, codigo):
        personas_filtradas = [persona for persona in self.personas if persona.codigo != codigo]
        if len(personas_filtradas) < len(self.personas):
            self.personas = personas_filtradas
            self.guardar_datos()
            print(f"Persona {codigo} eliminada.")
        else:
            print(f"No se encontró a {codigo} en el registro.")

    def mostrar_personas(self):
        tabless = []
        for persona in self.personas:
            tabless.append([persona.nombre, persona.codigo, persona.edad, persona.correo, persona.numero, persona.genero, persona.fecha_nacimiento])

        tabla = tabless 
        return tabla, len(self.personas)

    def editar_persona(self, codigo, nueva_informacion):
        for persona in self.personas:
            if persona.codigo == codigo:
                persona.nombre = nueva_informacion.get('nombre', persona.nombre)
                persona.edad = nueva_informacion.get('edad', persona.edad)
                persona.correo = nueva_informacion.get('correo', persona.correo)
                persona.numero = nueva_informacion.get('numero', persona.numero)
                persona.genero = nueva_informacion.get('genero', persona.genero)
                persona.fecha_nacimiento = nueva_informacion.get('fecha_nacimiento', persona.fecha_nacimiento)
                self.guardar_datos()
                print(f"Datos de {persona.nombre} actualizados exitosamente.")
                return
        print(f"No se encontró a la persona con código {codigo} en el registro.")

    def buscar_persona_por_codigo(self, codigo):
        personas_encontradas = [persona for persona in self.personas if persona.codigo == codigo]
        if personas_encontradas:
            for persona in personas_encontradas:
                print("Persona encontrada:")
                print(f"Nombre: {persona.nombre}\nCodigo: {persona.codigo}\nEdad: {persona.edad}\nCorreo: {persona.correo}\nNúmero: {persona.numero}\nGénero: {persona.genero}\nFecha de Nacimiento: {persona.fecha_nacimiento}\n")
                persona_encontras = [persona.nombre, persona.codigo,persona.edad,persona.correo, persona.numero,persona.genero, persona.fecha_nacimiento]
                persona_encontrada = persona_encontras
                return persona_encontrada, len(personas_encontradas)
        else:
            print(f"No se encontró a {codigo} en el registro.")

    def extraer_emails(self):
        emails_receptores = [persona.correo for persona in self.personas]
        return emails_receptores