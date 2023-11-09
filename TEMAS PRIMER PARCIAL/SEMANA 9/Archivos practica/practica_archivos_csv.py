from data_stark import lista_personajes
import re
ROOT_DIR = r"./SEMANA 9/Archivos practica/"


def crear_csv_beta(ruta:str,modo:str,lista_personajes:list[dict])->None:
    with open (ruta,modo,encoding="utf-8") as archivo :
        texto = ""
        for heore in lista_personajes:
            primera_linea = True
            for clave in heore.keys():
                if primera_linea:
                    texto += f"{clave}"
                    primera_linea = False
                else:
                    texto += f",{clave}"
            texto += "\n"
            # el break es par romper en la primera iteracion,si no me escribe las claves por cada heroe
            break
        archivo.write(texto)
        texto = ""
        for heore in lista_personajes:
            primera_linea = True
            for valor in heore.values():
                if primera_linea:
                    texto += f"{valor}"
                    primera_linea = False
                else:
                    texto += f",{valor}"
            texto += "\n"
        archivo.write(texto)     

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

def crear_csv_alfa(lista_personajes:list[dict],ruta:str,modo:str)-> None:
    """
    Parametros: Lista personajes-> Contiene la informacion
                Ruta-> Nombre de la ruta donde voy a crear el csv
                Modo-> Modo de apertura del archivo
    Funcion: sobreescribe o crea  un archivo con formato csv
    Retorno:
    """    
    with open(ruta,modo,encoding="utf-8") as archivo:
        texto = ""
        texto = crear_categorias(lista_personajes,texto)
        texto = crear_datos_personajes(lista_personajes,texto)
        archivo.write(texto)

def leer_csv(ruta:str,modo:str)->list[dict]:
    """
    Parametros: Ruta-> Nombre de la ruta donde voy a crear el csv
                Modo-> Modo de apertura del archivo
    Funcion: lee  un archivo con formato csv y arma un lista de diccionarios
    Retorno: lista con los diccionarios de cada heroe
    """    
    lista_de_heroes = []
    with open(ruta,modo,encoding="utf-8") as archivo:
         # leo las lineas de csv y las guardo en formato lista
        lista_de_renglones = archivo.readlines()
        # guardo la primer linea que contiene las claves, sanitizo y le doy formato lista c/palabra
        lista_de_claves = lista_de_renglones[0].replace("\n","").split(",")
        # recorro la lista heroes,con formato renglon,son str
        for heroe in lista_de_renglones[1:]:
            # guardo la  linea que contiene los heroes, sanitizo y le doy formato lista c/palabra
            lista_de_valores = heroe.replace("\n","").split(",")
            # dict comprenhension: lista paralelas, armo par clave-valor por c/heroe 
            diccionario_heroe = {lista_de_claves[i]:lista_de_valores[i] for i in range(len(lista_de_valores))} 
            # apendeo los diccionarios a la lista
            lista_de_heroes.append(diccionario_heroe)
    return lista_de_heroes

if __name__ == "__main__":
    #crear_csv_beta(f"{ROOT_DIR}data_stark_beta.csv","w",lista_personajes)
    #crear_csv_alfa(lista_personajes,f"{ROOT_DIR}data_stark_alfa.csv","w")
    lista_nueva_heroes = leer_csv(f"{ROOT_DIR}data_stark_alfa.csv","r")
    DESTINO_CSV = f"{ROOT_DIR}heroes_f.csv"
    heroes_femeninos = list(filter(lambda heroeina: heroeina.get("genero","none")=="F",lista_nueva_heroes))
    
#crear_csv_alfa(heroes_femeninos,DESTINO_CSV,"w")

