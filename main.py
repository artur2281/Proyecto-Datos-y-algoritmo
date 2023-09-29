import sys
sys.path.append('.\src\modules')
from registro_persona import RegistroPersona
from persona import Persona
from base_de_datos import BaseDeDatos
from enviarCorreo import EnviadorDeCorreos
def main():
    registro = RegistroPersona()
    enviador_de_correos = EnviadorDeCorreos('trabajosgrupalesdelcole@gmail.com', 'dysa uxym osmb wuci')

    # Menu principal
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
            edad = int(input("Edad: "))
            codigo = input("Codigo: ")
            numero = input("Número de teléfono: ")
            genero = input("Genero(F/M): ")
            fecha_nacimiento = input("Fecha de nacimiento(dd/mm/aaaa): ")
            
            while True:
                correo = input("Correo electrónico: ")

                # Verificar correo electrónico
                if enviador_de_correos.verificar_correo(correo):
                    print("Correo verificado exitosamente.")
                    
                    # Crear objeto Persona
                    persona = Persona(nombre, codigo, edad, numero, genero, fecha_nacimiento, correo)

                    # Agregar persona al registro
                    registro.agregar_persona(persona)

                    # Enviar correo electrónico a la persona recién registrada
                    enviador_de_correos.enviar_correo(correo, "Registro exitoso", "Has sido registrado exitosamente.")
                    break
                else:
                    print(f"La verificación del correo {correo} ha fallado. Por favor, intenta ingresar un correo valido de nuevo.")
                      
                    

        elif opcion == "2":
            codigo = input("Ingrese el codigo de la persona a eliminar: ")
            registro.eliminar_persona(codigo)

        elif opcion == "3":
            registro.mostrar_personas()

        elif opcion == "4":
            codigo = input("Ingrese el codigo de la persona a buscar: ")
            registro.buscar_persona_por_codigo(codigo)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()