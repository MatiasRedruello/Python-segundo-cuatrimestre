"""
1)Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.
"""
def formatear_str_a_mayusculas(texto:str)->str:
    texto_normal = texto
    texto_formateado = texto_normal.upper()
    return texto_formateado

#print(formatear_str_a_mayusculas("hola mundo"))
"""
2)Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.
"""
formatear_texto_a_minuscula = lambda x:x.lower()

#print(formatear_texto_a_minuscula("HOLA MUNDO"))
"""
3)Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, 
separados por un espacio.
"""
cadena_concatenada = lambda x: " ".join(x)

#print(cadena_concatenada(["hola","mundo","totales"]))
"""
4)Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.
"""
def contar_caracteres(texto:str)->int:
    contador_caracteres = len(texto)
    return contador_caracteres
#print(contar_caracteres("Hola mundo. Como estan?"))
"""
5)Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.
"""
def contador_de_ocurrencias(texto:str,ocurrencia_deseada:str)->int:
    total_de_ocurrencias = texto.lower().count(ocurrencia_deseada)
    return total_de_ocurrencias 
#print(contador_de_ocurrencias("gracias totAles","a"))
"""
6)Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que 
contienen ese carácter.
"""
texto_random = "La excelencia no es un acto, sino un hábito; cultivemos virtud en cada acción y alcanzaremos la felicidad."
def crear_lista_de_palabras(texto:str,caracter:str)->list:
    lista_palabras = texto.split(" ")
    lista_aux = []
    for palabra in lista_palabras:
        if caracter in palabra:
            lista_aux.append(palabra)
    
    return lista_aux
#print(crear_lista_de_palabras(texto_random,"a"))
"""
7)Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados
"""
eliminar_espacios = lambda x: x.replace(" ","")

#print(eliminar_espacios(texto_random))
"""
8)Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido, eliminando 
los espacios del comienzo y el final y colocando la primer letra en mayúscula
"""
def formatear_nombre_apellido(nombre, apellido):

    nombre_formateado = nombre.strip().capitalize()
    apellido_formateado = apellido.strip().capitalize()

    return {"nombre": nombre_formateado, "apellido": apellido_formateado}

nombre = "  juan  "
apellido = "  perez  "
resultado = formatear_nombre_apellido(nombre, apellido)
# print(resultado)  
"""
9)Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un salto dee línea, por ejemplo: 
["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".
"""
lista_nombres = ["Juan", "María", "Pedro"]

formatear_lista_de_nombres = lambda x: f" \n".join(x)

# print(formatear_lista_de_nombres(lista_nombres))   
"""
10)Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".
"""
def crear_mail(nombre:str,apellido:str)->str:
    formato = "inicial_nombre.apellido@utn-fra.com.ar"
    formato = formato.replace("nombre",nombre.lower()).replace("apellido",apellido.lower()).replace("inicial",nombre[0].upper())
    return formato
# print(crear_mail("matias","REDRUELLO"))
"""
11)Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas 
y "y" antes de la última palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas"..
"""
def concatenar_palabras(lista:list[str])->str:
    if not lista:
        print(-1)
    if len(lista) > 1:
        formato_final = '{} y {}'.format(', '.join(lista[:-1]), lista[-1])

    return formato_final    

# print(concatenar_palabras(lista_nombres))
"""
12)Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos y 
los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234".
"""
def tarjeta_de_credito():
    flag_validar_tarjeta = True
    while flag_validar_tarjeta:
        tarjeta = input("Ingrese el numero de su tarjeta")
        if not tarjeta.isnumeric() or len(tarjeta) != 16:
            print("No ingreso numeros o no puso los 16 numero de la tarjeta")
        else:
            flag_validar_tarjeta = False    
    numero_encriptado = tarjeta.replace(tarjeta[:12],"************")
    numero_separado_y_encriptado = f"{numero_encriptado[:4]} {numero_encriptado[4:8]} {numero_encriptado[8:12]} {numero_encriptado[12:26]}"

    return numero_separado_y_encriptado
# print(tarjeta_de_credito()) 
""" 
13)Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".
"""
def separar_dato_del_mail(mail:str)->str:
    dato = mail.split("@")

    return dato[0]

# print(separar_dato_del_mail("matias@gmail.com"))
"""
14)Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..
"""
def obtener_dominio(url:str)->str:
    url = url.replace("https://", "").replace("http://", "")
    partes = url.split(".")
    print(partes[-2])

# print(obtener_dominio("http://www.supervielle.com"))
"""
15)Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, eliminando cualquier número o símbolo 
(sólo son válidos letras y espacios), por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”
"""
def solo_caraceteeres_alfbeticos(texto:str)->str:
    caracteres_permitidos = []
    for caracteres in texto:
        if caracteres.isalpha():
            caracteres_permitidos.append(caracteres)
    return "".join(caracteres_permitidos)

    #caracteres_permitidos = [c for c in texto if c.isalpha() or c.isspace()] "Es una lista de comprencion"
    #return ''.join(caracteres_permitidos)

# print(solo_caraceteeres_alfbeticos("http://www.supervielle.com"))
"""
16)Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra de cada palabra, por ejemplo: 
"Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.
"""
def crear_acronimo(texto:str)->str:
    caracter_para_acronimo = []
    palabras = texto.split(" ")
    for palabra in palabras:
        for indice in range(len(palabra)):
            if 0 == indice:
                caracter_para_acronimo.append(palabra[indice])

    return "".join(caracter_para_acronimo) 

    # acronimo = [palabra[indice] for palabra in palabras for indice in range(len(palabra)) if 0 == indice] "list comprehension"
    # return "".join(acronimo)
# print(crear_acronimo("Universidad Tecnológica Nacional Facultad Regional Avellaneda"))
"""
17)Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario, por 
ejemplo: "101" -> "00000101".
"""
def transformar_binario_a_bit(numero:str)->str:
    numero_bit = numero.zfill(8)
    return numero_bit

# print(transformar_binario_a_bit("101"))
"""
18)Escribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas 
por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"
"""
def cambiar_tamaño(texto:str)->str:
    texto_modificado = texto.swapcase()
    return texto_modificado
            
# print(cambiar_tamaño("Hola Mundo"))
"""
19)Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.
"""
def contar_digitos(texto:str)->int:
    contador = 0
    for caracter in texto:
        if caracter.isdigit():
            contador += 1
    return contador
    
# print(contar_digitos("12346 felis año nuevo"))
"""<    
20)Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma, por 
ejemplo: ["juan@gmail.com", "maria@hotmail.com",pedro@hotmail.com] -> "juan@gmail.com;maria@hotmail.com".
"""
def unir_correos(lista:list[str])->str:
    texto = ";".join(lista)
    return texto

# print(unir_correos(["juan@gmail.com", "maria@hotmail.com","pedro@hotmail.com"]))
"""
21)Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero 
que indica cuántas veces aparece esa palabra dentro del string.
"""
texto = """Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero 
que indica cuántas veces aparece esa palabra dentro del string."""
def cantidad_de_palabras(texto:str)->dict:
    lista_palabras = texto.split()
    diccionario = {}
    for palabra in lista_palabras:
        if palabra not in diccionario:
            diccionario[palabra] = 1
        else:
            diccionario[palabra] += 1
    return diccionario

# print(cantidad_de_palabras(texto))

