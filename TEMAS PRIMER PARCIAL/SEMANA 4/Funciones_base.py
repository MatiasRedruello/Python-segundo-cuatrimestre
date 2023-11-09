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

"1.1)"               
def obtener_nombre(heroe:dict)->str:
    """ 
    Variables: Recibe un diccionario
    Funcion: Arma un mensajae con el valorq ue esta en la key nombre
    Retorna: Mensaje
    """    
    return "Nombre: {0}".format(heroe["nombre"])

"1.2)"
def imprimir_dato(dato_recibido:str)->None:
    """ 
    Variables: Recibe un dato de tipo str
    Funcion: Muestra el dato por consola
    Retorna: None
    """    
    print(dato_recibido)


"2.0 modificado)"
def obtener_nombre_y_dato(heroe:dict,key:str,identidad:str = "nombre"):
    """ 
    Variables: Heroe -> Diccionario
               Key -> Pertenece al diccionario
               Identidad -> Variable con un valor poder defecto, tambien es una key del diccionario           
    Funcion: Arma un mensaje con un formato especifico ej:Nombre: Venom | fuerza: 500
    Retorna: Mensaje
    """    
    return "{3}: {0} | {1}: {2}".format(heroe[identidad].capitalize(),key.capitalize(),heroe[key],identidad.capitalize())

"4.1)"
def calcular_max(lista:list[dict],key:str)->dict:
    """ 
    Variables: Lista -> Contine una lista de diccionarios
               Key -> Pertenece al diccionario
    Funcion: Busca el maximo de una caracteristica dada entre todos los diccionarios y guarda su indice
    Retorna: El diccionario del personaje con la mayor caracteristica
    """    
    for indice in range(len(lista)):
        if indice == 0 or lista[indice_guardado][key] < lista[indice][key]:           
            indice_guardado = indice
    return lista[indice_guardado]

"4.2)"
def calcular_min(lista:list[dict],key:str)->dict:
    """ 
    Variables: Lista -> Contine una lista de diccionarios
               Key -> Pertenece al diccionario
    Funcion: Busca el minimo de una caracteristica dada  entre todos los diccionarios y guarda su indice
    Retorna: El diccionario del personaje con la menor caracteristica
    """     
    for indice in range(len(lista)):
        if indice == 0 or lista[indice_guardado][key] > lista[indice][key]:           
            indice_guardado = indice
    return lista[indice_guardado]

"4.3)"
def calcular_max_min_dato(lista:list[dict],key:str,max_o_min:str)->dict:
    """ 
    Variables: Lista -> Contine una lista de diccionarios
               Key -> Pertenece al diccionario
               max_o_min -> Determina si busca la maxima caracteristica o la minima
    Funcion: Busca el maximo de una caracteristica dada y guarda su indice
    Retorna: El diccionario que le pertenece al personaje con la caracteristica deseada
    """ 
    if max_o_min.lower() == "maximo":           
        resultado = calcular_max(lista,key)
    elif max_o_min.lower() == "minimo":
            resultado = calcular_min(lista,key)
    return  resultado

"5.1)"
def sumar_dato_heroe(lista:list[dict],key:str)->int: 
    """ 
    Variables: Lista -> Contine una lista de diccionarios
               Key -> Pertenece al diccionario
    Funcion: acumula la caracteristica deseada de todos los diccionarios
    Retorna: El valor numerico de esa suma
    """          
    acumulador = 0   
    if len(lista) == 0:
        return -1
    for personajes in lista_personajes:
        if len(personajes) != 0 and isinstance(personajes,dict):
            acumulador += personajes[key]

    return acumulador

"5.2)"
def dividir(dividendo:int,divisor:int)->int:
    """ 
    Variables: dividendo -> Numero el cual se va a dividir
               divisor -> Numero que divide al dividendo
    Funcion: Se ingresan dos numeros y se utilizar para realizar un division 
    Retorna: El resultado numerico de esa division
    """     
    if divisor == 0:
        resultado = 0
    else:
        resultado = dividendo/divisor
    
    return resultado

"5.3)"
def calcular_promedio(lista:list[dict],key:str):
    """ 
    Variables: Lista -> Contine una lista de diccionarios
               Key -> Pertenece al diccionario
    Funcion: Calcula un promedio
    Retorna: El resultado numerico del promedio
    """     
    promedio = dividir(sumar_dato_heroe(lista,key),len(lista))
    return promedio
"6.2)"
def validar_entero(caracteres:str)->bool:
    """ 
    Variables: Caracteres -> Contine un str
    Funcion: Valida que el valor ingresado efectivamente se del tipo str
    Retorna: Devuelve true si  se cumple o false en caso contrario
    """     
    respuesta = lambda x: True if isinstance(x,str) else False
    return respuesta(caracteres)

lista_personajes_actualizada = stark_normalizar_datos(lista_personajes)