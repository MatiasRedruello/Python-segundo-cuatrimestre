from Funciones_base import (imprimir_dato,es_genero,obtener_nombre,calcular_max_min_dato_genero,obtener_nombre_y_dato,
                            calcular_cantidad_tipo,imprimir_cantidad_heroes_tipo,calcular_promedio_genero,obtener_lista_de_tipos,obtener_heroes_por_tipo,
                            imprimir_heroes_por_tipo,lista_personajes_normalizada,validar_entero)

"1.2)"
def stark_imprimir_heroe_genero(lista_heroes:list[dict],genero:str)->None:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Genero -> Es un str del tipo M,F,NB.
    Funcion: Imprimero por pantalla el nombre del heroe.
    Retorna: None
    """    
    for heroe in lista_heroes:
        genero_heroe = es_genero(heroe,genero)
        if genero_heroe:
            nombre_heroe = obtener_nombre(heroe)
            imprimir_dato(nombre_heroe)


"2.4)"
def stark_calcular_imprimir_heroe_genero(lista_heroes:list[dict],caracteristica_deseada:str,genero:str,max_min:str)->None:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Caracteristica deseada-> Es un string que contiene una clave del diccionario..
               Genero -> Es un str del tipo M,F,NB.
               Max y min -> Es un string del tipo maximo o minimo
    Funcion: Busca,calcula e imprime el Heroe con el valor mas grande o chico de una determinada caracteristica y lo mutra por pantalla.
    Retorna: None
    """    
    if not lista_heroes:
        return -1
    else:
        respuesta = calcular_max_min_dato_genero(lista_heroes,caracteristica_deseada,genero,max_min)
        nombre_valor = obtener_nombre_y_dato(respuesta,caracteristica_deseada)
        imprimir_dato(nombre_valor)

"3.4)"
def stark_calcular_imprimir_promedio_altura_genero(lista_heroes:list[dict],calcular_dato:str,genero:str)->str:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Calcular dato -> Es un string que contiene una clave del diccionario..
               Genero -> Es un str del tipo M,F,NB.
    Funcion: Calcula y muestra el valor promedio de una determinada caracteristica y arma un mensaje
    Retorna: Un String
    """    
    if not lista_heroes:
        mensaje = "Error lista vacia"    
    else:
        resultado = calcular_promedio_genero(lista_heroes,calcular_dato,genero)
        mensaje = f"{calcular_dato} promedio genero {genero}: {resultado}"
    return mensaje   

"4.3)"
def stark_calcular_cantidad_por_tipo(lista_heroes:list[dict],caracteristica_deseada:str)->None:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Caracteristica deseada -> Es un string que contiene una clave del diccionario..
    Funcion: Calcula  e imprime por pantalla la cantida de heroes que contiene una caracteristica en comun
    Retorna: None
    """    
    caracteristica_almacenada = calcular_cantidad_tipo(lista_heroes,caracteristica_deseada)
    imprimir_cantidad_heroes_tipo(caracteristica_almacenada,caracteristica_deseada) 

"5.5)"
def stark_listar_heroes_por_dato(lista_heroes:list[dict],caracteristica_deseada:str)->None:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Caracteristica deseada -> Es un string que contiene una clave del diccionario..
    Funcion: Reutiliza las funciones obtener_lista_de_tipos,obtener_heroes_por_tipo y imprimir_heroes_por_tipo y muestra
    Retorna: None
    """    
    lista_de_tipos = obtener_lista_de_tipos(lista_heroes,caracteristica_deseada)
    diccionarios_heroes_por_tipo = obtener_heroes_por_tipo(lista_heroes,lista_de_tipos,caracteristica_deseada)
    imprimir_heroes_por_tipo(diccionarios_heroes_por_tipo,caracteristica_deseada)


