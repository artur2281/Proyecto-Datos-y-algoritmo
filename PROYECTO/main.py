from registro_persona import RegistroPersona
from persona import Persona
import sys

def Agregar_persona(registro):
    nombre = input("Nombre y apellido: ")
    edad = int(input("Edad: "))
    codigo = input("Código: ")
    correo = input("Correo electrónico (sin @gmail.com): ")
    correo = correo + "@gmail.com"
    numero = input("Número de teléfono: ")
    genero = input("Género (F/M): ")
    fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")

    persona = Persona(nombre, codigo, edad, correo, numero, genero, fecha_nacimiento)
    registro.agregar_persona(persona)

def Eliminar_persona(registro):
    codigo = input("Ingrese el codigo de la persona a eliminar: ")
    registro.eliminar_persona(codigo)

def Mostrar_personas(registro):
    registro.mostrar_personas()

def Buscar_persona(registro):
    codigo = input("Ingrese el codigo de la persona a buscar: ")
    registro.buscar_persona(codigo)

def exit_program():
    print("Saliendo del programa...")
    sys.exit(0)

# Diccionario
opciones = {
    "1": Agregar_persona,
    "2": Eliminar_persona,
    "3": Mostrar_personas,
    "4": Buscar_persona,
    "0": exit_program
}

def main():
    registro = RegistroPersona()

    while True:
        print("MENU DE OPCIONES")
        print("1. Agregar persona")
        print("2. Eliminar persona")
        print("3. Mostrar personas")
        print("4. Buscar persona")
        print("0. Salir")

        seleccion = input("Seleccione una opción: ")

        if seleccion in opciones:
            opciones[seleccion](registro)
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

