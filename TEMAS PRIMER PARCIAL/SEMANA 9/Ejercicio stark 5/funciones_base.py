from funciones_archivos import guardar_archivo,ROOT_DIR,crear_categorias,crear_datos_personajes
import re
def capitalizar_palabras(texto:str)->str:
    """
    Parametros: Texto-> Texto que se quiere capitalizar puede ser una o mas palabras
    Funcion: Capitalizada cada palabra 
    Retorno: Texto capitalizado
    """    
    texto_capitalizado = ""
    lista_palabras = texto.split(" ")
    for palabra in lista_palabras:
        texto_capitalizado = texto_capitalizado + palabra.capitalize()
    return texto_capitalizado

def obtener_nombre_capitalizado(diccionario_heroe:dict)->str:
    """
    Parametros: Diccionario heroe-> Diccionario que contine los datos del heroe
    Funcion: Formatea el nombre del heroe
    Retorno: El nombre del heroe con formato   
    """
    nombre_heroe = capitalizar_palabras(diccionario_heroe.get("nombre",None))
    formato = f"Nombre: {nombre_heroe}"

    return formato

def obtener_nombre_y_dato(diccionario_heroe:dict,clave:str)->str:
    """
    Parametros: Diccionario heroe-> Diccionario que contine los datos del heroe
                Clave-> Clave que corresponde al deto que quiero imprimir
    Funcion: Formatea el nombre del heroe y el dato que se quiere mostrar
    Retorno: El nombre del heroe y el dato con formato     
    """

    obtener_valor = diccionario_heroe.get(clave,None)
    obtener_nombre = obtener_nombre_capitalizado(diccionario_heroe)
    formato = f"{obtener_nombre} | {clave}: {obtener_valor}"
    return formato

def es_genero(diccionario_heroe:dict,genero:str)->bool:
    """
    Parametros: Diccionario heroe-> Diccionario que contine los datos del heroe.
                Genero-> Genero con el cual voy a comparar al heroe, puede ser F,M,NB.
    Funcion: Formatea el nombre del heroe y el dato que se quiere mostrar.
    Retorno: True si el genero coincide y false en caso contrario.
    """
    if diccionario_heroe.get("genero","None") == genero.upper():
        return True
    else:
        return False
    
def stark_guardar_heroe_genero(lista_heroes:list[dict],genero:str)->bool:
    """
    Parametros: lista_heroes-> Contiene la informacion de todos los heroes.
                Genero-> Genero con el cual voy a comparar al heroe, puede ser F,M,NB.
    Funcion: Imprime y guarda aquellos heroes que coincidan con el genero.
    Retorno: True si se guarod el archivo y de lo contrario False.
    """
    ruta_destino = f"{ROOT_DIR}heroes{genero.upper()}.csv"
    texto = ""
    # Armo formato csv segun genero
    for heroe in lista_heroes:
        if es_genero(heroe,genero):
            print(heroe)
            flag = True
            for valor in heroe.values():
                if flag:
                    texto += f"{valor}"
                    flag = False
                else:
                    texto += f",{valor}" 
            texto += "\n"
    # Guardo archivo Y retorno  
    crear = guardar_archivo(ruta_destino,texto)
    if crear:
        return True
    else:
        return False

def calcular_min_genero(lista_heroes:list[dict],clave:str,genero:str)->dict:
    """ 
    parametros: lista_heroes -> Contine la informacion de los heroes
                Clave -> Pertenece al diccionario
                Genero-> Genero con el cual voy a comparar al heroe, puede ser F,M,NB.
    Funcion: Busca el minimo de una caracteristica dada entre todos los diccionarios y guarda el heroe
    Retorna: El diccionario del personaje con la mayor caracteristica
    """   
    flag = True
    for heroe in lista_heroes:
        if heroe.get("genero",None) == genero.upper():
            if flag or float(heroe.get(clave)) < valor_guardado:
                valor_guardado = float(heroe.get(clave))
                heroe_menor_caraceristica_genero = heroe
                flag = False
    return heroe_menor_caraceristica_genero

def calcular_max_genero(lista_heroes:list[dict],clave:str,genero:str)->dict:
    """ 
    parametros: lista_heroes -> Contine la informacion de los heroes
                Clave -> Pertenece al diccionario,es la caracteristica que se busca
                Genero-> Genero con el cual voy a comparar al heroe, puede ser F,M,NB.
    Funcion: Busca el maximo de una caracteristica dada entre todos los diccionarios y guarda el heroe
    Retorna: El diccionario del personaje con la mayor caracteristica
    """   
    flag = True
    for heroe in lista_heroes:
        if heroe.get("genero",None) == genero.upper():
            if flag or float(heroe.get(clave)) > valor_guardado:
                valor_guardado = float(heroe.get(clave))
                heroe_mayor_caraceristica_genero = heroe
                flag = False
    return heroe_mayor_caraceristica_genero

def calcular_max_min_dato_genero(lista_heroes:list[dict],clave:str,max_o_min:str,genero:str)->dict:
    """ 
    Parametros: Lista_heroes -> Contine la informacion de los heroes
                Clave -> Pertenece al diccionario,es la caracteristica que se busca
                Max_o_min -> Determina si busca la maxima caracteristica o la minima
                Genero-> Genero con el cual voy a comparar al heroe, puede ser F,M,NB.
    Funcion: Busca el maximo de una caracteristica dada y guarda su diccionario
    Retorna: El diccionario que le pertenece al personaje con la caracteristica deseada
    """ 
    if max_o_min.lower() == "maximo":           
        resultado = calcular_max_genero(lista_heroes,clave,genero.upper())
    elif max_o_min.lower() == "minimo":
            resultado = calcular_min_genero(lista_heroes,clave,genero.upper())
    return  resultado

def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes:list[dict],clave:str,max_o_min:str,genero:str,)->int:
    """ 
    Parametros: Lista_heroes -> Contine la informacion de los heroes
               Clave -> Pertenece al diccionario,es la caracteristica que se busca
               Max_o_min -> Determina si busca la "maxima" caracteristica o la "minima"
               Genero-> Genero con el cual voy a comparar al heroe, puede ser F,M,NB.
    Funcion: Busca en los dicionarios el heroe con la mayor o menor caracteristica deseada y lo mustra por pantalla.Se le da un formato al mensaje
    Retorna: -1 si la lista esta vaciar
    """     
    if len(lista_heroes) == 0:
        return -1
    # Datos para el formato
    resultado = calcular_max_min_dato_genero(lista_heroes,clave,max_o_min,genero)
    nombre_dato   = obtener_nombre_y_dato(resultado,clave)
    print(f"{nombre_dato}")
    # Creo una lista y guardo el diccionario con mi heroe,las funciones crear categorias y datos funcion con list[dict]
    lista_aux = []
    lista_aux.append(resultado)
    # Creo el formato para el csv
    texto = ""
    texto = crear_categorias(lista_aux,texto)
    texto = crear_datos_personajes(lista_aux,texto)
    
    if guardar_archivo(f"{ROOT_DIR}heroes_{max_o_min}_{clave}_{genero.upper()}.txt",texto):
        return True
    else:
        return False

def sumar_dato_heroe_genero(lista_heroes:list[dict],clave:str,genero:str)->int: 
    """ 
    Parametro: Lista heroes -> Contine la informacion de los heroes
               Clave -> Pertenece al diccionario,es la caracteristica que se busca
               Genero-> Genero con el cual voy a comparar al heroe, puede ser F,M,NB
    Funcion: Acumula la caracteristica deseada de todos los diccionarios  teniendo en cuenta el genero
    Retorna: El valor numerico de esa suma
    """         
    acumulador = 0
    for personajes in lista_heroes:
        if len(personajes) != 0 and isinstance(personajes,dict):
            if personajes.get("genero") == genero.upper():
                acumulador += float(personajes.get(clave))      
        else:
            return 0
    return acumulador

def cantidad_heroes_genero(lista_heroes:list[dict],genero:str):
    """ 
    Parametro: Lista heroes -> Contine la informacion de los heroes
               Genero-> Genero con el cual voy a comparar al heroe, puede ser F,M,NB
    Funcion: acumula la caracteristica deseada de todos los diccionarios  teniendo en cuenta el genero
    Retorna: El valor numerico de esa suma
    """
    heroes_filtrados = filter(lambda heroe: heroe.get("genero") == genero.upper(), lista_heroes)
    suma = sum(1 for heroe in heroes_filtrados)
    return suma

def dividir(dividendo:int,divisor:int)->int:
    """ 
    Variables: dividendo -> Numero el cual se va a dividir
               divisor -> Numero que divide al dividendo
    Funcion: Se ingresan dos numeros y se utilizar para realizar un division 
    Retorna: El resultado numerico de esa division
    """     
    try:
        resultado_division = dividendo/divisor
    except ZeroDivisionError as type_error:
        print(f"Error no se puede realizar la division{type_error}")
    else:
        return resultado_division
    
def calcular_promedio_genero(lista_heroes:list[dict],clave:str,genero:str):
    """ 
    Variables: Lista heroes -> Contine la informacion de los heroes.
               Clave -> Pertenece al diccionario,es la caracteristica que se busca.
               Genero-> Genero con el cual voy a comparar al heroe, puede ser F,M,NB.
    Funcion: Calcula un promedio
    Retorna: El resultado numerico del promedio
    """     
    promedio = dividir(sumar_dato_heroe_genero(lista_heroes,clave,genero),cantidad_heroes_genero(lista_heroes,genero))
    return promedio

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes:list[dict],clave:str,genero:str)->int:
    """ 
    Variables: Lista heroes -> Contine la informacion de los heroes.
               Clave -> Pertenece al diccionario,es la caracteristica que se busca.
               Genero-> Genero con el cual voy a comparar al heroe, puede ser F,M,NB.
    Funcion: Calcula el promedio de una caracteristica especifica y la muestra por pantalla,ademas la guarda en un archivo csv.
    Retorna: -1 si la lista esta vaciar
    """        
    if len(lista_heroes) == 0:
        print("Error: Lista de héroes vacía")
        return False
    
    resultado = calcular_promedio_genero(lista_heroes,clave,genero)
    datos_obtenidos = f"{clave.capitalize()} promedio género {genero.upper()}: {resultado}"
    print(datos_obtenidos)

    guardar_archivo(f"{ROOT_DIR}heroes_promedio_altura_{genero.upper()}.txt",datos_obtenidos)
    
    return True

def calcular_cantidad_tipo(lista_heroes:list[dict],caracteristica:str)->dict:
    """ 
    Variables: Lista heroes -> Contine la informacion de los heroes.
               Caracteristica -> Pertenece al diccionario.
    Funcion: Calcula la cantidad de personajes que hay segun una caracteristica
    Retorna: dict
    """
    diccionario_caracterisitcas = {}
    if len(lista_heroes) == 0:
        return {"Error": "La lista se encuentra vacía" }
    for heroes in lista_heroes:
        for key,value in heroes.items():
            if key == caracteristica:
                if capitalizar_palabras(value) not in diccionario_caracterisitcas:
                    if value == "":
                        diccionario_caracterisitcas["no tiene".capitalize()] = 1
                    else:
                        diccionario_caracterisitcas[capitalizar_palabras(value)] = 1           
                else:
                    diccionario_caracterisitcas[capitalizar_palabras(value)] += 1

    return diccionario_caracterisitcas

def guardar_cantidad_heroes_tipo(diccionario_caracteristicas:dict,caracteristica:str)->bool:
    """ 
    Variables: Diccionario caracteristicas -> Contine la catidad de heroes por caracteristica.
               Caracteristica -> Pertenece al diccionario.
    Funcion: Calcula la cantidad de personajes que hay segun una caracteristica
    Retorna: True si se guarod el archivo y de lo contrario False.
    """

    texto = ""
    for clave,valor in diccionario_caracteristicas.items():
        texto += f"Caracteristica: {caracteristica} {clave} - Cantidad de heroes: {valor}"
        texto += "\n"
    if guardar_archivo(f"{ROOT_DIR}heroes_cantidad_{caracteristica}.txt",texto):
        return True
    else:
        return False

def stark_calcular_cantidad_por_tipo(lista_heroes:list[dict],caracteristica:str)->bool:
    """ 
    Variables: Diccionario caracteristicas -> Contine la catidad de heroes por caracteristica.
               Caracteristica -> Pertenece al diccionario.
    Funcion: Calcula la cantidad de personajes que hay segun una caracteristica y los guarda
    Retorna: True si se guarod el archivo y de lo contrario False.
    """
    diccionario_tipos = calcular_cantidad_tipo(lista_heroes,caracteristica)
    if guardar_cantidad_heroes_tipo(diccionario_tipos,caracteristica):
        return True
    else:
        False

def obtener_lista_de_tipos(lista_heroes:list[dict],caracteristica:str)->set:
    """ 
    Variables: lista_heroes -> contiene los heroes con la informacion 
               Caracteristica -> Pertenece al diccionario.
    Funcion: Itera sobre la lista y guarda los valores de los datos capitalizado las palabras y borrando los duplicados.
    Retorna: Un set de datos
    """
    # lista_valores = []
    # for heroe in lista_heroes:
    #     if heroe.get(caracteristica) != "":
    #         lista_valores.append(heroe[caracteristica])
    #     else:
    #         lista_valores.append("N/A")                     
    # CODIGO EQUIVALENTE CON LIST COMPRENHENSION
    lista_valores = set([capitalizar_palabras(heroe[caracteristica]) if heroe.get(caracteristica, "N/a") != "" else "N/a" for heroe in lista_heroes])
    # la palabra capitaliza viene con un espacio
    # set comprenhension
    lista_valores = {color.strip() for color in lista_valores}
    return lista_valores

def normalizar_dato(dato:str,date_defecto="None")->str:
    """ 
    Variables: Dato -> Contiene el valor de una clave
               Dato_defecto -> Si el valor viene con un str vacio, lo remplaza
    Funcion: Evaluar que el dato no este vacio,en caso de estarlo lo remplaza por el valor por defecto
    Retorna: El dato
    """   
    if dato != "":
        return dato
    else:
        return date_defecto
    
def normalizar_heroe(diccionario_heroe:dict,clave:str)->dict:
    """ 
    Variables: Diccionario heroe -> Contiene la informacion de un heroe
               Clave -> Representa una de las claves del diccionario heroe
    Funcion: Evaluar que el dato no este vacio,en caso de estarlo lo remplaza por el valor por defecto
    Retorna: Diccionaior normalizado
    """ 
    # Capitalizar palabras en el nombre del héroe
    diccionario_heroe['nombre'] = capitalizar_palabras(diccionario_heroe['nombre'])

    # Capitalizar palabras y normalizar el valor asociado a la key
    if clave in diccionario_heroe:
        if not diccionario_heroe[clave]:
            diccionario_heroe[clave] = 'N/A'
        else:
            diccionario_heroe[clave] = capitalizar_palabras(diccionario_heroe[clave])

            # Verificar y convertir a número si es un valor numérico representado como string
            if re.match(r'^-?\d+(\.\d+)?$', diccionario_heroe[clave]):
                diccionario_heroe[clave] = float(diccionario_heroe[clave])

    return diccionario_heroe

def obtener_heroes_por_tipo(lista_heroes:list[dict],set_datos:set,clave:str)->dict[list]:
    """ 
    Variables: Lista heroes -> Contine la informacion de los heroes.
               Set datos -> n set de tipos/variedades (colores de ojos, de pelo, etc)
               Clave -> Pertenece al diccionario,es la caracteristica que se busca.
    Funcion: Crea un diccionario donde los tipos son las claves y los valoeres los nombres de los personajes
    Retorna: diccioanrio 
    """
    diccoionario_de_tipos = {}
    for dato in set_datos:
        if dato not in diccoionario_de_tipos:
            diccoionario_de_tipos[dato] = []
        for heroe in lista_heroes:
            dato_normalizado = normalizar_dato(heroe.get(clave),"N/A")
            dato_normalizado = capitalizar_palabras(dato_normalizado)
            if dato_normalizado == dato:
                diccoionario_de_tipos[dato].append(heroe.get("nombre"))
    return diccoionario_de_tipos

def guardar_heroes_por_tipo(diccionario_de_tipos:dict[list],clave:str)->bool:
    """ 
    Variables: Diccionarios de tipos -> Contine una caracteristica como clave y los personajes corresposndientes como valor
               Clave -> Tipo de dato a evaluar
    Funcion: Recorre el diccionario y formatea un mensaje.Se guarda en un archivo txt
    Retorna: True si salió todo bien, False caso contrario. 
    """    
    texto = ""
    for key,value in diccionario_de_tipos.items():
        flag = True
        texto += f"{clave} {key}: "
        for personaje in value:
            if flag:
                texto += f"{personaje}"
                flag = False
            else:
                texto += f" | {personaje}"
        texto += "\n"
    if guardar_archivo(f"{ROOT_DIR}heroes_segun_{clave}.txt",texto):
        return True
    else: 
        return False
    
def stark_listar_heroes_por_dato(lista_heroes:list[dict],clave:str)->bool:
    """ 
    Variables: Lista heroes -> Contiene la inormaciond de los heroes
               Clave -> Tipo de dato a evaluar
    Funcion: Recorre el diccionario y formatea un mensaje.Se guarda en un archivo txt
    Retorna: True si salió todo bien, False caso contrario. 
    """    
    lista_tipos = obtener_lista_de_tipos(lista_heroes,clave)
    heroes_por_tipo = obtener_heroes_por_tipo(lista_heroes,lista_tipos,clave)
    if guardar_heroes_por_tipo(heroes_por_tipo,clave):
        return True
    else:
        return False




    #stark_guardar_heroe_genero(lista_personajes,"m")
    #print( calcular_min_genero(lista_personajes,"peso","m"))
    #print( calcular_max_genero(lista_personajes,"altura","m"))
    #print(calcular_max_min_dato_genero(lista_personajes,"fuerza","maximo","f"))
    #stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,"altura","maximo","m")
    #print(calcular_promedio_genero(lista_personajes,"fuerza","f"))
    #stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes,"altura","f")
    # diccionario_caracteristicas = calcular_cantidad_tipo(lista_personajes,"color_pelo")
    #guardar_cantidad_heroes_tipo(diccionario_caracteristicas,"color_pelo")
    # stark_calcular_cantidad_por_tipo(lista_personajes,"color_ojos")
    # print(normalizar_heroe(diccionario,"color_pelo"))
    #set_tipos = obtener_lista_de_tipos(lista_personajes,"color_pelo")
    #diccioanrio_de_tipos = obtener_heroes_por_tipo(lista_personajes,set_tipos,"color_pelo")
    #guardar_heroes_por_tipo(diccioanrio_de_tipos,"color_pelo")
    #stark_listar_heroes_por_dato()