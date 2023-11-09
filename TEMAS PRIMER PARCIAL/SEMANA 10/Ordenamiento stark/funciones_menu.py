import re
from funciones_base import (pedir_al_usuario,validar_rango,listar_n_heroes,ordenar_heroes,buscar_heroes_por_inteligencia)
from funciones_archivos import (crear_datos_personajes,crear_categorias,guardar_archivo)

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
    imprimir_menu_desafio_5(texto_a = "A- Listar los primeros N heroes",
                            texto_b = "B- Ordenar heroes por altura [Ascendente o Descendente]",
                            texto_c = "C- Ordenar heroes por fuerza [Ascendente o Descendente]",
                            texto_d = "D- Buscar heroes por inteligencia [good, average, high] ",
                            texto_e = "E- Exportar lista Ordenada de heroes ordenada [ASC o DESC] por una clave que decida el usuario a CSV",
                            texto_f = "F- Salir",
                            )
    while True:
            opcion = re.match(r"^[abcdefghijklmnoz]{1}$",input("Elija una opcion"),re.I)
            if opcion:
                break
            else:
                 print(f"Error opcion incorrecta. Elija nuevamente: ")
 
    return opcion.group()

def stark_marvel_app_ordenamiento(lista_personajes:list[dict],path:str)->None:
    """
    Parametro:Opciones-> Lista personajes: Contiene la informacion
    Funcion: Ejecucion principal del programa.
    Retorna: None
    """
    while True:
        match(stark_menu_principal_desafio_5().upper()):
            case "A":
                patron = r"^[1-9]{1,2}$"
                consigna = "Ingrese un numero del 1 al 24: "
                # Valido que lo ingresado cumpla con el RE
                validar_str = pedir_al_usuario(consigna,patron)
                # Validacion adicional para numeros
                validar_rango_numerico = validar_rango(consigna,validar_str,consigna,patron,25,0)
                listar_n_heroes(lista_personajes,validar_rango_numerico)                
            case "B":
                patron = f"^(asc|desc)$"
                consigna = "Vamos a ordenar a los heroes por altura, lo hacemos de forma ascendente(asc) o descendente(desc): "
                respuesta = pedir_al_usuario(consigna,patron)
                ordenar_heroes(lista_personajes,"altura",respuesta)                
            case "C":
                patron = f"^(asc|desc)$"
                consigna = "Vamos a ordenar a los heroes por altura, lo hacemos de forma ascendente(asc) o descendente(desc): "
                respuesta = pedir_al_usuario(consigna,patron)
                ordenar_heroes(lista_personajes,"fuerza",respuesta)                
            case "D":
                patron = f"^(good|average|high)$"
                consigna = "Vamos a filtrar los heroes por tipo de inteligencia good, average, high. Cual Elige?: "
                respuesta = pedir_al_usuario(consigna,patron)
                buscar_heroes_por_inteligencia(lista_personajes,respuesta)                
            case "E":
                # Patrones de validacion
                patron = f"^(asc|desc)$"
                patron_key_valida = f"^(fuerza|altura|peso)$"
                # textos de interaccion con usuario
                consigna_como_ordenar = "Lo hacemos de forma ascendente(asc) o descendente(desc): "
                consigna_key_valida = "Vamos a ordenar a los heroes por la clave que desea,las opciones validas son: fuerza,altura o peso."
                # Valido la palabra ingresada y la retorno de ser correcta.
                respuesta_key_valida = pedir_al_usuario(consigna_key_valida,patron_key_valida)
                respuesta_como_ordenar = pedir_al_usuario(consigna_como_ordenar,patron)
                # Ordeno heroes
                lista_personajes_ordenada = ordenar_heroes(lista_personajes,respuesta_key_valida,respuesta_como_ordenar)     
                # Armo formato y guado en csv
                texto_a =""  
                texto_b = crear_categorias(lista_personajes_ordenada,texto_a)
                texto_f = crear_datos_personajes(lista_personajes_ordenada,texto_b)
                guardar_archivo(f"{path}heroes_{respuesta_key_valida}.csv",texto_f)
            case "F":
                break
                                                                                              


