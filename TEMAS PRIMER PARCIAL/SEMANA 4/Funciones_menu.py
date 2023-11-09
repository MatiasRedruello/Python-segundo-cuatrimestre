from Funciones_stark_02 import *
"6.1)"
def imprimir_menu(**texto:dict)->None:
    """ 
    Variables: A travez de keywors arguments convierto mis aprametros en iterables (empaqueto todos los parametros en uno)
    Funcion: Recore un iterable y muesta por pantalla, generando un menu
    Retorna: None
    """     
    for oracion in texto:
        imprimir_dato(texto[oracion])

def interaccion_con_el_menu()->int:
    """ 
    Variables: No tiene
    Funcion: Utiliza la funcion imprimir menu mostrar todas las opciones y atravez de un imput el usuario elige una
    Retorna: Un numero que corresponde a una opcion
    """    
    imprimir_menu(texto_1 = "Menú de opciones:",
             texto_2 = "1. Imprimir por consola el nombre de cada superhéroe",
             texto_3 = "2. Imprimir por consola nombre de cada superhéroe junto a la altura del mismo",
             texto_4 = "3. Superheroe mas alto ",
             texto_5 = "4. Superheroe mas bajo ",
             texto_6 = "5. Altura promedio de los  superhéroes ",
             texto_7 = "6. Identidad del superhéroe asociado a cada uno de los indicadores anteriores ",
             texto_8 = "7. superhéroe más pesado",
             texto_9 = "8. superhéroe menos pesado",
             texto_10 = "0. Salir del programa")
    while True:
        entrada = input("Elija una opcion")
        if validar_entero(entrada) and not entrada.isalpha():
            respuesta = int(entrada)
            break
        else:
            print("Error-1, respuesta incorecta elija nuevamente una opcion")

    return respuesta

def menu_app()->None:
    """ 
    Variables: No tiene
    Funcion: Se Encarga de llamar a la opcion seleccionada por el ususario
    Retorna: None
    """    
    while True:   
        respuesta =  interaccion_con_el_menu()
        if respuesta > -1 and respuesta < 15:
            match respuesta:
                case 1:
                    stark_imprimir_nombres_heroes(lista_personajes_actualizada)                
                case 2:
                    stark_imprimir_nombres_alturas(lista_personajes_actualizada,"altura")
                case 3:
                    stark_calcular_imprimir_heroe(lista_personajes_actualizada,"altura","maximo")
                case 4:
                    stark_calcular_imprimir_heroe(lista_personajes_actualizada,"altura","minimo")
                case 5:
                    stark_calcular_imprimir_promedio_altura(lista_personajes_actualizada,"altura")
                case 6:
                    stark_calcular_imprimir_heroe(lista_personajes_actualizada,"altura","maximo","identidad")
                    stark_calcular_imprimir_heroe(lista_personajes_actualizada,"altura","minimo","identidad")
                case 7:
                    stark_calcular_imprimir_heroe(lista_personajes_actualizada,"peso","maximo")
                case 8:
                    stark_calcular_imprimir_heroe(lista_personajes_actualizada,"peso","minimo")
                case 9:
                    pass 
                case 10:
                    pass
                case 11:
                    pass
                case 12:
                    pass
                case 13:
                    pass
                case 14:
                    pass                                                                                                                 
                case 0:
                    break
        else:
            print("Error opcion incorrecta debe elegir un numero del 0 al 14")

                
        