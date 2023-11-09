import json
from constantes_examen import (PATH_JSON,PATH_CSV)
import sqlite3
class EquipoDreamTeam():
    def __init__(self) -> None:
        self._ruta_archivo_json = PATH_JSON
        self._ruta_archivo_csv = PATH_CSV
        self.jugadores_lista = EquipoDreamTeam.leer_json(self).copy() 
        
    # La idea es que si quieren cambiar la ruta se haga de forma controlada
    @property
    def ruta_archivo_json(self):
        return self._ruta_archivo_json
    @property
    def ruta_archivo_csv(self):
        return self._ruta_archivo_csv


    @ruta_archivo_json.setter
    def ruta_archivo_json(self,nueva_ruta):
        self._ruta_archivo_json = nueva_ruta
        return self._ruta_archivo_json    

    @ruta_archivo_csv.setter
    def ruta_archivo_csv(self,nueva_ruta):
        self._ruta_archivo_csv = nueva_ruta
        return self._ruta_archivo_csv


    
    def leer_json(self) -> list[dict]:
        """
        Parametros: self-> 
        Funcion: Abre un archivo json
        Retorno: lista de diccionarios
        """         
        try:
            with open(self._ruta_archivo_json, "r", encoding="utf-8") as archivo:
                archivo_cargado = json.load(archivo)["jugadores"]
            return archivo_cargado
        except FileNotFoundError as type_error:
            # Manejar la excepción de archivo no encontrado
            print(f"{type_error} El archivo JSON no se encontró en la ubicación especificada.")
            return []
        except PermissionError as type_error:
            # Manejar la excepción de permisos insuficientes
            print(f"{type_error} No tienes permisos para acceder al archivo JSON.")
            return []
        except json.JSONDecodeError as  type_error:
            # Manejar la excepción de formato JSON inválido
            print(f"{type_error} El archivo JSON no tiene un formato válido.")
            return []
        except UnicodeDecodeError as type_error:
            # Manejar la excepción de decodificación de caracteres
            print(f"{type_error} Error al decodificar el archivo con la codificación utf-8.")
            return []
    
    def crear_json(self,ruta:str,lista:list)->None:
        """
        Parametros: Ruta-> Nombre de la ruta donde voy a crear el csv
                    Modo-> Modo de apertura del archivo
                    Lista -> Contiene la informacion
        Funcion: sobreescribe o crea  un archivo con formato json
        Retorno: None
        """
        with open(ruta,"w",encoding="utf-8") as archivo_json:
            contenido_json = {"Dream Team":lista}
            json.dump(contenido_json,archivo_json,indent=4)
            print(f"Archivo creado en ruta {ruta}") 

    def crear_categorias_csv(self,diccionario_jugador:dict,texto:str)->str:
        """
        Parametros: Diccionario jugador-> Contiene la informacion
                    Texto-> Contine uns str
                    flag-> Booleano que indica si se
        Funcion: Itera  sobre el diccionario de un jugador y guarda en formato str las claves
                 NOTA: Los diccionarios de un personaje pasarlos dentro de una lista.
        Retorno: Un str con las claves
        """    
        flag_primer_dato = True
        for jugador in diccionario_jugador:    
            for claves in jugador.get("estadisticas"):      
                if flag_primer_dato:
                    texto += f"Nombre,{claves.capitalize().replace('_',' ')}"
                    flag_primer_dato = False
                else:
                    texto += f",{claves.capitalize().replace('_',' ')}"
            texto += "\n"            
            break
        return texto 
    def crear_datos_personajes_csv(self,diccionario_jugador:dict,texto:str)->str:
        """
        Parametros: Diccionario jugador-> Contiene la informacion
                    Texto-> Contine  un str         
        Funcion: Itera  sobre el diccionario de un jugador y guarda en formato str los valores
                 NOTA: Los diccionarios de un personaje pasarlos dentro de una lista.
        Retorno: Un str con  los valores
        """
        for jugador in diccionario_jugador:
            texto += f"{jugador['nombre']}"
            for valor in jugador.get("estadisticas").values():
                    texto += f",{valor}"
            texto += "\n"        
                
        return texto

               
    def guardar_archivo_csv(self,diccionario_jugador:dict,nombre_jugador:str)->bool:
        """
        Parametros: Diccionario jugador-> Informacion del jugador
        Funcion: Crea un archivo csv si no exite y si existe los sobre escribe 
        Retorno: True si lo creo y False en caso contrario
        """
        # creo la ruta
        path = self._ruta_archivo_csv 
        ruta = f"{path}{nombre_jugador}.csv"
        # creo el contenido
        texto = ""
        contenido = EquipoDreamTeam()
        texto_categorias = contenido.crear_categorias_csv(diccionario_jugador,texto)
        texto_final = contenido.crear_datos_personajes_csv(diccionario_jugador,texto_categorias)
           
        with open (ruta,"w+",encoding="utf-8") as archivo:
            try:
                archivo.write(texto_final)
            except PermissionError as type_error:
                print(f"Error {type_error} al crear el archivo: {ruta}")
            except FileNotFoundError as type_error:
                print(f"Error {type_error} al crear el archivo: {ruta}")
            except IsADirectoryError as type_error: 
                print(f"Error {type_error} al crear el archivo: {ruta}")
            except NotADirectoryError as type_error:
                print(f"Error {type_error} al crear el archivo: {ruta}")
            except FileExistsError as type_error:
                print(f"Error {type_error} al crear el archivo: {ruta}")
            else:
                print(f"Se creó el archivo: {ruta}")
                return True            
        return False
    
    def crear_base_datos_sql(self,ruta)->None:
        """
        Parametros: Self->defecto
                    ruta-> Donde voy a crear el archivo
        Funcion: Crea una base de datos.
        Retorna: None
        """
        try:
            with sqlite3.connect(f"{ruta}") as conexion:
                sentencia = f"""CREATE TABLE personajes (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                temporadas INTEGER,
                puntos_totales INTEGER,
                promedio_puntos_por_partido REAL,
                rebotes_totales INTEGER,
                promedio_rebotes_por_partido REAL,
                asistencias_totales INTEGER,
                promedio_asistencias_por_partido REAL,
                robos_totales INTEGER,
                bloqueos_totales INTEGER,
                porcentaje_tiros_de_campo REAL,
                porcentaje_tiros_libres REAL,
                porcentaje_tiros_triples REAL
                )"""
            conexion.execute(sentencia)
            print(f"Se creó el archivo: {ruta}")

        except sqlite3.IntegrityError as type_error:
            print(f"Error {type_error} al crear el archivo: {ruta}")
        except sqlite3.OperationalError as type_error:
            print(f"Error {type_error} al crear el archivo: {ruta}")
  


    def insertar_tabla_sql(self,ruta,nombre_jugador,informacion:dict)->None:
        """
        Parametros: Self->defecto
                    Ruta-> Donde voy a insetar las tablas
                    Nombre jugador-> Es uno de los aprametros de la tabla
                    informacion-> lo que voy a guardar en la tabla
        Funcion: Inserta una tabla
        Retorna: None
        """
        try:
            with sqlite3.connect(f"{ruta}") as conexion:
                sentencia = f"""INSERT INTO personajes (
                nombre,
                temporadas,
                puntos_totales,
                promedio_puntos_por_partido,
                rebotes_totales,
                promedio_rebotes_por_partido,
                asistencias_totales,
                promedio_asistencias_por_partido,
                robos_totales,
                bloqueos_totales,
                porcentaje_tiros_de_campo,
                porcentaje_tiros_libres,
                porcentaje_tiros_triples) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                valores = (
                    nombre_jugador,
                    informacion["temporadas"],
                    informacion["puntos_totales"],
                    informacion["promedio_puntos_por_partido"],
                    informacion["rebotes_totales"],
                    informacion["promedio_rebotes_por_partido"],
                    informacion["asistencias_totales"],
                    informacion["promedio_asistencias_por_partido"],
                    informacion["robos_totales"],
                    informacion["bloqueos_totales"],
                    informacion["porcentaje_tiros_de_campo"],
                    informacion["porcentaje_tiros_libres"],
                    informacion["porcentaje_tiros_triples"]
                )
                conexion.execute(sentencia, valores) 
                print(f"Se agregaron datos del jugador {nombre_jugador} ") 
        except sqlite3.IntegrityError as type_error:
            print(f"Error {type_error} al intentar insertar informacion: {ruta}")
        except sqlite3.ProgrammingError as type_error:
            print(f"Error {type_error} al intentar insertar informacion: {ruta}")
        except sqlite3.DatabaseError as type_error:
            print(f"Error {type_error} al intentar insertar informacion: {ruta}")
  
   
    def informacion_tabla_sql(self,ruta,lista:list[dict])->None:
        """
        Parametros: Self->defecto
                    Ruta-> Donde voy a insetar las tablas
                    lista-> Contiene la informacion que voy a guardar en el sql
        Funcion: Itero la lista pra obtener la informacion que necesito e insertarla en la tabla
        Retorna: None
        """        
        for jugador in lista:
            nombre_jugador = jugador.get("nombre")
            estadisticas = jugador.get("estadisticas")
            jugador_clase = EquipoDreamTeam()
            jugador_clase.insertar_tabla_sql(ruta,nombre_jugador,estadisticas)
        print("Se agrego la informacion a la tabla")

    "10)"

    def crear_posicion_csv(self,diccionario_jugador:dict,texto:str)->str:
        """
        Parametros: Diccionario jugador-> Contiene la informacion
                    Texto-> Contine uns str
                    flag-> Booleano que indica si se
        Funcion: Itera  sobre el diccionario de un jugador y guarda en formato str las claves
                 NOTA: Los diccionarios de un personaje pasarlos dentro de una lista.
        Retorno: Un str con las claves
        """    
        flag_primer_dato = True
        for jugador in diccionario_jugador:   
            for key in jugador.keys():
                if key == "posicion":
                    if flag_primer_dato:
                        texto += f"{'posicion'.capitalize()}"
                        flag_primer_dato = False
                    else:
                        texto += f",posicion"
            texto += "\n"            
            break
        return texto 
    def crear_datos_jugadores_posiciones_csv(self,diccionario_jugador:dict,texto:str)->str:
        """
        Parametros: Diccionario jugador-> Contiene la informacion
                    Texto-> Contine  un str         
        Funcion: Itera  sobre el diccionario de un jugador y guarda en formato str los valores
                 NOTA: Los diccionarios de un personaje pasarlos dentro de una lista.
        Retorno: Un str con  los valores
        """
        lista_aux = []
        for jugador in diccionario_jugador:
            for clave,valor in jugador.items():
                if valor not in lista_aux and clave == "posicion":
                    lista_aux.append(valor)
                    texto += f"{valor}"
                    texto += "\n"                
        return texto

               
    def guardar_archivo_posiciones_csv(self,diccionario_jugador:dict,nombre_jugador:str)->bool:
        """
        Parametros: Diccionario jugador-> Informacion del jugador
        Funcion: Crea un archivo csv si no exite y si existe los sobre escribe 
        Retorno: True si lo creo y False en caso contrario
        """
        # creo la ruta
        path = self._ruta_archivo_csv 
        ruta = f"{path}{nombre_jugador}.csv"
        # creo el contenido
        texto = ""
        contenido = EquipoDreamTeam()
        texto_categorias = contenido.crear_posicion_csv(diccionario_jugador,texto)
        texto_final = contenido.crear_datos_jugadores_posiciones_csv(diccionario_jugador,texto_categorias)
           
        with open (ruta,"w+",encoding="utf-8") as archivo:
            try:
                archivo.write(texto_final)
            except PermissionError as type_error:
                print(f"Error {type_error} al crear el archivo: {ruta}")
            except FileNotFoundError as type_error:
                print(f"Error {type_error} al crear el archivo: {ruta}")
            except IsADirectoryError as type_error: 
                print(f"Error {type_error} al crear el archivo: {ruta}")
            except NotADirectoryError as type_error:
                print(f"Error {type_error} al crear el archivo: {ruta}")
            except FileExistsError as type_error:
                print(f"Error {type_error} al crear el archivo: {ruta}")
            else:
                print(f"Se creó el archivo: {ruta}")
                return True            
        return False
    "10)"
    def crear_base_datos_posiciones_sql(self,ruta)->None:
        """
        Parametros: Self->defecto
                    ruta-> Donde voy a crear el archivo
        Funcion: Crea una base de datos.
        Retorna: None
        """
        try:
            with sqlite3.connect(f"{ruta}") as conexion:
                sentencia = f"""CREATE TABLE personajes (
                posicion TEXT
                )"""
            conexion.execute(sentencia)
            print(f"Se creó el archivo: {ruta}")

        except sqlite3.IntegrityError as type_error:
            print(f"Error {type_error} al crear el archivo: {ruta}")
        except sqlite3.OperationalError as type_error:
            print(f"Error {type_error} al crear el archivo: {ruta}")
  


    def insertar_tabla_posiciones_sql(self,ruta,posicion:dict)->None:
        """
        Parametros: Self->defecto
                    Ruta-> Donde voy a insetar las tablas
                    Nombre jugador-> Es uno de los aprametros de la tabla
                    informacion-> lo que voy a guardar en la tabla
        Funcion: Inserta una tabla
        Retorna: None
        """
        
        with sqlite3.connect(f"{ruta}") as conexion:
            sentencia = f"""INSERT INTO personajes (
            posicion,
            posicion,
            posicion,
            posicion,
            posicion
            ) VALUES (?, ?, ?, ?, ?)"""
            valores = (
                posicion,
                posicion,
                posicion,
                posicion,
                posicion
            )
            conexion.execute(sentencia,valores)  

  
   
    def informacion_tabla_posiciones_sql(self,ruta,lista:list[dict])->None:
        """
        Parametros: Self->defecto
                    Ruta-> Donde voy a insetar las tablas
                    lista-> Contiene la informacion que voy a guardar en el sql
        Funcion: Itero la lista pra obtener la informacion que necesito e insertarla en la tabla
        Retorna: None
        """
        jugador_clase = EquipoDreamTeam()       
        lista_aux = [] 
        for jugador in lista:
            for clave,valor in jugador.items():
                if valor not in lista_aux and clave == "posicion":
                    print(valor)
                    lista_aux.append(valor)
                    jugador_clase.insertar_tabla_posiciones_sql(ruta,valor)
        print("Se agrego la informacion a la tabla")



     

    

    
if __name__ =="__main__":
    pass
    
    
