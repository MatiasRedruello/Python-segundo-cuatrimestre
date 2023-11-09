import json
ROOT_DIR = r"./SEMANA 9/Ejercicio stark 5/"

def crear_json(ruta:str,modo:str,lista:dict)->None:
    """
    Parametros: Ruta-> Nombre de la ruta donde voy a crear el csv
                Modo-> Modo de apertura del archivo
                Lista -> Contiene la informacion
    Funcion: sobreescribe o crea  un archivo con formato json
    Retorno: None
    """
    with open(ruta,modo,encoding="utf-8") as archivo_json:
        contenido_json = {"lista_heroes":lista}
        json.dump(contenido_json,archivo_json,indent=4)
        print(f"Archivo creado en ruta {ruta}")

def leer_archivo_json(ruta:str,clave:str):
    """
    Parametros: Ruta-> Nombre de la ruta donde voy a crear el json
                Clave-> Str que reprensenta una clave
    Funcion: Abre un archivo json
    Retorno: lista de diccionarios
    """    
    lista_heroes = [] 
    with open (ruta,"r",encoding="utf-8") as archivo:
        lista_heroes = json.load(archivo).get(clave,None)
    return lista_heroes

def crear_categorias(lista_personajes:list[dict],texto:str)->str:
    """
    Parametros: Lista personajes-> Contiene la informacion
                Texto-> Contine uns str
    Funcion: Itera una vez sobre la lista de personajes y guarda en formato str las claves
    Retorno: Un str con las claves
    """    
    for heroe in lista_personajes:
        flag = True
        for clave in heroe.keys():
            if flag:
                texto += f"{clave}"
                flag = False
            else:
                texto += f",{clave}"
        texto += "\n"
        break
    return texto   

def crear_datos_personajes(lista_personajes:list[dict],texto:str)->str:
    """
    Parametros: Lista personajes-> Contiene la informacion
                Texto-> Contine  un str         
    Funcion: Itera  sobre la lista de personajes y guarda en formato str los valores
    Retorno: Un str con  los valores
    """    
    for heroe in lista_personajes:
        flag = True
        for valor in heroe.values():
            if flag:
                texto += f"{valor}"
                flag = False
            else:
                texto += f",{valor}"
        texto += "\n"
    return texto

def guardar_archivo(ruta:str,contenido)->bool:
    """
    Parametros: Ruta-> Nombre de la ruta donde voy a crear el csv
                Contenido-> Informacion que deseo guardar
    Funcion: Crea un archivo csv si no exite y si existe los sobre escribe 
    Retorno: True si lo creo y False en caso contrario
    """    
    with open (ruta,"w+",encoding="utf-8") as archivo:
        try:
            archivo.write(contenido)
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

if __name__=="__main__":
    #crear_json(f"{ROOT_DIR}data_stark.json","w",lista_personajes)
    pass