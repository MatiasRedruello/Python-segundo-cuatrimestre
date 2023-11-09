import re
from funciones_validacion import(validar_rango,pedir_al_usuario,validar_nombre)
from constantes_examen import (JUGADORES)
from clase_jugador import JugadorDreamTeam

def fromato_jugadores(lista_jugadores)->None:
    """
    Parametro:
            Lista jugadores-> Contiene el nombre de los jugadores del Dream Team
    Funcion:Recorre La lista y los muestra por pantall
    Retorna: None
    """    
    print("jugadores")
    for i in range(len(lista_jugadores)):
        print(f"{i+1}) {JUGADORES[i]:<20}")

def imprimir_menu_dream_team(**texto:dict)->None:
    """
    Parametro:Opciones-> Paquete de str
    Funcion:Recorre el diccionario de str e imprime por pantalla cada uno.
    Retorna: None
    """
    for opcion in texto:
        print(texto[opcion])


def dream_team_menu_principal():
    """
    Parametro:No tiene
    Funcion: Interactua con el usuario,pide una opcion y valida que sea correcta.
    Retorna: Retorna opcion
    """    
    imprimir_menu_dream_team(texto_a = "A- Mostrar la lista de todos los jugadores del Dream Team",
                            texto_b = "B- Seleccionar un jugador por su índice",
                            texto_c = "C- Guardar las estadísticas de ese jugador en un archivo CSV",
                            texto_d = "D- Buscar un jugador por su nombre",
                            texto_e = "E- Mostrar el promedio de puntos por partido de todo el equipo del Dream Team,ordenado por nombre de manera ascendente",
                            texto_f = "F- Ingresar el nombre de un jugador y mostrar si ese jugadores miembro del Salón de la Fama del Baloncesto. ",
                            texto_g = "G- Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.",
                            texto_h = "H- Calcular y mostrar el jugador con la mayor cantidad de bloqueos_totales.Se guarda en csv,json y sql",
                            texto_i = "I- Ordenar y mostrar los datos por el jugador sumando los robos totales más los bloqueos totales",
                            texto_j = "J- Crear la tabla posiciones",
                            texto_k = "k- Salir",
                            )
    while True:
            opcion = re.match(r"^[abcdefghijklmnoz]{1}$",input("Elija una opcion"),re.I)
            if opcion:
                break
            else:
                 print(f"Error opcion incorrecta. Elija nuevamente: ")
 
    return opcion.group()

def dream_team_app()->None:
    """
    Parametro:No tiene
    Funcion: Ejecucion principal del programa.
    Retorna: None
    """
    flag_ejecucion = False 
    jugador = JugadorDreamTeam()# lo creo aca para hacerlo una sola vez y que funcione en todos lados
    lista_dream_team = jugador.equipo.jugadores_lista # Lista con los jugadores    
    while True:

        match(dream_team_menu_principal().upper()):
            case "A":
                jugador.lista_jugador_posicion()
            case "B":
                #Muestra  los nombres de los jugadores
                fromato_jugadores(JUGADORES)                
                # validaciones
                patron = r"^([1-9]{1,2})$"
                consigna = f"Que jugador desea buscar: "
                validacion_uno = pedir_al_usuario(consigna,patron)
                validar_indice_jugador = validar_rango(consigna,validacion_uno,consigna,patron,12,0)
                jugador.mostrar_estadisticas(validar_indice_jugador,lista_dream_team)  
                flag_ejecucion = True       
            case "C":
                if flag_ejecucion == True:
                     # no entiendo porque tengo que crear el objeto de nuevo, preguntar
                    diccionario_jugador = jugador.diccionario_del_jugador_por_indice(validar_indice_jugador,lista_dream_team)
                    nombre_jugador = diccionario_jugador.get("nombre")
                    jugador.guardar_jugador_en_csv([diccionario_jugador],nombre_jugador) 
                else:
                    print("Error no puede crear el csv del eprsonaje,si primero no elige uno")
                    return dream_team_app()               
            case "D":
                patron_validar_nombre = r"^[a-z]+( [a-z]+)$"
                consigna = f"Que jugador desea buscar:"
                validacion_nombre = pedir_al_usuario(consigna,patron_validar_nombre)
                validacion_de_lista = validar_nombre(consigna,validacion_nombre,consigna,patron_validar_nombre,JUGADORES)

                jugador.mostrar_logros(validacion_de_lista)                               
            case "E":
                
                caracteristica = "promedio_puntos_por_partido"
                promedio_del_equipo = jugador.promedio_puntos_partidos()
                print(f"El promedio de puntos por partido de cada jugador es: {promedio_del_equipo}")
                jugador.jugadores_ordenados_por_caracteristicas(lista_dream_team,caracteristica,True)
            case "F":
                patron_validar_nombre = r"^[a-z]+( [a-z]+)$"
                consigna = f"Que jugador desea buscar :"                
                validacion_nombre = pedir_al_usuario(consigna,patron_validar_nombre)
                validacion_de_lista = validar_nombre(consigna,validacion_nombre,consigna,patron_validar_nombre,JUGADORES)    
                
                jugador.hall_of_fame(validacion_de_lista)
            case "G":
                caracteristica = "rebotes_totales"
                jugador.jugadores_ordenados_por_caracteristicas(lista_dream_team,caracteristica,True)                                       
            case "H":
                #ordenar y mostrar por pantalla
                caracteristica = "bloqueos_totales"
                jugador.jugadores_ordenados_por_caracteristicas(lista_dream_team,caracteristica,True) 
                # guardar en cs
                nombre_jugador = "Redruello"
                jugadores_ordenados = jugador.ordenar_jugadores_por_caracteristica(lista_dream_team,caracteristica,True)
                jugador.guardar_jugador_en_csv(jugadores_ordenados,nombre_jugador)
                # guardar json
                jugador.guardar_en_json(f"./PRIMER PARCIAL/dream_team_ordenado.json",jugadores_ordenados)
                # guardar en base de datos
                ruta_sql = f"./PRIMER PARCIAL/Base_de_datos.db"
                jugador.acceder__crear_base_datos_sql(ruta_sql)
                jugador.guardar_en_sql(ruta_sql,jugadores_ordenados)
            case "I":
                # validar filtro jugador
                patron = r"^([1-9]{1,2})$"
                consigna = f"Cuantos jugadores quiere buscar: "
                validacion_uno = pedir_al_usuario(consigna,patron)
                validar_indice_jugador = validar_rango(consigna,validacion_uno,consigna,patron,12,0)
                #filtrar
                lista_jugadores_filtrada  =  jugador.filtrar_n_jugadores(validar_indice_jugador,lista_dream_team)
                estadistica_uno = "robos_totales"
                estadistica_dos = "bloqueos_totales"
                jugadores_ordenados = jugador.mostrar_jugadores_ordenados_por_porcentaje_de_suma_estadisticas(lista_jugadores_filtrada,estadistica_uno,estadistica_dos,True)
            case "J":
                nombre_archivo = "posiciones"
                jugador.guardar_jugador_posicion_en_csv(lista_dream_team,nombre_archivo) 
                #Con sql
                ruta_posiciones_sql = f"./PRIMER PARCIAL/Base_de_datos_posiciones.db"
                jugador.acceder_crear_base_datos_posiciones_sql(ruta_posiciones_sql)
                jugador.guardar_posiciones_en_sql(ruta_posiciones_sql,lista_dream_team)                                
            case "k":
                break         
                                                                                              


