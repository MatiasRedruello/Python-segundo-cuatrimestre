from Funciones_principales import (estadisticas_por_edades,mostrar_lista_pasajeros,pedir_un_dato,buscar_pasajero,borrar_pasajero,modificar_datos_pasajeros,imprimir_dato,
                                   agregar_pasajero,informacio_pasajeros_normalizada)
import re
def imprimir_menu(**opciones:dict)->None:
    """
    Parametro:Opciones-> Paquete de str
    Funcion:Recorre el diccionario de str e imprime por pantalla cada uno.
    Retorna: None
    """
    for key in opciones:
        imprimir_dato(opciones[key])

def opciones_menu()->str:
    """ 
    Parametro: No tiene
    Funcion: Utiliza la funcion imprimir menu para mostrar todas las opciones y atravez de un imput el usuario elige una de ellas
    Retorna: Un string que corresponde a una opcion
    """
    imprimir_menu(texto_uno = "1- Agregar pasajero",
                  texto_dos = "2- Modificar pasajero",
                  texto_tres = "3- Borrar pasajero",
                  texto_cuatro ="4- Buscar pasajero por nombre",
                  texto_sinco = "5- Buscar pasajero por número de pasaporte",
                  texto_seis = "6- Mostrar la lista de pasajeros",
                  texto_siete = "7- Mostrar estadísticas por edades:",
                  texto_ocho = "8- Salir")
    #OPCION UNO REGEX:
    # opcion_elegida = input("ingrese una opcion")
    # patron = r"^[1-8]{1}"
    # while not re.match(patron,opcion_elegida):
    #     print("La opcion elegida es incorrecta ingrese un numero del 1 al 8")
    #     opcion_elegida = input("ingrese una opcion")

    #OPCION DOS TRY-EXCEPT:
    while True:
        try:
            opcion_elegida = int(input("ingrese una opcion"))
            break
        except ValueError:
            print("Error ingrese un valor numerico: ")
    
    return opcion_elegida
    
    

def menu_app():
    """
    Parametro:Opciones-> No tiene
    Funcion:Ejecuta el programa principal
    Retorna: No tiene
    """    
    while True:
        match(opciones_menu()):
            case 1:
                agregar_pasajero(informacio_pasajeros_normalizada) 
            case 2:
                modificar_datos_pasajeros(informacio_pasajeros_normalizada)
            case 3:
                borrar_pasajero(informacio_pasajeros_normalizada)
            case 4:
                dato_nombre = pedir_un_dato("Ingrese el nombre del pasajero asi lo buscamos")
                pasajero_encontrado_nombre = buscar_pasajero(informacio_pasajeros_normalizada,dato_nombre)
                imprimir_dato(pasajero_encontrado_nombre) 
            case 5:
                dato_nro_pasaporte = pedir_un_dato("Ingrese el numero de pasaporte del pasajero asi lo buscamos ej: AS123456")
                pasajero_encontrado_nro_pasaporte = buscar_pasajero(informacio_pasajeros_normalizada,dato_nro_pasaporte)
                imprimir_dato(pasajero_encontrado_nro_pasaporte)
            case 6:
                mostrar_lista_pasajeros(informacio_pasajeros_normalizada) 
            case 7:
                imprimir_dato(estadisticas_por_edades(informacio_pasajeros_normalizada))
            case 8:
                break                                                                                                                 
            