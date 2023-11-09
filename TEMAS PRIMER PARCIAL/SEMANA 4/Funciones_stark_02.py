from Funciones_base import (imprimir_dato,obtener_nombre,obtener_nombre_y_dato,calcular_max_min_dato,calcular_promedio,validar_entero,
                            lista_personajes_actualizada)
"""
1)Analizar detenidamente el set de datos
2)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
3)Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
4)Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
5)Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
6)Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
7)Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
8)Calcular e informar cual es el superhéroe más y menos pesado.
9)Ordenar el código implementando una función para cada uno de los valores informados.
10)Construir un menú que permita elegir qué dato obtener

"""
"0)"


"1.3)"
def stark_imprimir_nombres_heroes(lista:list[dict])->None:
    """ 
    Variables: Lista -> Contine una lista de diccionarios
    Funcion: Recorre la lista de dicionarios muestra por consola los diccionaros
    Retorna:None
    """     
    if len(lista) == 0:
        return -1

    for personajes in lista:
        imprimir_dato(obtener_nombre(personajes))

"3)"
def stark_imprimir_nombres_alturas(lista:list[dict],key:str)->None:
    """ 
    Variables: Lista -> Contine una lista de diccionarios
               Key -> Pertenece al diccionario
    Funcion: Recorre la lista de diccionarios y pasa cada diccionarios a otra funcion y mostar por pantalla  el dato deseado
    Retorna: None
    """     
    for personajes in lista:
        imprimir_dato(obtener_nombre_y_dato(personajes,key))

"4.4)"
def stark_calcular_imprimir_heroe(lista:list[dict],key:str,max_o_min:str,identidad:str ="nombre")->int:
    """ 
    Variables: Lista -> Contine una lista de diccionarios
               Key -> Pertenece al diccionario
               Max_o_min -> Determina si busca la maxima caracteristica o la minima
               Identidad -> Variable con un valor poder defecto, tambien es una key del diccionario 
    Funcion: Busca en los dicionarios el heroe con la mayor o menor caracteristica deseada y lo mustra por pantalla.Se le da un formato al mensaje
    Retorna: -1 si la lista esta vaciar
    """     
    if len(lista) == 0:
        return -1
    
    resultado = calcular_max_min_dato(lista,key,max_o_min)
    mensaje_uno   = obtener_nombre_y_dato(resultado,key,identidad)
    mensaje_dos = "El personaje con la {0} {2}: {1}".format(max_o_min.lower().replace("o","a"),mensaje_uno,key)
    print(mensaje_dos)

"5.4)"
def stark_calcular_imprimir_promedio_altura(lista:list[dict],key:str)->int:
    """ 
    Variables: Lista -> Contine una lista de diccionarios
               Key -> Pertenece al diccionario
    Funcion: Calcula el promedio de una caracteristica especifica y la muestra por pantalla
    Retorna: -1 si la lista esta vaciar
    """        
    if len(lista) == 0:
        return -1
    imprimir_dato(calcular_promedio(lista,key))




