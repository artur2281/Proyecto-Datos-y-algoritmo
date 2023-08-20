class Persona:
    def __init__(self, nombre, codigo, edad, correo, numero, genero, fecha_nacimiento):
        self.nombre = nombre
        self.codigo = codigo
        self.edad = edad
        self.correo = correo
        self.numero = numero
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento

class RegistroPersona:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)
        print("Persona agregada exitosamente.")

    def eliminar_persona(self, codigo):
        personas_filtradas = [persona for persona in self.personas if persona.codigo != codigo]
        if len(personas_filtradas) < len(self.personas):
            self.personas = personas_filtradas
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

def main():
    registro = RegistroPersona()

    while True:
        print("\nMenú:")
        print("1. Agregar persona")
        print("2. Eliminar persona")
        print("3. Mostrar personas")
        print("4. Buscar persona")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Solicitar datos al usuario
            nombre = input("Nombre y apellido: ")
            edad = input("Edad: ")
            codigo = input("Codigo: ")
            # Validación del correo electrónico
            while True:
                correo = input("Correo electrónico: ")
                if correo.endswith("@gmail.com"):
                    break
                else:
                    print("Correo incorrecto")
            # Validación del número de celular
            while True:
                numero = input("Número de teléfono: ")
                if len(numero) == 9 and numero.isdigit():
                    break
            else:
                    print("Numero incorrecto")
            genero = input("Genero(F/M): ")
            fecha_nacimiento = input("Fecha de nacimiento(dd/mm/aaaa): ")

            # Crear objeto Empleado
            persona = Persona(nombre, codigo, edad, correo, numero, genero, fecha_nacimiento)

            # Crear objeto RegistroEmpleados
            registro = RegistroPersona()

            # Agregar empleado al registro
            registro.agregar_persona(persona)

        elif opcion == "2":
            codigo = input("Ingrese el codigo de la persona a eliminar: ")
            registro.eliminar_persona(codigo)

        elif opcion == "3":
            registro.mostrar_personas()

        elif opcion == "4":
            codigo = input("Ingrese el codigo de la persona a buscar: ")
            registro.buscar_persona(codigo)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()