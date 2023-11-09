from practica_archivos_csv import crear_csv_alfa,leer_csv,ROOT_DIR
import json

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

def leer_json(ruta:str,modo:str,clave:str)->list[dict]:
    """
    Parametros: Ruta-> Nombre de la ruta donde voy a crear el csv
                Modo-> Modo de apertura del archivo
    Funcion: Abre un archivo json
    Retorno: lista de diccionarios
    """    
    lista_del_archivo = []
    with open(ruta,modo) as archivo_json:
        lista_del_archivo = json.load(archivo_json).get(clave,"Diccionario vacio")
    return lista_del_archivo