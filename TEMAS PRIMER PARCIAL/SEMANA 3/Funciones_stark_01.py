from Data_stark_copy import lista_personajes
"""
a)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M #listo
b)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F #listo
c)Recorrer la lista y determinar cuál es el superhéroe más alto de género M #listo
d)Recorrer la lista y determinar cuál es el superhéroe más alto de género F #listo
e)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M #listo
f)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F #listo
g)Recorrer la lista y determinar la altura promedio de los  superhéroes de género M #listo
h)Recorrer la lista y determinar la altura promedio de los  superhéroes de género F #listo
i)Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F) #listo
j)Determinar cuántos superhéroes tienen cada tipo de color de ojos.  #listo
k)Determinar cuántos superhéroes tienen cada tipo de color de pelo.#listo
l)Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). #listo
m)Listar todos los superhéroes agrupados por color de ojos.
n)Listar todos los superhéroes agrupados por color de pelo.
o)Listar todos los superhéroes agrupados por tipo de inteligencia
"""

def filtrar_por_caracteristicas(lista_personajes:list[dict],caracteristica:str,clave:str)->list[dict]:
    """ 
    Variables:Lista: contine diccionarios
              Caracteristica: lo que busco para filtrar
              Clave: es una de las claves del diccionario
    Funcion: Creo un nuevo diccionario a partir de comparar  la clave y la caracteristica,luego lo filtro.
    Retorna: Una nueva lista con diccionarios
    """ 
    filtro = list(filter(lambda x:x[clave]== caracteristica,lista_personajes))
    return filtro

def nombre_de_los_personajes(lista_personajes:list[dict],caracteristica:str,clave:str)->None:
    """ 
    Variables:Lista: contine diccionarios
              Caracteristica: lo que busco para filtrar
              Clave: es una de las claves del diccionario
    Funcion: Creo una variable que contiene los nombres de los personajes masculinos y los muestro
    Retorna: None
    """    
    personajes = filtrar_por_caracteristicas(lista_personajes,caracteristica,clave)
    for personaje in personajes:
        print(personaje["nombre"])

def altura_de_los_superheroes(lista_personajes:list[dict],caracteristica:str,clave:str,parametro:str):
    personajes = filtrar_por_caracteristicas(lista_personajes,caracteristica,clave)
    flag_mensaje = False

    for indice in range(len(personajes)):
        if parametro == "alto":
            if indice == 0 or float(personajes[personaje_mas_alto]["altura"]) < float(personajes[indice]["altura"]):
                personaje_mas_alto = indice
                flag_mensaje = True
        elif parametro == "bajo":
            if indice == 0 or float(personajes[personaje_mas_bajo]["altura"]) > float(personajes[indice]["altura"]):
                personaje_mas_bajo = indice        

    if flag_mensaje:
        print("El super heroe mas alto del genero {0} es {1} y mide {2} cm".format(caracteristica,personajes[personaje_mas_alto]["nombre"],personajes[personaje_mas_alto]["altura"]))
    else:
        print("El super heroe mas bajo del genero {0} es {1} y mide {2} cm".format(caracteristica,personajes[personaje_mas_bajo]["nombre"],personajes[personaje_mas_bajo]["altura"]))

def promediar(lista_personajes:list[dict],caracteristica:str,clave:str)->str:
    personajes = filtrar_por_caracteristicas(lista_personajes,caracteristica,clave)
    acumulador = 0
    for personaje in personajes:
        acumulador += float(personaje["altura"])
    promedio = acumulador/ len(personajes)   

    return "La altura promedio de los personajes {0} es: {1} cm".format(caracteristica,promedio)

    
def agrupar_superheroes_por_caracteristicas(lista_personajes,clave):
    diccionario_aux = {}
    for personaje in lista_personajes:
        
        if personaje.get(clave,"no se encontro el valor") not in diccionario_aux:
            if personaje.get(clave,"no se encontro el valor") == "":
                diccionario_aux["no_tiene"] = 1
            else:
                diccionario_aux[personaje.get(clave,"no se encontro el valor")] = 1 
        else:
            diccionario_aux[personaje.get(clave,"no se encontro el valor")] += 1
    return diccionario_aux
    
def nombre_de_los_personajes_por_tipo_de_caracteristica(lista_personajes:list[dict],clave:str):

    diccionario_aux = {}
    
    for personaje in lista_personajes:
        if personaje.get(clave,"no se encontro el valor") not in diccionario_aux:
            if personaje.get(clave,"no se encontro el valor") == "":
                diccionario_aux["no_tiene"] = [personaje["nombre"]]
            else:    
                diccionario_aux[personaje[clave]] = [personaje["nombre"]]  

        else:
            diccionario_aux[personaje[clave]].append(personaje["nombre"])
            
    return diccionario_aux    

print(nombre_de_los_personajes_por_tipo_de_caracteristica(lista_personajes,"color_ojos"))


