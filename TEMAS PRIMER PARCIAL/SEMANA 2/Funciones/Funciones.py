"""
1)
Crear una función que convierta grados Celsius a grados Fahrenheit. 
Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.
"""

def grados_fahrenheit(celsius:float)->float:
    """
    Variables: Grados Celsius
    Funcion: Convierte grados Celcius a Fahrenheit.
    Retorna: Grados Fahrenheit.
    """
    fahrenheit = 0

    fahrenheit = (celsius * 9/5)+32

    return "{0} grados Celsius es igual a {1} grados Fahrenheit".format(celsius,fahrenheit)

# print(grados_fahrenheit(100))

"""
2)
Crear una función que calcule el área de un círculo. Recibe un parámetro (radio) y devuelve el área del círculo.
"""

PI= 3.14

def calcular_area_de_un_circulo(radio:float)->float:
    """
    Variables: Un radio
    Funcion: Calcula un Area.
    Retorna: El area calculada.
    """

    area = 0
    area = PI * (radio**2)

    return "El radio ingresado es {0} y su area es: {1}".format(radio,area)

# print(calcular_area_de_un_circulo(50))

"""
3)
Crear una función que calcule el descuento aplicado a un producto. Recibe dos parámetros (precio original y precio con descuento) 
y devuelve el porcentaje de descuento aplicado.
"""

def calcular_descuento(precio_original:float,precio_final:float)->float:
    """ 
    Variables: Precio Inicial y precio con descuento
    Funcion: Calcula la diferencia entre dos precios y genera la diferencia porsentual
    Retorna: La diferencia porsentual.
    """
    descuento = 0
    porsentaje_descuento = 0

    descuento = precio_original - precio_final
    porsentaje_descuento = (descuento * 100)/precio_original

    return "El porsentaje de descuento es {} %".format(porsentaje_descuento)

# print(calcular_descuento(100.00,90.00))

"""
4)
Crear una función que calcule el promedio de edad de un grupo de personas. Recibe una lista de edades y devuelve el promedio.
"""
lista_edades = [1,4,5,6,7,8,12,9,15,16,15,18,19,20,3,4]
def calcular_promedio(lista:list)->float:
    """ 
    Variables: Listas numericas
    Funcion: Calcula el promedio .
    Retorna: Promedio.
    """
    acumlador = 0
    for edad in lista:
        acumlador += edad

    return acumlador/len(lista_edades)

# print(calcular_promedio(lista_edades))
"""
5)
Crear una función que determine si un número es primo o no. Recibe un parámetro (número) y devuelve True si es primo y 
False si no lo es.
"""

def calcular_numero_primo(numero:int)->bool:
    """ 
    Variables: Un numero  entero
    Funcion: Calcula si e sprimo o no.
    Retorna: Retorna True si lo es o False si no lo es.
    """
    for divisor in range(numero):
        if divisor > 2  and divisor < numero**2:
            if numero % divisor == 0:
                mensaje = False
                break
            else:
                mensaje = True
        elif numero == 2:
            mensaje = False
    return mensaje
# print(calcular_numero_primo())

"""
6)
Crear una función que calcule el área de un triángulo. Recibe dos parámetros (base y altura) y devuelve el área.
"""

def calcular_area_traingulo(base:float,altura:float)->float:
    """ 
    Variables: Base y area de un triangulo
    Funcion: Calcula el area
    Retorna: Area.
    """
    area = 0
    area = base * altura/2
    return area

# print(calcular_area_traingulo(10.5,8))

"""
7)
Crear una función que calcule el máximo común divisor de dos números. Recibe dos parámetros (números) y 
devuelve el máximo común divisor
"""



def maximo_comun_divisor(numero_uno:int,numero_dos:int)->int:
    """ 
    Variables: Dos numeros
    Funcion: Compara los numeros entre si y los separa en mas grande y mas chico, luego divide a el 
              numero mas chico por los divisores del mas grande que tengan menor valor que el nunmero mas chico.
    Retorna: devuelve el mayor divisor.
    """
    numero_mas_grande = 0
    divisor_mas_grande = 0
    numero_mas_chico = 0
    lista_divisores = []
    if numero_uno > numero_dos:
        numero_mas_grande = numero_uno
        numero_mas_chico = numero_dos
    else:
        numero_mas_grande = numero_dos
        numero_mas_chico = numero_uno
    
    for numero in range(numero_mas_grande):
        if numero > 0 and numero_mas_grande % numero == 0:
            lista_divisores.append(numero)
        for indice in range(len(lista_divisores)):
            if numero_mas_chico % lista_divisores[indice] == 0 and lista_divisores[indice] <= numero_uno and (indice == 0 or
             divisor_mas_grande < lista_divisores[indice]):
                divisor_mas_grande = lista_divisores[indice]

    return  divisor_mas_grande

resultado = maximo_comun_divisor(15,2) 
# print(resultado)

"""
8)
Crear una función que verifique si un número es par o impar. Recibe un número como parámetro y devuelve True si es par o False 
si es impar.
"""

def par_o_impar(numero:int)->bool:
    """ 
    Variables: Recibe un numero
    Funcion: Calcula si es par o impar
    Retorna: bool.
    """
    if numero % 2 == 0:
        mensaje = True 
    else:
        mensaje = False 
    
    return mensaje

resultado = par_o_impar(2)
# print(resultado)

"""
9)
Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. 
Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.
"""
numeros = [1,2,3,4,5,6,7,8,9,1,12,13,1,14,15,16,18,3,14,7]

def cuenta_elementos(lista:list[int],elemento)->int:
    """ 
    Variables: Recibe una lista y un elemento
    Funcion: Cuenta la cantidad de veces que esta el elemento
    Retorna: Retorna la cantidad.
    """
    # veces = lista.count(elemento) Resuelto con esta funcion
    contador = 0
    for numero in lista:
        if numero == elemento:
            contador += 1

    return contador
resultado = cuenta_elementos(numeros,7)
# print(resultado)

"""
10)
Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.
"""

lista_palabras = ["Montaña","Avión","Girasol","Guitarra","Elefante","Biblioteca","Estrella","Naranja","Computadora","Jardín"]

def palabra_mas_larga(lista:list[str])->str:
    """ 
    Variables: Una Lista
    Funcion: Compara el largo de las palabras y la guarda
    Retorna: La mas larga.
    """    
    mas_larga = None

    for palabra in lista:
        if mas_larga not in lista or len(mas_larga) < len(palabra):
            mas_larga = palabra
    
    return mas_larga
resultado = palabra_mas_larga(lista_palabras)

# print(resultado)

"""
11)
Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.
"""
frase = "Nuestra vida es lo que nuestros pensamientos hacen de ella."

def contador_vocales(frase:str)->int:
    """ 
    Variables: Cadena de caracteres
    Funcion: cuenta las vocales que hay en esa cadeana
    Retorna: La cantidad de vocales
    """ 
    contador = 0
    for letra in frase:
        if letra in "aeiou":
            contador += 1
    return contador
resultado = contador_vocales(frase)
# print(resultado)

"""
12)
Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas
"""
lista_uno = ["Juan", "María", "Carlos", "Ana", "Pedro"]
lista_dos = ["Laura", "Andrés", "Sofía", "Manuel", "Isabel"]

def unifificador_de_listas(lista_alfa:list,lista_beta:list)->list:
    """ 
    Variables: Dos listas
    Funcion: Hace una lista nueva con los datos de las dos o en el segundo caso extiene una lista con los datos
             de la otra
    Retorna: Unica lista con todos los datos
    """ 
    
    lista_aux = []
     
    for nombre_alfa in lista_alfa:
        lista_aux.append(nombre_alfa)
    for nombre_beta in lista_beta:
        lista_aux.append(nombre_beta)

    # otra forma
    lista_alfa.extend(lista_beta)
           

    return lista_alfa
resultado = unifificador_de_listas(lista_uno,lista_dos)
# print(resultado)

"""
13)
Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y 
su longitud como valores.
"""
def largo_de_caracteres(lista:list[str])->dict:
    """ 
    Variables: Cadena de caracteres
    Funcion: cuenta las vocales que hay en esa cadeana
    Retorna: La cantidad de vocales
    """ 
    diccionario_de_longitudes = {}
    for palabra in lista:
        # diccionario_de_longitudes[palabra] = len(palabra)
        diccionario_de_longitudes[palabra] = diccionario_de_longitudes.get(palabra,len(palabra)) #otra forma
    return diccionario_de_longitudes
resultado = largo_de_caracteres(lista_palabras)
# print(resultado)


"""
14)
Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, 
el valor máximo y el promedio de los números en la lista.
"""
def estadisticas_descriptivas(lista:float)->dict[float]:
    """ 
    Variables: Lista
    Funcion: Recorre la lista y busca el valor maximo y minimo y por ultimo hace el promedio de todos los numeros
    Retorna: Diccionarios con dichos valores
    """    
    estadisitcas = {}
    maximo = 0
    minimo = 0
    acumulador = 0
    for numero in lista:
        if maximo == 0 or maximo < numero:
            maximo = numero
        elif minimo == 0 or minimo > numero:
            minimo = numero
        acumulador += numero
    promedio =  acumulador/len(lista)
    estadisitcas["Maximo"] = maximo
    estadisitcas["Minimo"] = minimo
    estadisitcas["promedio"] = promedio

    return estadisitcas
resultado = estadisticas_descriptivas(lista_edades)
# print(resultado)
#OTRA FORMA DE HACERLO
import statistics
def estadisticas_descriptivas_dos(lista:int)->dict[float]:
    estadisticas_dos = {}
    estadisticas_dos["Maximo"] = max(lista)
    estadisticas_dos["Minimo"] = min(lista)
    estadisticas_dos["Promedio"] = statistics.mean(lista)

    return estadisticas_dos
resultado = estadisticas_descriptivas_dos(lista_edades)   
# print(resultado)

"""
15)
Crear una función que recibe una lista de diccionarios con información de películas 
(título, género, director) y devuelve un diccionario con la cantidad de películas por género.
"""
peliculas_clasicas = [
    {
        "titulo": "Casablanca",
        "genero": "Romance",
        "director": "Michael Curtiz"
    },
    {
        "titulo": "Lo que el viento se llevó",
        "genero": "Romance",
        "director": "Victor Fleming"
    },
    {
        "titulo": "El Padrino",
        "genero": "Drama",
        "director": "Francis Ford Coppola"
    },
    {
        "titulo": "Ciudadano Kane",
        "genero": "Misterio",
        "director": "Orson Welles"
    },
    {
        "titulo": "Lo que ocurrió aquella noche",
        "genero": "Comedia",
        "director": "Frank Capra"
    },
    {
        "titulo": "Cantando bajo la lluvia",
        "genero": "Musical",
        "director": "Stanley Donen y Gene Kelly"
    },
    {
        "titulo": "12 hombres en pugna",
        "genero": "Crimen",
        "director": "Sidney Lumet"
    },
    {
        "titulo": "Psicosis",
        "genero": "Terror",
        "director": "Alfred Hitchcock"
    },
    {
        "titulo": "Cadena perpetua",
        "genero": "Drama",
        "director": "Frank Darabont"
    },
    {
        "titulo": "Sueño de fuga",
        "genero": "Crimen",
        "director": "Frank Darabont"
    },
        {
        "titulo": "Harry Potter",
        "director": "Frank Darabont"
    }
]
def peliculas_por_genero(lista:list[dict])->dict:
    """ 
    Variables: Lista
    Funcion: Recorre la lista y busca el valor maximo y minimo y por ultimo hace el promedio de todos los numeros
    Retorna: Diccionarios con dichos valores
    """ 
    diccionarios_de_generos = {}

    for peliculas in lista:
        genero = peliculas.get("genero",None)
        diccionarios_de_generos[genero] = diccionarios_de_generos.get(genero,0)+1

    return diccionarios_de_generos
resultado = peliculas_por_genero(peliculas_clasicas)
# print(resultado)
# OTRA FORMA DE HACERLO
def peliculas_por_genero_dos(lista:list[dict])->dict:
    diccionarios_generos = {}

    for peliculas in lista:
        if peliculas.get("genero","no existe") not in diccionarios_generos: # si voy a usar el .get es importante aca,de lo contrario no entra
            diccionarios_generos[peliculas.get("genero","no existe")] = 1 # y aca de lo contrario no lo encuentra y lo rompe si falta  la categoria genero
        else:
             diccionarios_generos[peliculas["genero"]] += 1
    return diccionarios_generos
resultado =peliculas_por_genero_dos(peliculas_clasicas)
# print(resultado)