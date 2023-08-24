from base_de_datos import BaseDeDatos
from persona import Persona

class RegistroPersona:
    def __init__(self):
        self.bd = BaseDeDatos('personas.xlsx')
        self.personas = [Persona(**persona) for persona in self.bd.obtener_datos()]

    def agregar_persona(self, persona):
        self.personas.append(persona)
        self.bd.guardar_datos([persona.__dict__ for persona in self.personas])
        print("Persona agregada exitosamente.")

    def eliminar_persona(self, codigo):
        personas_filtradas = [persona for persona in self.personas if persona.codigo != codigo]
        if len(personas_filtradas) < len(self.personas):
            self.personas = personas_filtradas
            self.bd.guardar_datos([persona.__dict__ for persona in self.personas])
            print(f"Persona {codigo} eliminada.")
        else:
            print(f"No se encontró a {codigo} en el registro.")

    def mostrar_personas(self):
        for persona in self.personas:
            print(f"Nombre: {persona.nombre}\nCodigo: {persona.codigo}\nEdad: {persona.edad}\nCorreo: {persona.correo}\nNúmero: {persona.numero}\nGénero: {persona.genero}\nFecha de Nacimiento: {persona.fecha_nacimiento}\n")

    def buscar_persona(self, codigo):
        personas_encontradas = [persona for persona in self.personas if persona.codigo == codigo]
        if personas_encontradas:
            for persona in personas_encontradas:
                print("Persona encontrada:")
                print(f"Nombre: {persona.nombre}\nCodigo: {persona.codigo}\nEdad: {persona.edad}\nCorreo: {persona.correo}\nNúmero: {persona.numero}\nGénero: {persona.genero}\nFecha de Nacimiento: {persona.fecha_nacimiento}\n")
        else:
            print(f"No se encontró a {codigo} en el registro.")
