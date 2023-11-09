import re
import json
from funciones_archivos import leer_archivo_json,ROOT_DIR


def pedir_al_usuario(texto:str,patron:str)->str:
    """
    Parametros:
        Texto-> El mensaje que queiro que aparezca por input
        patron-> Exprecion regular con la que voy a validar
    Funcion: Pide un dato por input y valida que sea un str numerico
    Retorno: El dato pedido
    """
    while True:
        resultado  = input(texto)
        resultado_validado = re.match(patron,resultado,re.I)            
        if resultado_validado:
            break
        else:
            print(f"Error opcion incorrecta. Elija nuevamente: ")
    return resultado_validado.group()

def validar_rango(pregunta,opcion_validada:str,texto_a_validar:str,patron:str,fin_rango:int,inicio_rango:int = 0)->str:
    """
    Parametros:
        Pregunta-> Consigna para el usuario
        opcion_validada-> Paso el primer filtro y es un numero
        Texto_a_validar-> Si no se cumple el rango,es necesario para volver a peguntar.
        Patron-> Exprecion regular con la que voy a validar
        Fin_rango-> Valor numerico donde termina el rango
        Inicio_rango-> Valor numerico donde Inicia el rango
    Funcion: Ingreso un texto que contega un numero y valido que este dentro de un rango y y si es correcto lo retorna
            de lo contrario se pide al usuario que lo ingrese de nuevo.
    Retorno: El dato validado
    """
    if int(opcion_validada) > inicio_rango and int(opcion_validada) < fin_rango:
        return opcion_validada
    else:
        print("Error el numero ingresado supera el rango,ingrese un numero del 1 al 24: ")
        resultado = pedir_al_usuario(texto_a_validar,patron)
        return validar_rango(pregunta,resultado,pregunta,patron,25,0)

def listar_n_heroes(lista_heroes:list[dict],cantidad:str)->None:
    """
    Parametros:
        Lista heroes-> Contiene la informacion de los superheroes de marvel
        Cantidad -> Representa la cantidad de heroes a mostrar
    Funcion:
    Retorno:
    """
    for indice in range(len(lista_heroes)):
        if indice < int(cantidad):
            print(lista_heroes[indice])

def ordenar_heroes(lista_heroes:list[dict],caracteristica:str,ordenar:str)->list[dict]:
    """
    Parametros:
        Lista heroes-> Contiene la informacion de los superheroes de marvel
        Caracteristica-> Es el parametro que voy a usar para ordenar
        Ordenar-> Como lo voy a ordenar
    Funcion: Ordena a los heroes segun la caracteristica pedida y un orden
    Retorno:lista ordenada
    """   
    #sort() modifica la lista original
    #sorted() crea una lista ordenada
    #FUNCION SORTED()
    if ordenar.lower() == "asc": 
        lista_ordenada = sorted(lista_heroes,key= lambda x:x[caracteristica])
    elif ordenar.lower() == "desc":
        lista_ordenada = sorted(lista_heroes,key= lambda x:x[caracteristica],reverse=True)

    for heroe in lista_ordenada:
        print(heroe["nombre"], heroe[caracteristica])
    return lista_ordenada


def buscar_heroes_por_inteligencia(lista_heroes:list[dict],tipo_inteligencia:str):
    """
    Parametros:
        Lista heroes-> Contiene la informacion de los superheroes de marvel
        Caracteristica-> Es el parametro que voy a usar para filtrar.
    Funcion: filtra los heroes por tipo de inteligencia
    Retorno:lista filtrada
    """
    # FORMA DE HACERLO CON FILTER:
    #heroes_filtrados = filter(lambda heroe: heroe.get("inteligencia") == tipo_inteligencia, lista_heroes)
    # FORMA DE HACERLO CON LIST COMPRENHENSION
    lista_filtrado = [heroe for heroe in lista_heroes if heroe.get("inteligencia") == tipo_inteligencia.lower()]  
    for heroe in lista_filtrado:
        print(heroe)

if __name__ == "__main__":
    lista_heroes = leer_archivo_json(f"{ROOT_DIR}data_stark.json","heroes")
    #'^[a-zA-Z ]+\|\|[a-zA-Z ]+#[0-9]{1,2}$'
    """
    a)
    patron = "^[1-9]+$"
    pregunta = "Ingrese un numero del 1 al 24: "
    # Valido que lo ingresado cumpla con el RE
    validar_str = pedir_al_usuario(pregunta,patron)
    # Validacion adicional para numeros
    validar_rango_numerico = validar_rango(validar_str,pregunta,patron,25,1)
    listar_n_heroes(lista_heroes,validar_rango_numerico)"""
    """ "b)"
    patron = f"^(asc|desc)$"
    consigna = "Vamos a ordenar a los heroes por altura, lo hacemos de forma ascendente(asc) o descendente(desc): "
    respuesta = pedir_al_usuario(consigna,patron)
    ordenar_heroes(lista_heroes,"altura",respuesta)"""
    """patron = f"^(good|average|high)$"
    consigna = "Vamos a filtrar los heroes por tipo de inteligencia good, average, high. Cual Elige?: "
    respuesta = pedir_al_usuario(consigna,patron)
    buscar_heroes_por_inteligencia(lista_heroes,respuesta)"""