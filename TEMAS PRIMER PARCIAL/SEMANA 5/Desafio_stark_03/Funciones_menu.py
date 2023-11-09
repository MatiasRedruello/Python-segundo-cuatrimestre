from Funciones_stark_03 import *
"0.0)"
def imprimir_menu_2(**texto:dict)->None:
    """ 
    Variables: A travez de keywors arguments convierto mis aprametros en iterables (empaqueto todos los parametros en uno)
    Funcion: Recore un iterable y muesta por pantalla, generando un menu
    Retorna: None
    """     
    for oracion in texto:
        imprimir_dato(texto[oracion])
"0.1)"
def stark_menu_principal_2()->int:
    """ 
    Variables: No tiene
    Funcion: Utiliza la funcion imprimir menu mostrar todas las opciones y atravez de un imput el usuario elige una
    Retorna: Un numero que corresponde a una opcion
    """    
    imprimir_menu_2(texto_1 = "Menú de opciones:",
             texto_2 = "1. Nombre de cada superhéroe de género M",
             texto_3 = "2. Nombre de cada superhéroe de género F",
             texto_4 = "3. Superhéroe más alto de género M",
             texto_5 = "4. Superhéroe más alto de género F",
             texto_6 = "5. Superhéroe más bajo de género M",
             texto_7 = "6. Superhéroe más bajo de género F",
             texto_8 = "7. Determinar la altura promedio de los  superhéroes de género M",
             texto_9 = "8. Determinar la altura promedio de los  superhéroes de género F",
             texto_10 = "9. Cuántos superhéroes tienen cada tipo de color de ojos",
             texto_11 = "10. Cuántos superhéroes tienen cada tipo de color de pelo",
             texto_12 = "11. Cuántos superhéroes tienen cada tipo de color de inteligencia",
             texto_13 = "12. Listar todos los superhéroes agrupados por color de ojos",
             texto_14 = "13. Listar todos los superhéroes agrupados por color de pelo",
             texto_15 = "14. Listar todos los superhéroes agrupados por color de inteligencia",
             texto_16 = "0. Salir del programa")
    
    entrada = input("Elija una opcion")

    if validar_entero(entrada) and not entrada.isalpha():
        respuesta = int(entrada) 
    else:
        respuesta = stark_menu_principal_2()
      

    return respuesta
"0.2)"
def menu_app()->None:
    """ 
    Variables: No tiene
    Funcion: Se Encarga de llamar a la opcion seleccionada por el ususario
    Retorna: None
    """    
    while True: 

        respuesta = stark_menu_principal_2()
        if respuesta > -1 and respuesta < 15:
            match respuesta:
                case 1:
                    stark_imprimir_heroe_genero(lista_personajes_normalizada,"m")            
                case 2:
                    stark_imprimir_heroe_genero(lista_personajes_normalizada,"f")
                case 3:
                     stark_calcular_imprimir_heroe_genero(lista_personajes_normalizada,"altura","m","maximo")
                case 4:
                    stark_calcular_imprimir_heroe_genero(lista_personajes_normalizada,"altura","f","maximo")
                case 5:
                    stark_calcular_imprimir_heroe_genero(lista_personajes_normalizada,"altura","m","minimo")
                case 6:
                    stark_calcular_imprimir_heroe_genero(lista_personajes_normalizada,"altura","f","minimo")
                case 7:
                    print(stark_calcular_imprimir_promedio_altura_genero(lista_personajes_normalizada,"altura","M"))
                case 8:
                    print(stark_calcular_imprimir_promedio_altura_genero(lista_personajes_normalizada,"altura","F"))
                case 9:
                    stark_calcular_cantidad_por_tipo(lista_personajes_normalizada,"color_ojos") 
                case 10:
                    stark_calcular_cantidad_por_tipo(lista_personajes_normalizada,"color_pelo")
                case 11:
                    stark_calcular_cantidad_por_tipo(lista_personajes_normalizada,"inteligencia")
                case 12:
                    stark_listar_heroes_por_dato(lista_personajes_normalizada,"color_ojos")
                case 13:
                    stark_listar_heroes_por_dato(lista_personajes_normalizada,"color_pelo")
                case 14:
                    stark_listar_heroes_por_dato(lista_personajes_normalizada,"inteligencia")                                                                                                                 
                case 0:
                    break
        else:
            print("Error opcion incorrecta debe elegir un numero del 0 al 14")

                
        