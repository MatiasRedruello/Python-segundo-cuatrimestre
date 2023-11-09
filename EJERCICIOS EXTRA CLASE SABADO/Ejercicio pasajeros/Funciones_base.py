#from Pasajeros import lista_pasajeros
import re
import json

ruta_pasajeros_json = r"EJERCICIOS EXTRA CLASE SABADO/Ejercicio pasajeros/pasajeros.json"
lista_de_claves = ["Nombre","Apellido","Edad","Nro. Pasaporte","Email","Nro. Telefono"]

def cargar_json(pasajeros_data:str,modo_apertura:str)->dict:
    """
    Parametros: Pasajeros data-> Datos de los pasajeros.
                Modo apertura-> Como quiero abrir el archivo
    Funcion: Abro un archivo json y lo guardo en una variable.
    Retorno: El archivo
    """
    with open(pasajeros_data,modo_apertura,encoding="utf-8") as archivo:       
        datos_actuales = json.load(archivo)
        # En la linea 18 paso la clave al diccionario para que me traiga la lista 
        datos_actuales_lista = datos_actuales  

    return datos_actuales_lista
informacio_pasajeros = cargar_json(ruta_pasajeros_json,"r")

def actualizar_json(pasajeros_data:str,modo_apertura:str,dato:dict)->dict:
    """
    Parametros: Pasajeros data-> D   atos de los pasajeros.
                Modo apertura-> Como quiero abrir el archivo
                Dato-> Es el diccionario que voy a agregar.
    Funcion: Abro un archivo json,acualizo la infornmaicion y lo guardo en una variable.
    Retorno: El archivo
    """
    with open(pasajeros_data,modo_apertura,encoding="utf-8") as archivo:      
        datos_actuales_lista = json.dump(dato,archivo,indent=4,ensure_ascii=False)   

    return datos_actuales_lista

def normalizar_datos(diccionario:dict[list[dict]])->dict[list[dict]]:
    """
    Parametro: Lista-> Contienela informacion evaluar.
    Funcion: Recorre el contenido,evalua tipos de datos,ormaliza y actualiza de ser necesario.
    retorna: La lista normalizada.
    """ 
    for pasajero in diccionario["lista_pasajeros"]:
        for informacion in pasajero:
            #FORMA  CON REGEX:  
            if not isinstance(pasajero[informacion],int):
                if re.match(r"^[\+]{0,1}[\d]+$",pasajero[informacion]): #macheo edad y telefono
                    #Metodo update de dict,paso la clave y a travez de sub saco el "+" del num.tel y paso a int
                    pasajero.update({informacion:int(re.sub(r"\+","",pasajero.get(informacion)))})
            
            # FORMA SIN REGEX
            # if informacion == "Nro. Teléfono" and not isinstance(pasajero[informacion],int):
                # pasajero.update({informacion:int(re.sub(r"\+","",pasajero[informacion]))})
            # if informacion == "Edad" and not isinstance(pasajero[informacion],int):
                # pasajero.update({informacion:int(re.sub(r"\+","",pasajero[informacion]))})
            
    return diccionario

informacio_pasajeros_normalizada = normalizar_datos(informacio_pasajeros)

def imprimir_dato(dato)->None:
    """
    Parametro:Dato-> Dato que se desea imprimir
    Funcion:Imprime el dato recibido, el tipo de dato puede variar.
    Retorna: None
    """
    print(dato)

def pedir_datos()->dict:
    """
    Parametros: No tiene
    Funcion: Crea un diccionario y agrega un nuevo pasajero
    Retorna: un diccionario
    """
    diccionario_aux = {}
    while True:
        try:
            nombre = re.match(r"^[a-zA-Z]+$",input("Cual es su nombre: ")).group()
            diccionario_aux["Nombre"] = str(nombre).lower().capitalize()

            apellido = re.match(r"^[a-zA-Z]+$",input("Cual es su apellido: ")).group()
            diccionario_aux["Apellido"] = apellido.lower().capitalize()

            edad = re.match(r"^[1-9]{2}$",input("Cual es su edad: ")).group()
            diccionario_aux["Edad"] = int(edad)

            nro_pasaporte = re.match(r"^[\w]{2}[\d]+$",input("Cual es su numero de pasaporte.EJ AB123456: ")).group()
            diccionario_aux["Nro. Pasaporte"] = nro_pasaporte

            email = re.match(r"^[\d\w\._-]+[@]{1}[\w]+[\.]{1}[\w]{3}$",input("Cual es su email: ")).group()
            diccionario_aux["Email"] = email
    
            nro_telefono = re.match(r"^[\d]{8}$",input("Cual es su numero de telefono sin numero de area: ")).group()
            diccionario_aux["Nro. Teléfono"] = int(nro_telefono)

            break
        except AttributeError as que_error:
            print(f"Error {que_error},esta ingresando mal los datos, vuelva a ingresarlo: ")

    return diccionario_aux

def pedir_un_dato(texto:str)->str:
    """
    Parametros: Texto-> Cadena de caracteres qe quiere mostrar en el imput
    Funcion: Pide un dato por input, se le puede predefinir un texto.
    Retorna: El dato ingresado
    """    
    dato = str(input(texto))
    
    return dato

def buscar_pasajero(disccionario:dict[list[dict]],buscar:str)->dict:
    """
    Parametros: Lista-> Contiene los pasajeros
                Clave-> Str que contiene la clave con la cual buscamos el pasajero
    Funcion: Busca a el pasajero
    Retorna: El pasajero
    """
    
    for pasajero in disccionario["lista_pasajeros"]:
        for valor in pasajero.values():
            if valor == buscar:
                return pasajero


def suma(edades:int)->int:
    """
    Parametros: Edades-> Crecibe un numero que representa una edad               
    Funcion: Suma las edades
    Retorna: La suma    
    """
    suma = 0
    
    suma = suma + edades

    return suma


def promedio_edades(edades:int,diccionario:dict)->float:
    """
    Parametros: Edades-> Recibe la suma de las edades    
                Diccionario-> Contiene las edades de los apsajeros y la cantida de ellos que corresponde a cada edad            
    Funcion: Calcula un promedio
    Retorna: El promedio    
    """
    promedio = suma(edades)/len(diccionario["lista_pasajeros"])

    return promedio


def edad_mas_comun(diccionario:dict[list[dict]])->dict:
    """
    Parametros: Diccioanrio-> Contiene la informacion de los pasajeros               
    Funcion: Crea un nuevo diccionario con las edades y la cantidad de pasajeros que le corresponde a cada edad
    Retorna: Diccionario   
    """
    diccioanrio_edades = {}
    for pasajero in diccionario["lista_pasajeros"]:
        for clave,valor in pasajero.items():
            if clave == "Edad":
                if  pasajero.get(clave) not in diccioanrio_edades:
                    diccioanrio_edades[valor] = 1
                else:
                    diccioanrio_edades[valor] += 1

    return diccioanrio_edades

