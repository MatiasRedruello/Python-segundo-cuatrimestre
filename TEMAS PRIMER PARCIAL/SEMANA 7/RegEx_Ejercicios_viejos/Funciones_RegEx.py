import re
"1)"
"EJERCICIO CON FUNCION"
def es_mayuscula(caracteres_alfabeticos:str)->bool:
    """
    Parametro: Caracter Afabetico-> Recibe un str
    Funcion: Genera un objeto match si el str y el patron coinciden
    Retorna: Bool dependiendo si hay match  o no
    """
    patron = "^[A-Z]*$"

    if re.match(patron,caracteres_alfabeticos):
        respuesta = True
    else:
        respuesta = False
    
    return respuesta

"EJERCICIO CON LAMBDA"   
# es_mayuscula = lambda caracteres_alfabeticos: bool(re.match("^[A-Z ]*$",caracteres_alfabeticos))
 
"EJERCICIO CON DESEMPAQUETADO" 
# def es_mayuscula(**caracteres_alfabeticos:dict[str])->dict[bool]:
    # """
    # Parametro: Caracter Afabetico-> Diccionario con str
    # Funcion: Recorre el diccionario y guarda clave en un nuvo diccionario y les asigna true si hay match o false en caso de que no
    # Retorna: Diccionario de booleanos
    # """
#     diccionario_true = {}
#     diccionario_false = {}
#     patron = "^[A-Z]*$"
#     for texto_machear in caracteres_alfabeticos.values():
#         if re.match(patron,texto_machear):
#             diccionario_true[texto_machear] = True
#         else:
#             diccionario_false[texto_machear] = False
#     diccionario_true.update(diccionario_false)
#     return  diccionario_true
"2)"
"EJERCICIO CON FUNCION"
def es_minuscula(caracteres_alfabeticos:str)->bool:
    """
    Parametro: Caracter Afabetico-> Recibe un str
    Funcion: devuelve un objeto match si el str y el patron coinciden
    Retorna: Bool dependiendo si hay match  o no
    """
    patron = "^[a-z]*$"

    if re.match(patron,caracteres_alfabeticos):
        respuesta = True
    else:
        respuesta = False
    
    return respuesta  
"EJERCICIO CON LAMBDA"
# es_minuscula = lambda caracteres: bool(re.match("^[a-z]*$",caracteres))  

"3)"
def es_entero(carateres_numericos:str)->bool:
    """
    Parametro: Caracter numerico-> Recibe un str
    Funcion: devuelve un objeto match si el str y el patron coinciden
    Retorna: Bool dependiendo si hay match  o no
    """
    patron = "^[0-9]*$"

    if re.match(patron,carateres_numericos):
        respuesta = True
    else:
        respuesta = False
    
    return respuesta
"EJERCICIO CON LAMBDA"
# es_entero = lambda enteros: bool(re.match("^[0-9]*$",enteros))

"4)"
def es_solo_texto(texto:str)->bool:
    """
    Parametro: Texto-> Recibe un str
    Funcion: devuelve un objeto match si el str y el patron coinciden
    Retorna: Bool dependiendo si hay match  o no
    """
    patron = r"^[\D\s]*$"

    if re.match(patron,texto):
        respuesta = True
    else:
        respuesta = False
    
    return respuesta
"EJERCICIO CON LAMBDA"
# es_solo_texto = lambda texto: bool(re.match(r"^[\D\s]*$",texto))

"5)"
def es_decimal(exprecion_decimal:str,separador_decimal:str)->bool:
    """
    Parametro: Exprecion decimal-> Recibe un str
               Separador decimal-> Recibe un "." o una ","
    Funcion: devuelve un objeto match si el str y el patron coinciden
    Retorna: Bool dependiendo si hay match  o no
    """    
    # escapa el separador que pasan por paramatro, util ya que escapa los caracteres especiales
    patron_separador = re.escape(separador_decimal)
    patron_exprecion = r"^[\d]*{0}[\d]+$".format(patron_separador)

    if re.match(patron_exprecion,exprecion_decimal):
        resultado = True
    else:
        resultado = False 
    
    return resultado

"6)"
def es_alfanumerico(caracteres_afanumericos:str)->bool:
    """
    Parametro: Caracteres afanumericos-> Recibe un str
    Funcion: devuelve un objeto match si el str y el patron coinciden
    Retorna: Bool dependiendo si hay match  o no
    """
    patron = r"^[\w]+$"

    if re.match(patron,caracteres_afanumericos,re.I):
        respuesta = True
    else:
        respuesta = False
    
    return respuesta

"EJERCICIO CON LAMBDA"
# es_alfanumerico = lambda caracteres_afanumericos: bool(re.match(r"^[\w]+$",caracteres_afanumericos,re.IGNORECASE))

"7)"
def es_binario(caracteres_binarios:str)->bool:
    """
    Parametro: Caracteres binarios-> Recibe un str
    Funcion: devuelve un objeto match si el str y el patron coinciden
    Retorna: Bool dependiendo si hay match  o no
    """
    patron = r"^[0-1]+$"

    if re.match(patron,caracteres_binarios):
        respuesta = True
    else:
        respuesta = False
    
    return respuesta 
"EJERCICIO CON LAMBDA"
# es_binario = lambda caracteres_binarios: bool(re.match(r"^[0-1]+$",caracteres_binarios))

"8)"
def crear_lista_palabras_con_u(lista:list[str])->list:
    """
    Parametro: Lista-> lista con str
    Funcion: devuelve un objeto match si el str y el patron coinciden y arma un lista con las coincidencias
    Retorna: lista
    """    
    patron = r"^[u]"
    # list comprehension # funciona tambien con match
    lista_palabras_con_u = [palabra for palabra in lista if re.findall(patron,palabra,re.I)]
    return lista_palabras_con_u

"EJERCICIO CON LAMBDA"
# lambda mas list comprehension # funciona tambien con match
# crear_lista_palabras_con_u = lambda lista: [palabra for palabra in lista if re.findall(r"^[u]",palabra,re.I)]

"9)"
def crear_lista_largo_palabra(lista:list[str])->list:
    """
    Parametro: lista-> lista con str
    Funcion: devuelve un objeto match si el str y el patron coinciden y arma un lista con las coincidencias
    Retorna: lista
    """    
    patron = r"^[a-z]{1,6}$"
    # list comprehension # funciona tambien con match
    lista_palabras_por_largo = [palabra for palabra in lista if len(palabra) < 7 and len(palabra) > 2 and re.findall(patron,palabra,re.I)]
    return lista_palabras_por_largo
"EJERCICIO CON LAMBDA"
# lambda mas list comprehension # funciona tambien con match
# crear_lista_largo_palabra = lambda lista: [palabra for palabra in lista if len(palabra) < 7 and len(palabra) > 2 and re.findall(r"^[a-z]{1,6}$",palabra,re.I)]

"10)"
def crear_lista_palabras_terminadas_cion(texto:str)->list:
    """
    Parametro: texto-> Recibe un str
    Funcion: devuelve un objeto match si el str y el patron coinciden y arma un lista con las coincidencias
    Retorna: lista
    """    
    patron = r"\b\w*ción\b"
    lista_palabras_terminadas_cion =  re.findall(patron,texto,re.I)

    return lista_palabras_terminadas_cion
"EJERCICIO CON LAMBDA"
# crear_lista_palabras_terminadas_cion = lambda texto: re.findall(r"\b\w*ción\b",texto,re.I)
"11)"
def crear_lista_palabras_inicia_vocal(texto:str)->list:
    """
    Parametro: texto-> Recibe un str
    Funcion: devuelve un objeto match si el str y el patron coinciden y arma un lista con las coincidencias
    Retorna: lista
    """    

    patron = r"\b[aeiou]\w*\b"
    listas_palabras_vocal =  re.findall(patron,texto,re.I)

    return listas_palabras_vocal
"EJERCICIO CON LAMBDA"
# crear_lista_palabras_inicia_vocal = lambda texto: re.findall(r"\b[aeiou]\w*\b",texto,re.I)

"12)"
def obtener_oraciones(texto:str)->list:
    """
    Parametro: texto-> Recibe un str
    Funcion: devuelve un objeto match si el str y el patron coinciden y arma un lista con el patron de corte
    Retorna: lista
    """    
    patron_separador = r"\.|\?|\!"
  
    lista_oraciones = re.split(patron_separador,texto)

    return lista_oraciones
"EJERCICIO CON LAMBDA"
# obtener_oraciones = lambda texto: re.split(r"\.|\?|\!",texto)
"13)"
def corregir_ortografia(texto:str)->str:

    texto_corregido_a = re.sub(r"mv",r"nv",texto)
    texto_corregido_final = re.sub(r"nb",r"mb",texto_corregido_a)

    return texto_corregido_final

"14)"
def es_fecha(fecha:str,separador_fecha):
    patron_separador = re.escape(separador_fecha)
    patron_comparacion = rf"^[\d]{{1,2}}{patron_separador}[\d]{{1,2}}{patron_separador}[\d]{{2,4}}$"
    if re.match(patron_comparacion,fecha):
        resultado = True
    else:
        resultado = False


    return resultado
"EJERCICIO CON LAMBDA"
#se puede pero queda horrible
# es_fecha = lambda fecha,separador_fecha: bool(re.match(rf"^[\d]{{1,2}}{re.escape(separador_fecha)}[\d]{{1,2}}{re.escape(separador_fecha)}[\d]{{2,4}}$",fecha))

"15)"
def es_hora(hora:str)->bool:
    patron = r"^[\d]{2}:[\d]{2}:[\d]{2}$"
    if re.match(patron,hora):
        resultado = True
    else:
        resultado = False
    return resultado
"EJERCICIO CON LAMBDA"
# es_hora = lambda hora: bool(re.match(r"^[\d]{2}:[\d]{2}:[\d]{2}$",hora))

"16)"
def validar_codigo_postal(codigo:str)->bool:

    patron = r"^[a-z]{1}[\d]{4}[a-z]{3}$"
    if re.match(patron,codigo,re.I):
        resultado = True
    else:
        resultado = False
    return resultado 
"EJERCICIO CON LAMBDA"
# validar_codigo_postal = lambda codigo: bool(re.match(r"^[a-z]{1}[\d]{4}[a-z]{3}$",codigo))

"17)"
def validar_patente(patente:str)->bool:
    patron = r"^[A-Z]{2}[\d]{3}[A-Z]{2}$"
    if re.match(patron,patente,re.I):
        resultado = True
    else:
        resultado = False
    return resultado  
# "EJERCICIO CON LAMBDA"
# validar_patente = lambda patente: bool(re.match(r"^[A-Z]{2}[\d]{3}[A-Z]{2}$",patente))   
"18)"
def obtener_direcciones_email(texto):
    pass

"19)"
def validar_password(password):
    mensaje = True
    # Longitud mínima de 8 caracteres
    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        mensaje = False

    # Al menos una letra mayúscula y una minúscula
    if not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password):
        print("La contraseña debe contener al menos una letra mayúscula y una minúscula.")
        mensaje = False

    # Al menos un número
    if not re.search(r"\d", password):
        print("La contraseña debe contener al menos un número.")
        mensaje = False

    # Al menos un carácter especial
    if not re.search(r"[!@#$%^&*()-_=+{};:,<.>/?[\]~]", password):
        print("La contraseña debe contener al menos un carácter especial.")
        mensaje = False

    return mensaje
"20)"
import re

def validar_ip(ip):
    # Patrón de expresión regular para validar una dirección IP v4
    patron_ip = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    # Verificar si la IP coincide con el patrón
    match = re.match(patron_ip, ip)

    if not match:
        return False

    # Verificar si cada número está en el rango adecuado (0-255)
    for grupo in match.groups():
        if not 0 <= int(grupo) <= 255:
            return False

    return True







    
