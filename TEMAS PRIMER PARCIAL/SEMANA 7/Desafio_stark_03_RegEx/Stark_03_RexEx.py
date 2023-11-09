from Data_stark_copy import lista_personajes
import re
"""
Crear una funcion "normalizar_datos"
-Usar RegEx.
-Armar patrones de busqueda
-Analizar Key x Key
"""

def normalizar_datos(lista_personajes:list[dict])->list[dict]:
    patron_flotante = "^[0-9]*[\.][0-9]*$"
    patron_entero = "^[0-9]+$"
    for personajes in lista_personajes:
        for clave in personajes.keys():
            if re.match(patron_flotante,personajes[clave]):
                personajes.update({clave:float(personajes[clave])})
            elif re.match(patron_entero,personajes[clave]):
                personajes.update({clave:int(personajes[clave])}) 
    return lista_personajes          

         
lista_personajes_normalizada = normalizar_datos(lista_personajes)

