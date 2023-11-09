from clase_estadisiticas import Estadisticas
from clase_equipo import EquipoDreamTeam
from funcion_ordenamiento import quick_sort,quick_sort_suma_estadisticas
class JugadorDreamTeam():
    def __init__(self) -> None:
        self.lista_logros = []
        self.nombre = None
        self.posicion = None
        self.equipo = EquipoDreamTeam()
        
    "1)"
    def lista_jugador_posicion(self)->None:
        """
        Parametros:
            self-> Defecto
        funcion: Busca el nombre y la posicion de juego del jugador y la muestra con el formato (Nombre Jugador - Posición)
        Retorno: None
        """
        # Verificar si la lista está vacía
        if len(self.equipo.jugadores_lista) == 0:  
            return print("La lista esta vacia")
        # < izquierda - < derecha
        print(f"{'Nombre Jugador':<20} {'Posicion':<15}")
        print("="*50)  # Línea separadora
        for jugadores in self.equipo.jugadores_lista:
            print(f"{jugadores.get('nombre'):<20} {jugadores.get('posicion'):<15}")    
                

    "2)"
    def diccionario_del_jugador_por_indice(self,indice_ususario:str,lista:list[dict])->dict:
        """
        Parametros: Self-> Defecto
                    Indice ususario-> numero de la ubicacion del jugador
                    lista -> Contiene la informacion de los jugadores
        funcion: Con el indice pasado por parametros busco al jugador y devuelvo su informacion
        Retorno: Diccionario con la informacion del jugador
        """        
        for indice in range(len(lista) +1): #+1 necesito que tomo el ultimo jugador
            if indice == int(indice_ususario):
                # el -1 al idice es para que lo jugadores tengan inn¡dice 1 a 12 y no 0 a 11
                return lista[indice -1]

    def mostrar_estadisticas(self,indice_ususario:int,lista:list[dict])->None:
        """
        Parametros: Self-> Defecto
                    Indice ususario-> El indice pasado por parametros se va utilizar como argumento de otra funcion.
                    lista -> Contiene la informacion de los jugadores
        funcion: Arma un formato y muestra las estadisticas de un jugador
        Retorno: None
        """        
        diccionario = JugadorDreamTeam().diccionario_del_jugador_por_indice(indice_ususario,lista)
        estadisticas = diccionario.get("estadisticas")
        print(f"{diccionario.get('nombre')}")
        for clave,valor in estadisticas.items():    
            print(f"{clave.replace('_',' ').capitalize()}: {valor} ")

    "3)"
    def guardar_jugador_en_csv(self,diccionario_jugador,nombre_jugador:str)->None:
        """
        Parametros: Self-> Defecto
                    Diccionario jugador -> informacion de un jugador
        funcion: usa la informacion del jugador como argumento de otra funcion la cual lo crear o sobresescibe en formato csv
        Retorno: None
        """          
        return self.equipo.guardar_archivo_csv(diccionario_jugador,nombre_jugador)
    
    "4)"
    def diccionario_del_jugador_por_nombre(self,nombre:str)->list[dict]:
        """
        Parametros: Self-> Defecto
                    Nombre -> El nombre de un jugador del Dream Team que se busca
        funcion: Con el metodo filter le paso la forma de filtrado y la lista a filtrar y me devulve lo que se filtro
        Retorno: La lista con el diccionario del jugador
        """        
        jugador_filtrado = list(filter(lambda jugador: jugador.get("nombre") == nombre,self.equipo.jugadores_lista))       
        return jugador_filtrado
    
    def mostrar_logros(self,nombre)->None:
        """
        Parametros: Self-> Defecto
                    Nombre -> Nombre del jugador que va a ser argumento de otra funcion que se encarga de buscarlo
        funcion: Arma un formato y muestra los logros del jugador
        Retorno: None
        """         
        lista_jugador = JugadorDreamTeam().diccionario_del_jugador_por_nombre(nombre)
        diccionario_jugador = lista_jugador[0]
        logros = diccionario_jugador.get("logros")
        print(f"{diccionario_jugador.get('nombre')}")
        for logro in logros:    
            print(f"{logro}")        
    "5)"
    def suma(self)->float:
        """
        Parametros: Self-> Defecto
        funcion: Suma los promedios de puntos por partido de tdos los jugadores
        Retorno: Numero con coma ue reprenseta la suma total del promedio de los putnos por aprtidos
        """         
        resultado_suma = 0
        diccionario_jugadores = self.equipo.jugadores_lista
        for jugador in diccionario_jugadores:
            for clave,valor in jugador.get("estadisticas").items():
                if clave == "promedio_puntos_por_partido":
                    resultado_suma += valor 
                
        return resultado_suma
    
    def divicion(self)->int:
        """
        Parametros: Self-> Defecto
        funcion: Mediante el metodo len averiguo cuantos diccionarios hay en la lista, ergo se cuando jugadores hay
        Retorno: cantidad de jugadores
        """      
        try:   
            diccionario_jugadores = self.equipo.jugadores_lista
            cantidad_jugadores = len(diccionario_jugadores)
        except IndexError as type_eror:
            print(f"{type_eror} La lista esta vacia")
        else:
            return cantidad_jugadores
    
    def promedio_puntos_partidos(self)->float: 
        """
        Parametros: Self-> Defecto
        funcion: Calcula el promedio de puntos por partido
        Retorno: El proemdio
        """ 
        try:
            promedio = 0
            dividendo = JugadorDreamTeam()
            divisor = JugadorDreamTeam()
            promedio = dividendo.suma()/divisor.divicion()
        except ZeroDivisionError as type_error:
            print(f"{type_error} No ce puede dividir por cero")
        else:
            return promedio
    def ordenar_jugadores_por_caracteristica(self,lista:list[dict],caracteristica:str,ordenar=False):
        """
        Parametros:
            Parametros: Self-> Defecto
            lista: Informacion que quiero ordenar
            caracteristicas-> La caracteristica por la cual se ordena
            Ordenar-> Como lo voy a ordenar. False ascendente True descendente
        Funcion: Ordena a los heroes segun la caracteristica pedida y un orden
        Retorno:lista ordenada
        """   
        #sort() modifica la lista original
        #sorted() crea una lista ordenada
        #FUNCION SORTED() 
        """diccionario_jugadores = lista
        if not ordenar:
            jugadores_ordenados = sorted(diccionario_jugadores, key=lambda jugador: jugador["estadisticas"][caracteristica])
        elif ordenar:
            jugadores_ordenados = sorted(diccionario_jugadores, key=lambda jugador: jugador["estadisticas"][caracteristica],reverse=True)"""
        # para poder usar la recursividad en la funcion  necesito crear la clase

        #quick sort
        jugadores_ordenados = quick_sort(lista,caracteristica,ordenar)        
        return jugadores_ordenados

    def jugadores_ordenados_por_caracteristicas(self,lista:list[dict],caracteristica:str,ordenar=False)->None:
        """
        Parametros:
            Parametros: Self-> Defecto
            lista: Informacion que quiero ordenar
            caracteristicas-> La caracteristica pasado por parametro va a ser argumento de la funcion que ordena los jugadores
            Ordenar-> El orden pasado por parametro va a ser argunmento de la funcion que ordena a los jugadores
        Funcion: Arma un formato y muestra a los jugadores de forma ordenada
        Retorno:None
        """         
        clase_jugador = JugadorDreamTeam()
        diccionario = clase_jugador.ordenar_jugadores_por_caracteristica(lista,caracteristica,ordenar)
        print(f"{'Nombre Jugador':<20} {caracteristica:<15}")
        print("="*50)  # Línea separadora
        for jugadores in diccionario:
            print(f"{jugadores.get('nombre'):<30}{jugadores['estadisticas'][caracteristica]:<30}")            

    "6)"
    def hall_of_fame(self,nombre:str)->None:
        """
        Parametros: Self-> Defecto
                    Nombre -> Nombre del jugador que va a ser argumento de otra funcion que se encarga de buscarlo
        funcion: Muestra si el jugador pertenece:"Miembro del Salon de la Fama del Baloncesto"
        Retorno: None
        """        
        clase_jugador = JugadorDreamTeam()
        diccionario_jugador = clase_jugador.diccionario_del_jugador_por_nombre(nombre)
        diccionario_jugador[0]["nombre"]
        if "Miembro del Salon de la Fama del Baloncesto" in diccionario_jugador[0]["logros"]:
            print(f"El jugador {diccionario_jugador[0]['nombre']} es miembro del Salon de la Fama del Baloncesto") 
        else:
            print(f"El jugador {diccionario_jugador[0]['nombre']} no es miembro del Salon de la Fama del Baloncesto")
    "8)"
    def guardar_en_json(self,ruta,lista:list[dict])->None:
        """
        Parametros: Self-> Defecto
                    Ruta -> Lugar donde voy a guardar el json
                    Lista-> INformacion de jugadores
        Funcion: Llama  a la funcion crear json y la retorna, con lo cual se guarda el archivo con ese formato
        Retorno: Funcion
        """         
        return self.equipo.crear_json(ruta,lista)
    "8 bis)"
    # accedo a la funcion crear sql
    def acceder__crear_base_datos_sql(self,ruta)->None:
        """
        Parametros: Self-> Defecto
                    Ruta -> Lugar donde voy a guardar el json
        Funcion: Llama  a la funcion Crear base de datos y la retorna, con lo cual crea el archivo con ese formato
        Retorno: Funcion
        """         
        return self.equipo.crear_base_datos_sql(ruta)
    #inserto informacion en la base de datos
    def guardar_en_sql(self,ruta,lista:list[dict])->None:
        """
        Parametros: Self-> Defecto
                    Ruta -> Lugar donde voy a insertar la informacion
                    Lista-> Informacion de jugadores
        Funcion: Llama  a la funcion informacion tabla sql y la retorna, con lo cual se guarda el archivo con ese formato
        Retorno: Funcion
        """         
        return self.equipo.informacion_tabla_sql(ruta,lista)
    "9)"
    def suma_entre_estadisticas(self,diccionario_jugador:dict,estadistica_uno:str,estadistica_dos:str)->float:
        """
        Parametros: Self-> Defecto
                    Diccionario_jugador-> Contiene la informacion de un jugador
                    Estadistica uno-> Es parte de las claves de estadisticas
                    Estadistica dos-> Es parte de las claves de estadisticas
        funcion: Suma entre si dos estadisitcas
        Retorno: Resultado de la suma
        """         
        resultado_suma = 0
        resultado_suma = diccionario_jugador["estadisticas"][estadistica_uno] + diccionario_jugador["estadisticas"][estadistica_dos]         
        return resultado_suma  
    
    def valor_maximo(self,lista:list[dict],estadistica_uno:str,estadistica_dos:str)->float:
        """
        Parametros: Self-> Defecto
                    Lista-> Contiene la informacion de un jugador
                    Estadistica uno-> Es parte de las claves de estadisticas
                    Estadistica dos-> Es parte de las claves de estadisticas
        funcion: Busca el valor maximo de todos los las sumas
        Retorno: El valor maximo
        """
        valor_maximo = 0
        jugador_clase = JugadorDreamTeam()
        for jugador in lista:
            resultado_suma = jugador_clase.suma_entre_estadisticas(jugador,estadistica_uno,estadistica_dos)
            if resultado_suma > valor_maximo:
                valor_maximo = resultado_suma
                
        return valor_maximo
    
    def porcentaje_de_la_suma(self,resultado_maximo:float,resultado_suma:float)->float:
        """
        Parametros: Self-> Defecto
                    Resultado maximo-> Contiene el valor mas alto
                    Resultado suma-> Contiene el valor de la suma
        funcion: Calcula los valores equivalentes en porcentaje
        Retorno: Valor que representa el porcentaje
        """        
        # resultado suma maximo ----100%
        #    resultado suma ------- ?
        resultado_porcentaje = resultado_suma * 100/ resultado_maximo
        return resultado_porcentaje


    def filtrar_n_jugadores(self,indice_ususario:str,lista:list[dict])->dict:
        """
        Parametros: Self-> Defecto
                    Indice ususario-> muestro los jugadores menores o iguales a ese numero
                    lista -> Contiene la informacion de los jugadores
        funcion: Con el indice pasado por parametro busco los jugadores menores o iguales a ese valor
        Retorno: Lista con los diccionarios menores o iguales al indice
        """    
        return lista[0:int(indice_ususario)]        


    def jugadores_ordenados_por_suma_estadisticas(self,lista:list[dict],estadistica_uno:str,estadistica_dos:str,ordenar:bool = False):
        """
        Parametros: Self-> Defecto
                    Lista-> Contiene la informacion de un jugador
                    Cara-> Es parte de las claves de estadisticas
                    Estadistica dos-> Es parte de las claves de estadisticas
                    Orden-> Como quiero ordenar, tiene valor falce por defecto
        funcion: Llama  a una variante de la funcion sort y ordena los jugadores
        Retorno: Lista de diccioanrios ordenados
        """        
        jugadores_ordenados = quick_sort_suma_estadisticas(lista,estadistica_uno,estadistica_dos,ordenar)
        return jugadores_ordenados
    
    def mostrar_jugadores_ordenados_por_porcentaje_de_suma_estadisticas(self,lista:list[dict],estadistica_uno:str,estadistica_dos:str,ordenar:str = False)->None:
        """
        Parametros: Self-> Defecto
                    Lista-> Contiene la informacion de un jugador
                    Cara-> Es parte de las claves de estadisticas
                    Estadistica dos-> Es parte de las claves de estadisticas
                    Orden-> Como quiero ordenar, tiene valor falce por defecto
        funcion: Muestra por pantalla los jugadores con la estaditica pediida y su porcentaje
        Retorno: None
        """         
        clase_jugador = JugadorDreamTeam()
        #ordeno jugadores
        jugadores_ordenados = clase_jugador.jugadores_ordenados_por_suma_estadisticas(lista,estadistica_uno,estadistica_dos,ordenar)   
        print(f"{'Nombre Jugador':<20} {estadistica_uno.capitalize().replace('_',' ')} + {estadistica_dos.capitalize().replace('_',' '):<30} {'porcentaje'.capitalize():<15}")
        print("="*90)  # Línea separadora
        #Obtengo el porcentaje en relacion a la suma de estadisiticas
        resultado_valor_maximo = clase_jugador.valor_maximo(jugadores_ordenados,estadistica_uno,estadistica_dos)
        for jugadores in jugadores_ordenados:       
            resultado_suma_estadisticas = clase_jugador.suma_entre_estadisticas(jugadores,estadistica_uno,estadistica_dos)
            resultado_porcentaje_suma = clase_jugador.porcentaje_de_la_suma(resultado_valor_maximo,resultado_suma_estadisticas)
            print(f"{jugadores.get('nombre'):<30}{resultado_suma_estadisticas:<40}{round(resultado_porcentaje_suma,2)}%")
    
    "10)"
    def guardar_jugador_posicion_en_csv(self,diccionario_jugador,nombre_jugador:str)->None:
        """
        Parametros: Self-> Defecto
                    Diccionario jugador -> informacion de un jugador
        funcion: usa la informacion del jugador como argumento de otra funcion la cual lo crear o sobresescibe en formato csv
        Retorno: None
        """          
        return self.equipo.guardar_archivo_posiciones_csv(diccionario_jugador,nombre_jugador)    
    ##########################################
    # con sqlite
    def acceder_crear_base_datos_posiciones_sql(self,ruta)->None:
        """
        Parametros: Self-> Defecto
                    Ruta -> Lugar donde voy a guardar el json
        Funcion: Llama  a la funcion Crear base de datos y la retorna, con lo cual crea el archivo con ese formato
        Retorno: Funcion
        """         
        return self.equipo.crear_base_datos_posiciones_sql(ruta)
    #inserto informacion en la base de datos
    def guardar_posiciones_en_sql(self,ruta,lista:list[dict])->None:
        """
        Parametros: Self-> Defecto
                    Ruta -> Lugar donde voy a insertar la informacion
                    Lista-> Informacion de jugadores
        Funcion: Llama  a la funcion informacion tabla sql y la retorna, con lo cual se guarda el archivo con ese formato
        Retorno: Funcion
        """         
        return self.equipo.informacion_tabla_posiciones_sql(ruta,lista) 
      
if __name__=="__main__":
    jugador = JugadorDreamTeam()
    lista = jugador.equipo.jugadores_lista
    print(jugador.filtrar_n_jugadores(2,lista))
    