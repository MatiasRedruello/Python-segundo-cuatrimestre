from Data_stark import lista_personajes
"""
A) Analizar detenidamente el set de datos
B) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
C) Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
D) Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E) Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
F) Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
G) Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
H) Calcular e informar cual es el superhéroe más y menos pesado.
I) Ordenar el código implementando una función para cada uno de los valores informados.
J) Construir un menú que permita elegir qué dato obtener
"""
from Data_stark import lista_personajes
"B)"
def nombre(lista:list[dict],permiso:str)->None:
    """ 
    Variables: Lista: Contiene diccionarios.
                Permiso: Variable de control que evita que el print se muestre constantemente. 
    Funcion: Muestra el nombre de todos los persoanjes
    Retorna: None
    """         
    for personaje in lista: 
        if permiso == "1":# Se puede evitar de otra forma?
            print("Nombre: {0}".format(personaje["nombre"]))


"C)"
def nombre_y_altura (lista:list[dict],permiso:str)->None:
    """ 
    Variables: Lista: Contiene diccionarios.
                Permiso: Variable de control que evita que el print se muestre constantemente. 
    Funcion: Muestra el nombre de todos los persoanjes y la altura
    Retorna: None
    """         
    for personaje in lista: 
        if permiso == "2":
            print("Nombre: {0} y su altura es: {1}".format(personaje["nombre"],personaje["altura"]))
        


"D)"
def calcular_mas_alto(lista:list[dict])->str:
    """ 
    Variables: Lista: Contiene diccionarios. 
    Funcion: Compara alturas para guardar el indice del mal alto
    Retorna: El mas alto
    """         
    for indice in range(len(lista)):
        if indice == 0 or float(lista[el_mas_alto]["altura"]) < float(lista[indice]["altura"]):
            el_mas_alto = indice
    return el_mas_alto

   

"E)"
def calcular_mas_bajo(lista:list[dict])->str:
    """ 
    Variables: Lista: Contiene diccionarios. 
    Funcion: Compara alturas para guardar el indice del mal bajo.
    Retorna: El mas bajo
    """         
    for indice in range(len(lista)):
        if indice == 0 or float(lista[el_mas_bajo]["altura"]) > float(lista[indice]["altura"]):
            el_mas_bajo = indice
    return el_mas_bajo

         

"F)"
def altura_promedio(lista:list[dict])->float:
    """ 
    Variables: Lista: Contiene diccionarios. 
    Funcion: Acumula las alturas y divide por la cantidad de heroes para sacar el promedio de las mismas
    Retorna: El promedio de alturas
    """         
    acumulador = 0
    for personajes in lista:
        acumulador += float(personajes.get("altura"))
    return acumulador/len(lista)

"G)"
def identidad(lista:list[dict],mas_alto:str,mas_bajo:str)->str:
    """ 
    Variables: Lista: Contiene diccionarios.
               Mas_alto: Personaje mas alto.
               Mas_bajo: Personaje mas bajo.
    Funcion: Busca y guarda la identidad del hero mas alto y mas bajo
    Retorna: Las identidades con las corespondientes alturas
    """         
    for personaje in lista:
        if float(personaje["altura"]) == float(mas_alto):
            nombre_mas_alto = personaje["identidad"]
        if float(personaje["altura"]) == float(mas_bajo):
            nombre_mas_bajo = personaje["identidad"]
            
    return "El personaje mas alto es {0} y la altura es {1} \n El personaje menos bajo es {2} y su altura es {3}".format([nombre_mas_alto],
                                                                                                                        mas_alto,
                                                                                                                        [nombre_mas_bajo],
                                                                                                                        mas_bajo)


"G)"
def pesos(lista:list[dict])->str:
    """ 
    Variables: Lista: Contiene diccionarios. 
    Funcion: Compara pesos para guardar el indice del mas pesado y el del menos pesado
    Retorna: El mas pesado y el menos pesado de los heroes
    """         
    for indice in range(len(lista)):
        if indice == 0 or float(lista[el_mas_pesado]["peso"]) < float(lista[indice]["peso"]):
            el_mas_pesado = indice
        if indice == 0 or float(lista[el_menos_pesado]["peso"]) > float(lista[indice]["peso"]):
            el_menos_pesado = indice        
    return "El personaje mas pesado es {0} y el peso es {1} \n El personaje menos pesado es {2} y su peso es {3}".format(lista_personajes[el_mas_pesado]["nombre"],
                                                                                                                        lista_personajes[el_mas_pesado]["peso"],
                                                                                                                        lista_personajes[el_menos_pesado]["nombre"],
                                                                                                                        lista_personajes[el_menos_pesado]["peso"])

