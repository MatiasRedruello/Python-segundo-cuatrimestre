import re
from funciones_base import (stark_guardar_heroe_genero,stark_calcular_imprimir_guardar_heroe_genero,
                            stark_calcular_imprimir_guardar_promedio_altura_genero,calcular_max_min_dato_genero,obtener_nombre_y_dato,
                            stark_calcular_cantidad_por_tipo,stark_listar_heroes_por_dato)

def imprimir_menu_desafio_5(**texto:dict)->None:
    """
    Parametro:Opciones-> Paquete de str
    Funcion:Recorre el diccionario de str e imprime por pantalla cada uno.
    Retorna: None
    """
    for opcion in texto:
        print(texto[opcion])


def stark_menu_principal_desafio_5():
    """
    Parametro:No tiene
    Funcion: Interactua con el usuario,pide una opcion y valida que sea correcta.
    Retorna: Retorna opcion
    """    
    imprimir_menu_desafio_5(texto_a = "A- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M: ",
                            texto_b = "B- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F: ",
                            texto_c = "C- Recorrer la lista y determinar cuál es el superhéroe más alto de género M: ",
                            texto_d = "D- Recorrer la lista y determinar cuál es el superhéroe más alto de género F: ",
                            texto_e = "E- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M: ",
                            texto_f = "F- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F: ",
                            texto_g = "G- Recorrer la lista y determinar la altura promedio de los  superhéroes de género M: ",
                            texto_h = "H- Recorrer la lista y determinar la altura promedio de los  superhéroes de género F: ",
                            texto_i = "I- Informar cual es el nombre del superhéroe asociado a cada uno de los indicadores anteriores: ",
                            texto_j = "J- Determinar cuántos superhéroes tienen cada tipo de color de ojos: ",
                            texto_k = "K- Determinar cuántos superhéroes tienen cada tipo de color de pelo: ",
                            texto_l = "L- Determinar cuántos superhéroes tienen cada tipo de inteligencia: ",
                            texto_m = "M- Listar todos los superhéroes agrupados por color de ojos: ",
                            texto_n = "N- Listar todos los superhéroes agrupados por color de pelo: ",
                            texto_o = "O- Listar todos los superhéroes agrupados por tipo de inteligencia: ",
                            texto_z = "Z- Salir")
    while True:
            opcion = re.match(r"^[abcdefghijklmnoz]{1}$",input("Elija una opcion"),re.I)
            if opcion:
                break
            else:
                 print(f"Error opcion incorrecta. Elija nuevamente: ")
 
    return opcion.group()

def stark_marvel_app_5(lista_personajes:list[dict])->None:
    """
    Parametro:Opciones-> Lista personajes: Contiene la informacion
    Funcion: Ejecucion principal del programa.
    Retorna: None
    """
    while True:
        match(stark_menu_principal_desafio_5().upper()):
            case "A":
                stark_guardar_heroe_genero(lista_personajes,"M")
            case "B":
                stark_guardar_heroe_genero(lista_personajes,"F")
            case "C":
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,"altura","maximo","M")
            case "D":
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,"altura","maximo","F")
            case "E":
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,"altura","minimo","M")
            case "F":
                stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,"altura","minimo","F")
            case "G":
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes,"altura","M")
            case "H":
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes,"altura","F") 
            case "I":
                # Personajes mas alatos por genero
                maximo_masculino = calcular_max_min_dato_genero(lista_personajes,"altura","maximo","M")
                nombre_maximo_masculino = obtener_nombre_y_dato(maximo_masculino,"altura")
                maximo_femenino = calcular_max_min_dato_genero(lista_personajes,"altura","maximo","F")
                nombre_maximo_femenino = obtener_nombre_y_dato(maximo_femenino,"altura") 
                # Personajes mas batos por genero  
                minimo_masculino = calcular_max_min_dato_genero(lista_personajes,"altura","minimo","M")
                nombre_minimo_masculino = obtener_nombre_y_dato(minimo_masculino,"altura")
                minimo_femenino = calcular_max_min_dato_genero(lista_personajes,"altura","minimo","F")
                nombre_minimo_femenino = obtener_nombre_y_dato(minimo_femenino,"altura")
                print("",nombre_maximo_masculino,f"\n",
                      nombre_maximo_femenino,f"\n",
                      nombre_minimo_masculino,f"\n",
                      nombre_minimo_femenino)
            case "J":
                stark_calcular_cantidad_por_tipo(lista_personajes,"color_ojos")
            case "K":
                stark_calcular_cantidad_por_tipo(lista_personajes,"color_pelo")
            case "L":
                stark_calcular_cantidad_por_tipo(lista_personajes,"inteligencia")
            case "M":
                stark_listar_heroes_por_dato(lista_personajes,"color_ojos")
            case "N":
                stark_listar_heroes_por_dato(lista_personajes,"color_pelo")
            case "O":
                stark_listar_heroes_por_dato(lista_personajes,"inteligencia")
            case "Z":
                break                                                                                                 


