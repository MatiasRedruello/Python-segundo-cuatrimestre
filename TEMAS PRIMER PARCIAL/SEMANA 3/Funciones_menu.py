from Funciones_stark_01 import *
import os
def imprimir_menu(**texto:dict)->None:
    """ 
    Variables: A travez de keywors arguments convierto mis aprametros en iterables (empaqueto todos los parametros en uno)
    Funcion: Recore un iterable y muesta por pantalla, generando un menu
    Retorna: None
    """     
    for oracion in texto:
        print(texto[oracion])

def interaccion_con_el_menu():
    imprimir_menu(texto_1 = "Menú de opciones:",
             texto_2 = "1. Nombres de los miembros masculinos",
             texto_3 = "2. Nombres de los miembros femeninos",
             texto_4 = "3. Superheroe mas alto masculino",
             texto_5 = "4. Superheroe mas alto femenino",
             texto_6 = "5. Superheroe mas bajo masculino",
             texto_7 = "6. Superheroe mas bajo masculino",
             texto_8 = "7. Promedio de las altura de los eprsoanjes masculinos",
             texto_9 = "8. Promedio de las altura de los eprsoanjes femeninos",
             texto_10 = "9. Cuántos superhéroes tienen cada tipo de color de ojos",
             texto_11 = "10. Cuántos superhéroes tienen cada tipo de color de pelo",
             texto_12 = "11. Cuántos superhéroes tienen cada tipo de color de inteligencia",
             texto_13 = "12. Listar todos los superhéroes agrupados por color de ojos",
             texto_14 = "13. Listar todos los superhéroes agrupados por color de pelo",
             texto_15 = "14. Listar todos los superhéroes agrupados por color de inteligencia",
             texto_16 = "0. Salir del programa")
    
    return input("Elija una opcion")

def menu_app():
    
    while True:
        match interaccion_con_el_menu():
            
            case "1":
                nombre_de_los_personajes(lista_personajes,"M","genero")                
            case "2":
                nombre_de_los_personajes(lista_personajes,"F","genero")
            case "3":
                altura_de_los_superheroes(lista_personajes,"M","genero","alto")
            case "4":
                altura_de_los_superheroes(lista_personajes,"F","genero","alto")
            case "5":
                altura_de_los_superheroes(lista_personajes,"M","genero","bajo")
            case "6":
                altura_de_los_superheroes(lista_personajes,"F","genero","bajo")
            case "7":
                print(promediar(lista_personajes,"M","genero"))   
            case "8":
                print(promediar(lista_personajes,"F","genero")) 
            case "9":
                print(agrupar_superheroes_por_caracteristicas(lista_personajes,"color_ojos")) 
            case "10":
                print(agrupar_superheroes_por_caracteristicas(lista_personajes,"color_pelo"))
            case "11":
                print(agrupar_superheroes_por_caracteristicas(lista_personajes,"inteligencia"))
            case "12":
                print(nombre_de_los_personajes_por_tipo_de_caracteristica(lista_personajes,"color_ojos"))
            case "13":
                print(nombre_de_los_personajes_por_tipo_de_caracteristica(lista_personajes,"color_pelo"))
            case "14":
                print(nombre_de_los_personajes_por_tipo_de_caracteristica(lista_personajes,"inteligencia"))                                                                                                                 
            case "0":
                break
            
        def limpiar_consola() -> None:
            """
            Imprime un mensaje indicando que limpiará la consola al presionar la tecla enter.
                Para que funcione hay que importar el modulo os de la siguiente manera:
                import os
            Recibe: Nada
            Devuelve: Nada
            """
            _ = input("\nPresione enter para continuar... ")
            if os.name in ['ce', 'nt', 'dos']:
                os.system('cls')
            else:
                os.system('clear')  
      