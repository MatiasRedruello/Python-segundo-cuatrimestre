    #quick sort
def quick_sort(lista:list[dict],caracteristica,ordenar = False):
    if len(lista) < 2:
            return lista
    else:
        lista_dream_team = lista.copy()
        
        jugador_pivot = lista_dream_team.pop()
        mas_grandes = []
        mas_chicos = []

        for jugador in lista_dream_team:
            if ordenar == False:    
                if jugador["estadisticas"][caracteristica] > jugador_pivot["estadisticas"][caracteristica]:
                    mas_grandes.append(jugador)
                elif jugador["estadisticas"][caracteristica] <= jugador_pivot["estadisticas"][caracteristica]:
                    mas_chicos.append(jugador)
            elif ordenar == True:
                if jugador["estadisticas"][caracteristica] < jugador_pivot["estadisticas"][caracteristica]:
                    mas_grandes.append(jugador)
                elif jugador["estadisticas"][caracteristica] >= jugador_pivot["estadisticas"][caracteristica]:
                    mas_chicos.append(jugador)

        return quick_sort(mas_chicos, caracteristica,ordenar) + [jugador_pivot] + quick_sort(mas_grandes, caracteristica,ordenar)
    
def quick_sort_suma_estadisticas(lista:list[dict],caracteristica_uno:str,caracteristica_dos,ordenar = False):
    """
    Parametros: 
                Lista-> Contiene la informacion de un jugador
                Cara-> Es parte de las claves de estadisticas
                Estadistica dos-> Es parte de las claves de estadisticas
                Orden-> Como quiero ordenar, tiene valor falce por defecto
    Funcion: Variante de quick sort.Suma las dos caracterisitcas del jugador que se asigna como pivot y del jugador a ordenar y esos valores son los que se comparan
                para realizar el ordenamiento
    Retorno: La funcion en si misma , recursividad
    """
    if len(lista) < 2:
            return lista
    else:
        lista_dream_team = lista.copy()
        jugador_pivot = lista_dream_team.pop()
        #aca sumo las dos caracterisiticas que voy a usar para comparar
        suma_de_pivot = 0
        suma_jugador_no_pivot = 0

        suma_de_pivot = jugador_pivot["estadisticas"][caracteristica_uno] + jugador_pivot["estadisticas"][caracteristica_dos]
        
        mas_grandes = []
        mas_chicos = []

        for jugador in lista_dream_team:
            #aca sumo las dos caracterisiticas que voy a usar para comparar
            suma_jugador_no_pivot =  jugador["estadisticas"][caracteristica_uno] + jugador["estadisticas"][caracteristica_dos]         
            if ordenar == False:    
                if suma_jugador_no_pivot > suma_de_pivot:
                    mas_grandes.append(jugador)
                elif suma_jugador_no_pivot <= suma_de_pivot:
                    mas_chicos.append(jugador)
            elif ordenar == True:
                if suma_jugador_no_pivot < suma_de_pivot:
                    mas_grandes.append(jugador)
                elif suma_jugador_no_pivot >= suma_de_pivot:
                    mas_chicos.append(jugador)

        return quick_sort_suma_estadisticas(mas_chicos, caracteristica_uno,caracteristica_dos,ordenar) + [jugador_pivot] + quick_sort_suma_estadisticas(mas_grandes, caracteristica_uno,caracteristica_dos,ordenar)      