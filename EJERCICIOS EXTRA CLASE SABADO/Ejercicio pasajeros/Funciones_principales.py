from Funciones_base import (suma,promedio_edades,edad_mas_comun,actualizar_json,buscar_pasajero,pedir_un_dato,imprimir_dato,pedir_datos,
                            ruta_pasajeros_json,informacio_pasajeros_normalizada,lista_de_claves)
import re
def agregar_pasajero(diccionario:dict[list[dict]])->None:
    """
    Parametro: Lista-> La lista con los pasajeros.
    Funcion: Agrega a la lista de pasajeros el nuevo pasajero.
    Retorna: None
    """
    while True:
        try:
            pregunta_pasajero = re.match(r"si|no",input("Agregamos un nuevo pasajero: Si/No"),re.I).group()
            if pregunta_pasajero == "si":
                #la idea es agregar el pasajero a la lista,borrar la anterior y actualizarla. TIENE QUE HABER UNA FORMA MAS EFICIENTE.
                nuevo_pasajero = pedir_datos()
                diccionario["lista_pasajeros"].append(nuevo_pasajero)
                actualizar_json(ruta_pasajeros_json,"w",diccionario)
                continue
            else:
                break
        except AttributeError as que_error:
            print(f"Error {que_error},esta ingresando mal los datos, vuelva a ingresarlo: ")        
    
def modificar_datos_pasajeros(diccionario:dict[list[dict]])->None:
    """
    Parametro: Lista-> La lista con los pasajeros.
    Funcion: Busca y modifica la informacion de un pasajero.
    Retorna: None
    """
    while True:
        #pido el nombre del pasajero al que le hago la modificacion
        id_pasajero = pedir_un_dato("Ingrese el nombre de psajero que debemos actualizar los datos")
        #pido la clave del  dato quequiero cambiar
        dato_a_modificar = pedir_un_dato("¿Que desea modificar?")
        dato_a_modificar = dato_a_modificar.lower().capitalize()        
        pasajero = buscar_pasajero(diccionario,id_pasajero.lower().capitalize())
        if pasajero not in diccionario["lista_pasajeros"] or dato_a_modificar not in lista_de_claves: 
            print("El pasajero ingresado no esta en la lista o el dato es incorrecto,fijese de ingresar correctametne lo pedido")
            continue    
        else:         
            #pido la modificacion que quiero hacer
            modificacion = pedir_un_dato(f"Vamos a modificar {dato_a_modificar},¿cual es el nuevo valor?")
            pasajero[dato_a_modificar] = modificacion
            actualizar_json(ruta_pasajeros_json,"w",diccionario)
            break

def borrar_pasajero(diccionario:dict[list[dict]])->None:
    """
    Parametro: Diccionario-> Contiene la informacion de los pasajeros
    Funcion: Busca y borrar la informacion de un pasajero.
    Retorna: None
    """
    while True:
        id_pasajero = pedir_un_dato("Ingrese el nombre de psajero que debemos borrar los datos")
        pasajero = buscar_pasajero(diccionario,id_pasajero.lower().capitalize())
        if pasajero not in diccionario["lista_pasajeros"]: 
            print("El pasajero ingresado no esta en la lista o el dato es incorrecto,fijese de ingresar correctametne lo pedido")
            continue    
        else:         
            diccionario["lista_pasajeros"].remove(pasajero)
            actualizar_json(ruta_pasajeros_json,"w",diccionario)
            break

def mostrar_lista_pasajeros(diccionario:dict[list[dict]])->None:
    """
    Parametro: Diccioanrio-> Contiene la informacion de los pasajeros
    Funcion:{}: Esto indica que aquí se colocará el contenido que se desea formatear.
            :<15: Es una especificación de formato que significa que el campo debe tener un ancho de 15 caracteres 
            y la alineación es a la izquierda (<). Esto asegura que el texto tenga un espacio de 15 caracteres, y 
            si el texto es más corto, se llenará con espacios en blanco hasta alcanzar esa longitud.
    Retorna:None
    """

    imprimir_dato("{:<15} {:<15} {:<15} {:<30} {:<15}".format("Nombre", "Apellido", "Nro. Pasaporte", "Email", "Nro. Teléfono"))
    imprimir_dato("="*90)  # Línea separadora

    for pasajero in diccionario["lista_pasajeros"]:
        imprimir_dato("{:<15} {:<15} {:<15} {:<30} {:<15}".format(pasajero["Nombre"], pasajero["Apellido"], 
                                                          pasajero["Nro. Pasaporte"], pasajero["Email"], 
                                                          pasajero["Nro. Teléfono"]))
def estadisticas_por_edades(diccionario:dict[list[dict]])->str:
    """
    Parametro: Diccionario-> Contiene la informacion de los pasajeros
    Funcion: Arma un mensaje con: La edad mas comun,cuantos tienen esa edad y el promedio de edades
    Retorna: str
    """
    resultado_suma = 0
    edad_comun = 0
    diccionario_de_edades = edad_mas_comun(diccionario)
    for clave in diccionario_de_edades.keys():
        if edad_comun == 0 or edad_comun < int(diccionario_de_edades[clave]):
            edad_comun = clave

    for pasajero in diccionario["lista_pasajeros"]:
        for valor,clave in pasajero.items():
            if valor == "Edad":
                resultado_suma = suma(int(clave)) + resultado_suma

    promedio = promedio_edades(resultado_suma,diccionario)

    mensaje = f"La que mas se repite es {edad_comun}\nLa cantidad de los mismos es {diccionario_de_edades[edad_comun]}\nEl promedio de edad de los pasajeros es: {promedio}"
    
    return mensaje
