import pandas as pd
from persona import Persona

#clase para la base de datos
class BaseDeDatos:
    #funcion para inicializar la base de datos
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    #funcion para guardar los datos en la base de datos
    def guardar_datos(self, datos):
        df = pd.DataFrame(datos)
        df.to_excel(self.nombre_archivo, index=False)
        
    #funcion para obtener los datos de la base de datos
    def obtener_datos(self):
        try:
            df = pd.read_excel(self.nombre_archivo)
            return [Persona(**persona) for persona in df.to_dict('records')]
        except FileNotFoundError:
            return []

    #funcion para buscar personas por nombre
    def buscar_personas_por_nombre(self, nombre):
        personas = self.obtener_datos()
        personas_encontradas = [persona for persona in personas if persona.nombre == nombre]
        if personas_encontradas:
            print(f"Se encontraron {len(personas_encontradas)} personas con el nombre {nombre}:")
            for persona in personas_encontradas:
                print(f"- Codigo: {persona.codigo}, Edad: {persona.edad}")
        else:
            print(f"No se encontraron personas con el nombre {nombre} en la base de datos.")

    #funcion para buscar personas por edad
    def buscar_personas_por_edad(self, edad_minima, edad_maxima):
        personas = self.obtener_datos()
        personas_encontradas = [persona for persona in personas if edad_minima <= persona.edad <= edad_maxima]
        if personas_encontradas:
            print(f"Se encontraron {len(personas_encontradas)} personas con edades entre {edad_minima} y {edad_maxima}:")
            for persona in personas_encontradas:
                print(f"- Nombre: {persona.nombre}, Codigo: {persona.codigo}")
        else:
            print(f"No se encontraron personas con edades entre {edad_minima} y {edad_maxima} en la base de datos.")
    
    #funcion para cerrar el archivo de Excel
    def cerrar(self):
        try:
            with open(self.nombre_archivo, 'r') as f:
                f.close()
        except FileNotFoundError:
            pass
