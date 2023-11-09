from Data_stark_copy import lista_personajes

def stark_normalizar_datos(lista_personajes:list[dict])->list:
    """ 
    Variables: Recibe una lista de diccionarios
    Funcion: Recorro la lista y actualizo los str que contengan un dato  numerico a la clase correspondiente como puede ser un entero o un numero flotante
    Retorna: La lista casteada
    """      
    datos_normalizados = False

    if len(lista_personajes) == 0:
        print("Error: Lista de héroes vacía")

    for personaje in lista_personajes:
        for llave,valor in personaje.items():
            if llave == "altura" and not isinstance(valor,float):
                personaje.update({"altura":float(valor)})  
            elif llave == "peso" and not isinstance(valor,float):
                personaje.update({"peso":float(valor)})                   
            elif llave == "fuerza" and not isinstance(valor,int):
                personaje.update({"fuerza":int(valor)}) 
            datos_normalizados = True

    if datos_normalizados:
        print("Los datos fueron normalizados")
    return lista_personajes 
lista_personajes_normalizada = stark_normalizar_datos(lista_personajes)

"FUNCIONES REICLADAS:"
def imprimir_dato(dato_recibido:str)->None:
    """ 
    Variables: Recibe un dato de tipo str
    Funcion: Muestra el dato por consola
    Retorna: None
    """    
    print(dato_recibido)
               
def obtener_nombre(heroe:dict)->str:
    """ 
    Variables: Recibe un diccionario
    Funcion: Arma un mensajae con el valorq ue esta en la key nombre
    Retorna: Mensaje
    """    
    return "Nombre: {0}".format(heroe["nombre"]) 

def obtener_nombre_y_dato(heroe:dict,key:str,identidad:str = "nombre"):
    """ 
    Variables: Heroe -> Diccionario.
               Key -> Pertenece al diccionario.
               Identidad -> Variable con un valor por defecto, tambien es una key del diccionario.           
    Funcion: Arma un mensaje con un formato especifico ej:Nombre: Venom | fuerza: 500
    Retorna: Mensaje
    """  
    print(heroe)  
    return "{3}: {0} | {1}: {2}".format(heroe[identidad].capitalize(),key.capitalize(),heroe[key],identidad.capitalize()) 

"FUNCIONES LAMDBA:"
validar_entero = lambda x: True if isinstance(x,str) else False
divicion = lambda x,y: x/y
suma_heroes_por_genero = lambda listado_heroes,machear_genero: sum(1 for heroe in listado_heroes if heroe["genero"] == machear_genero.upper()) 

"FUNCIONES EJERCICIOS:"
"1.1)"
def es_genero(personaje:dict,genero:str)->bool:
    """ 
    Variables: Personaje-> Recibe un diccionario.
               Genero-> str del tipo F,M,NB.
    Funcion: la variable genero será usara para evaluar si el héroe coincide con el género buscado 
    Retorna: bool
    """     
    if genero.upper() == personaje["genero"]:
        respuesta = True
    else:
        respuesta = False
    return respuesta
"2.1)"
def calcular_min_genero(lista_heroes:list[dict],caracteristica_minima:str,genero:str)->dict:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Caracteristica minima-> Es un string que contiene una key del diccionario.
               Genero -> Es un str del tipo M,F,NB.
    Funcion: Busca el valor minimo correspondiente a una clave denro del diccionario correspondiente a un heroe y guarda el dato
    Retorna: Diccionario
    """    
    flag = True
    for heroe in lista_heroes:
        if heroe["genero"] == genero.upper():
            if flag or heroe_minimo.get(caracteristica_minima) > heroe.get(caracteristica_minima,100):
                heroe_minimo = heroe
                flag = False
    return heroe_minimo
"2.2)"
def calcular_max_genero(lista_heroes:list[dict],caracteristica_maxima:str,genero:str)->dict:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Caracteristica maxima-> Es un string que contiene una key del diccionario.
               Genero -> Es un str del tipo M,F,NB.
    Funcion: Busca el valor maximo correspondiente a una clave denro del diccionario correspondiente a un heroe y guarda el dato
    Retorna: El diccionario que le corresponde a un heroe.
    """     
    flag = True
    for heroe in lista_heroes:
        if heroe["genero"] == genero.upper():
            if flag or heroe_maximo.get(caracteristica_maxima) < heroe.get(caracteristica_maxima,100):
                heroe_maximo = heroe
                flag = False
    return heroe_maximo
    
"2.3)"
def calcular_max_min_dato_genero(lista_heroes:list[dict],caracteristica_deseada:str,genero:str,max_min:str)->dict:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Caracteristica deseada -> Es un string que contiene una key del diccionario..
               Genero -> Es un str del tipo M,F,NB.
               Max y min -> Es un str del tipo maximo o minimo.
    Funcion: Trae el diccionario del hero cuya caracteristica es la maxima o la minima y segun si es femenino,masculino o no binario
    Retorna: Diccionario de un heroe
    """
    heroe = {}    
    if max_min.lower() == "maximo":
        heroe = calcular_max_genero(lista_heroes,caracteristica_deseada,genero)
    elif max_min.lower() == "minimo":
        heroe = calcular_min_genero(lista_heroes,caracteristica_deseada,genero)

    return heroe

"3.1)"
def sumar_dato_heroe_genero(lista_heroes:list[dict],calcular_dato:str,genero:str)->float:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Calcular dato -> Es un string que contiene una clave del diccionario..
               Genero -> Es un str del tipo M,F,NB.
    Funcion: Suma el valor numerico que se encuentra dentro de la clave de todos los heroes
    Retorna: Un valor numerico
    """    
    resultado_suma = 0
    for heroe in lista_heroes:
        if isinstance(heroe,dict) and heroe and heroe.get("genero","no tiene genero") == genero.upper():
           resultado_suma += heroe[calcular_dato]
    return resultado_suma

"3.2)"
def cantidad_heroes_genero(lista_heroes:list[dict],genero:str)->float:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Genero -> Es un str del tipo M,F,NB.
    Funcion: Suma la cantidad de heroes por genero
    Retorna: Retorna un valor numerico
    """    
    return suma_heroes_por_genero(lista_heroes,genero)

"3.3)"
def calcular_promedio_genero(lista_heroes:list[dict],calcular_dato:str,genero:str)->float:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Calcular dato -> Es un string que contiene una clave del diccionario..
               Genero -> Es un str del tipo M,F,NB.
    Funcion: Divide la suma total de una clave determinada de todos los heroes y la divide por la cantidad todal de los mismos segun el genero
    Retorna: Un valor numerico
    """   
    divisor = sumar_dato_heroe_genero(lista_heroes,calcular_dato,genero)
    dividendo = cantidad_heroes_genero(lista_heroes,genero)
    promedio = divicion(divisor,dividendo)
    return promedio

"4.1)"
def calcular_cantidad_tipo(lista_heroes:list[dict],caracteristica_deseada:str)->dict:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Caracteristica deseadas -> Es un string que contiene una clave del diccionario..
    Funcion: Guarda en un diccionario la cantidad de heroes que contienen la caracteristica deseada.
    Retorna: Diccionario de un heroe
    """
    caracteristicas = {}
    if not lista_heroes:
        print(-1)
    for heroe in lista_heroes:
        if heroe.get(caracteristica_deseada,"caracteristica inexistente") not in caracteristicas:
            if heroe.get(caracteristica_deseada,"caracteristica inexistente") == "":
                caracteristicas["no tiene"] = 1
            else:
                caracteristicas[heroe.get(caracteristica_deseada,"caracteristica inexistente")] = 1
        else:
            caracteristicas[heroe.get(caracteristica_deseada,"caracteristica inexistente")] += 1

    return caracteristicas

"4.2)"
def imprimir_cantidad_heroes_tipo(caracteristica_almacenada:dict,caracteristica_deseada:str)->None:
    """ 
    Variables: Caracteristica almacenada-> Un diccionario con la cantidad de heroes con caracteristicas en comun
               Caracteristica deseada-> Es un string que contiene una clave del diccionario que se busca.
    Funcion: Arme un string y lo mustra por pantalla
    Retorna: None
    """    
    for clave,valor in caracteristica_almacenada.items():
        imprimir_dato(f"Característica: {caracteristica_deseada} {clave}: - Cantidad de héroes: {valor}")
"5.1)"
def obtener_lista_de_tipos(lista_heroes:list[dict],caracteristica_deseada)->list:
    """ 
    Variables: Lista de heroes-> una lista con diccionarios.
               Caracteristica deseada -> Es un string que contiene una clave del diccionario..
    Funcion: Crea una lista que contiene las distintas caracteristicas de un mismo tipo y luego arma un segundo pero si nlas palabras repetidas.
    Retorna: Una lista con los distintos tipos de una misma caracteristica
    """    
    caracteristicas_sin_duplicados = []
    caracteristicas = [] #[heroe.get(caracteristica_deseada,'N/A') for heroe in lista_heroes]
    for heroe in lista_heroes:
        if heroe[caracteristica_deseada] == "":
            caracteristicas.append("no existe")
        else:
            caracteristicas.append(heroe[caracteristica_deseada])
    for valor in caracteristicas:
        if valor not in caracteristicas_sin_duplicados:
            caracteristicas_sin_duplicados.append(valor)

        
    return caracteristicas_sin_duplicados

"5.2)"
def normalizar_dato(valor:str,valor_por_defecto= "no existe")->str:
    """ 
    Variables: valor-> Es un string
               valor por defecto-> Valor por defecto 
    Funcion: Si se ingresa un valor lo devulve y si no existe de vulve por defecto, no existe
    Retorna: Un string
    """    
    if not valor:
        mensaje = valor_por_defecto
    else:
        mensaje = valor
    return mensaje

"5.3)"
def obtener_heroes_por_tipo(lista_heroes:list[dict],lista_de_tipos:list,caracteristica_deseada:str)->dict:
    """ 
    Variables: Lista de heroes-> Una lista con diccionarios.
               Lista de tipos -> Contiene la variedad de tipos que tiene una caracteristica
               Caracteristica deseada -> Es un string que contiene una clave del diccionario..
    Funcion: Arma un diccionario que sus clave son los tipos y el valor los distintos heroes que cumplan con la caracteristica
    Retorna: Una diccionario
    """    
    heroes_ordenados_por_caracteristicas = {}
    for tipo in lista_de_tipos:
        if tipo not in heroes_ordenados_por_caracteristicas:
            heroes_ordenados_por_caracteristicas[tipo] = []
        for heroe in lista_heroes:
            dato_normalizado = normalizar_dato(heroe.get(caracteristica_deseada,"no existe"))
            if tipo == dato_normalizado:
                heroes_ordenados_por_caracteristicas[tipo].append(heroe["nombre"]) 

              
            
    return heroes_ordenados_por_caracteristicas


"5.4)"
def imprimir_heroes_por_tipo(heroes_ordenados_por_caracteristicas:dict,caracteristica_deseada:str)->None:
    """ 
    Variables: Heroes ordenados por caracterisitcas-> Es un diccionario que contiene los heroes con una caracteristica en comun
               Caracteristica deseada -> Es un string que contiene una clave del diccionario..
    Funcion: Arma un string con un formato tipo "color_ojos Green: Black Widow | Hulk"
    Retorna: None
    """
    for clave,valor in heroes_ordenados_por_caracteristicas.items():
        heroes = " | ".join(valor)
        imprimir_dato(f"{caracteristica_deseada} {clave}: {heroes}")





