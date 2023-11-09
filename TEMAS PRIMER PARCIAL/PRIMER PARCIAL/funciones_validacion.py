import re
from constantes_examen import JUGADORES
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
    if int(opcion_validada) >= inicio_rango and int(opcion_validada) < fin_rango + 1:
        return opcion_validada
    else:
        print("Error el numero ingresado supera el rango,ingrese un numero del 1 al 12: ")
        resultado = pedir_al_usuario(texto_a_validar,patron)
        return validar_rango(pregunta,resultado,pregunta,patron,25,0)

def validar_nombre(pregunta,opcion_validada:str,texto_a_validar:str,patron:str,lista_nombres:list)->str:
    """
    Parametros:
        Pregunta-> Consigna para el usuario
        opcion_validada-> Paso el primer filtro y es un numero
        Texto_a_validar-> Si no se cumple el rango,es necesario para volver a peguntar.
        Patron-> Exprecion regular con la que voy a validar
        Lista nombres->Lista de los jugadores
    Funcion: Ingreso un texto que contega un str valido y valido que este dentro de la lista d ejugadores
            de lo contrario se pide al usuario que lo ingrese de nuevo.
    Retorno: El dato validado
    """    
    if opcion_validada not in lista_nombres:
        print("Error nombre ingresado no pertenece al  Dramteam o no esta bien scrito: ")
        resultado = pedir_al_usuario(texto_a_validar,patron)
        return validar_nombre(pregunta,resultado,pregunta,patron,lista_nombres)         
    else:
        return opcion_validada