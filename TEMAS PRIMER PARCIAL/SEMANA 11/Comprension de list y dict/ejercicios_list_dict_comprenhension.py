"""
####################################################LIST COMPRENHENSION###############################################################
        En todos los casos resolver utilizando una comprensión de lista y la forma tradicional mediante bucle for

1)Dada una lista de números: 
lista_numeros = [10, 2, -5, 30, 50]
Crear una nueva lista donde cada número se duplique.
"""
lista_numeros = [10, 2, -5, 30, 50]
#FORMA TRADICIONAL
numero_duplicado = []
for numero in lista_numeros:
    resultado = numero *2
    numero_duplicado.append(resultado)
#LISTA COMPRENSION
lista_duplicados = [numero * 2 for numero in lista_numeros]

"""
2)Dada una lista de números: 
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Crea una lista que contenga solo los números pares 
"""
#FORMA TRADICIONAL
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = []
for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
#LISTA DE COMPRENSION
lista_pares = [numero for numero in lista_numeros if numero % 2 == 0]
"""
3)Dada una lista de nombres:
lista_nombres = ["Ana", "Juan", "María", "Carlos", "Luisa", "Pedro", "Sofía", "Pablo", "Laura", "Diego"]
Crea una lista de las iniciales de cada nombre
"""
#FORMA TRADICIONAL
lista_nombres = ["Ana", "Juan", "María", "Carlos", "Luisa", "Pedro", "Sofía", "Pablo", "Laura", "Diego"]
lsita_iniciales = []
for inicial in lista_nombres:
    lsita_iniciales.append(inicial[0])
#LISTA DE COMPRENSION
lista_iniciales = [inicial[0] for  inicial in lista_nombres]
"""
4)Dada una lista de frutas:
lista_frutas = ["manzana", "plátano", "naranja", "uva", "sandía", "fresa", "kiwi", "pera", "mango", "papaya"]
Crea una lista que contenga sólo las palabras que tienen más de 5 letras 
"""
lista_frutas = ["manzana", "plátano", "naranja", "uva", "sandía", "fresa", "kiwi", "pera", "mango", "papaya"]

lista_palabras_5_letras = []
for fruta in lista_frutas:
    if len(fruta) == 5:
        lista_palabras_5_letras.append(fruta)
#LISTA DE COMPRENSION
lista_palabras_5_letras = [fruta for fruta in lista_frutas if len(fruta)== 5]
"""
5)Dada una lista de números, 
lista_numeros = [8, 17, 33, 41, 59, 22, 14, 6, 49, 10]
Crea una lista donde los números impares se elevan al cuadrado y los números pares permanecen sin cambios.
"""
lista_numeros = [8, 17, 33, 41, 59, 22, 14, 6, 49, 10]
#FORMA TRADICIONAL
lista_numeros_modificados_2 = []
for numero in lista_numeros:
    if numero %2 != 0:
        resultado = numero ** 2
        lista_numeros_modificados_2.append(resultado)
    else:
        lista_numeros_modificados_2.append(numero)
#LISTA DE COMPRENSION
lista_numeros_modificados = [numero ** 2 if numero % 2 != 0 else numero ** 1 for numero in lista_numeros]
"""
6)Dada esta lista:
lista_numeros = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]
Crea una lista que contenga solo los valores únicos 
"""
lista_numeros = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]
#FORMA TRADICIONAL CON SET
lista_numeros_unicos = list(set(lista_numeros))
# FORMA TRADICIONAL 
lista_numeros_unicos = []
for numero in lista_numeros:
    if numero not in lista_numeros_unicos:
        lista_numeros_unicos.append(numero)
#LISTA DE COMPRENSION
lista_numeros_unicos = [list(set(numero for numero in lista_numeros))] 
#NOTA: 
"""
En este caso si quiero hacerlo con esa forma de condicion (if) me devuelve la lista vacia ya que  como
esta  creada previamente en la linea 81. primero sucede lo de adentro de la lista y luego 
lo guarda en la variable ergo devuelve algo vacio y si borro la linea 81 rompe porque esta comprando contra 
algo que no existe todavia.
"""
#lista_numeros_unicos = [numero for numero in lista_numeros if numero not in lista_numeros_unicos]
"""
7)Crea una lista que con tenga los números del 1 al 1000.
"""
# FORMA TRADICIONAL 
lista_mil_numeros = []
for numero in range(1001):
    lista_mil_numeros.append(numero)
#LISTA DE COMPRENSION
lista_mil_numeros = [numero for numero in range(1001)]
"""
8)Genera una lista que contenga 10 números enteros aleatorios en un rango del 1 al 1000.
"""
# FORMA TRADICIONAL 
import random
lista_diez_numeros = []
for _ in range(10):
    resultado = random.randint(1,1000)
    lista_diez_numeros.append(resultado)
#LISTA DE COMPRENSION
lista_diez_numeros = [random.randint(1,1000) for _ in range(10)]
"""
9)Dada una lista de nombres:
lista_nombres = ["Lourdes", "Ignacio", "Adela", "Roberto", "Marina", "Ramón", "Ezequiel", "Rodrigo", "Beatriz", "Miguel"]
Crea una lista que contenga sólo los nombres que comienzan con una consonante
"""
# FORMA TRADICIONAL 
lista_nombres = ["Lourdes", "Ignacio", "Adela", "Roberto", "Marina", "Ramón", "Ezequiel", "Rodrigo", "Beatriz", "Miguel"]
lista_nombres_consonante = []
for nombre in lista_nombres:
    if nombre[0].lower() not in ["a","e","i","o","u"]:
        lista_nombres_consonante.append(nombre)
#LISTA DE COMPRENSION
lista_nombres_consonante = [nombre for nombre in lista_nombres if nombre[0].lower() not in ["a","e","i","o","u"]]
"""
10)Dada una lista de nombres:
lista_nombres = ["Lourdes", "Ignacio", "Adela", "Roberto", "Marina", "Ramón", "Ezequiel", "Rodrigo", "Beatriz", "Miguel"]
Crea una lista que contenga sólo las primeras tres letras de los nombres que comienzan con una vocal 
"""
# FORMA TRADICIONAL 
lista_nombres = ["Lourdes", "Ignacio", "Adela", "Roberto", "Marina", "Ramón", "Ezequiel", "Rodrigo", "Beatriz", "Miguel"]
lista_nombres_consonante = []
for nombre in lista_nombres:
    if nombre[0].lower()  in ["a","e","i","o","u"]:
        lista_nombres_consonante.append(nombre[0:3])
#LISTA DE COMPRENSION
lista_nombres_consonante = [nombre[0:3] for nombre in lista_nombres if nombre[0].lower()  in ["a","e","i","o","u"]]

"""
----------------------------------------------------------------------------------------------------------------------------------------
####################################################DICT COMPRENHENSION###############################################################
        En todos los casos resolver utilizando una comprensión de diccionarios y la forma tradicional mediante bucle for

1)Dado un diccionario de estudiantes y sus calificaciones:
notas = { "Ana": 8, "Juan": 7, "María": 9, "Carlos": 6, "Luisa": 5, "Pedro": 10, "Sofía": 8, "Pablo": 6, "Laura": 9, "Diego": 7 }
Crea un nuevo diccionario donde las calificaciones donde solo se encuentren los alumnos que sacaron nota mayor o igual a 5.
"""
notas = { "Ana": 8, "Juan": 7, "María": 9, "Carlos": 6,"Matias": 3 ,"Luisa": 5, "Pedro": 10, "Sofía": 8, "Pablo": 6, "Laura": 9, "Diego": 7 }
# FORMA TRADICIONAL 
diccionarios_probados = {}
for clave,valor in notas.items():
    if valor >= 5:
        diccionarios_probados[clave]= valor
#LISTA DE COMPRENSION
diccionarios_probados = {clave:valor for clave,valor in notas.items() if valor >= 5}
"""
2)Dado una lista de colores y sus valores hexadecimales
colores_hex = {
    "Rojo": "#FF0000",
    "Verde": "#00FF00",
    "Azul": "#0000FF",
    "Amarillo": "#FFFF00",
    "Naranja": "#FFA500",
    "Violeta": "#8A2BE2",
    "Rosa": "#FFC0CB",
    "Gris": "#808080",
    "Cian": "#00FFFF",
    "Marrón": "#A52A2A"
}
Crea un nuevo diccionario donde los códigos hexadecimales sean las claves y los nombres de colores sean los valores.
"""
colores_hex = {
    "Rojo": "#FF0000",
    "Verde": "#00FF00",
    "Azul": "#0000FF",
    "Amarillo": "#FFFF00",
    "Naranja": "#FFA500",
    "Violeta": "#8A2BE2",
    "Rosa": "#FFC0CB",
    "Gris": "#808080",
    "Cian": "#00FFFF",
    "Marrón": "#A52A2A"
}
# FORMA TRADICIONAL 
diccionario_invertido = {}
for clave,valor in colores_hex.items():
        diccionario_invertido[valor] = clave
#LISTA DE COMPRENSION
diccionario_invertido = {valor:clave for clave,valor in colores_hex.items()}
"""
3)Dado un diccionario de productos y sus precios:
productos_precios = { "Manzanas": 50.5, "Bananas": 30.10, "Naranjas": 20.0, "Uvas": 55.10, "Peras": 38.10, "Frutillas": 80.5, "Kiwi": 120.10, "Mangos": 50.5, "Sandía": 20.1, "Papayas": 32.5 }
Crea un nuevo diccionario que aplique un descuento del 10% a cada producto.
"""

productos_precios = { "Manzanas": 50.5, "Bananas": 30.10, "Naranjas": 20.0, "Uvas": 55.10, "Peras": 38.10, "Frutillas": 80.5, 
                     "Kiwi": 120.10, "Mangos": 50.5, "Sandía": 20.1, "Papayas": 32.5 }
# FORMA TRADICIONAL 
diccionario_con_descuento = {}
for clave,valor in productos_precios.items():
        diccionario_con_descuento[clave] = (valor-(valor * 10 /100))
#LISTA DE COMPRENSION
diccionario_con_descuento = {clave:(valor-(valor * 10 /100)) for clave,valor in productos_precios.items()}
"""
4)Dado el siguiente texto, crear un diccionario donde clave es una letra y cada valor es la cantidad de veces que aparece la letra dentro del text
zen_python = '''

El Zen de Python, por Tim Peters
Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
Plano es mejor que anidado.
Disperso es mejor que denso.
La legibilidad cuenta.
Los casos especiales no son tan especiales como para quebrantar las reglas.
Aunque lo práctico le gana a la pureza.
Errores nunca deberían pasar silenciosamente.
A menos que se silencien explícitamente.
Frente a la ambigüedad, evitar la tentación de adivinar.
Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
Aunque esa manera puede no ser obvia en un primer momento a menos que usted sea holandés.
Ahora es mejor que nunca.
Aunque nunca es a menudo mejor que *ahora* mismo.
Si la implementación es difícil de explicar, es una mala idea.
Si la implementación es fácil de explicar, puede que sea una buena idea.
Los espacios de nombres son una gran idea ¡Hagamos más de eso!
'''
"""
zen_python = '''
El Zen de Python, por Tim Peters
Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
Plano es mejor que anidado.
Disperso es mejor que denso.
La legibilidad cuenta.
Los casos especiales no son tan especiales como para quebrantar las reglas.
Aunque lo práctico le gana a la pureza.
Errores nunca deberían pasar silenciosamente.
A menos que se silencien explícitamente.
Frente a la ambigüedad, evitar la tentación de adivinar.
Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
Aunque esa manera puede no ser obvia en un primer momento a menos que usted sea holandés.
Ahora es mejor que nunca.
Aunque nunca es a menudo mejor que *ahora* mismo.
Si la implementación es difícil de explicar, es una mala idea.
Si la implementación es fácil de explicar, puede que sea una buena idea.
Los espacios de nombres son una gran ide a ¡Hagamos más de eso!
'''
# FORMA TRADICIONAL 
diccionario_cantidad = {}
for letra in zen_python:   
     if letra.isalpha():
        diccionario_cantidad[letra] = zen_python.count(letra)

#LISTA DE COMPRENSION
diccionario_cantidad = {letra: zen_python.count(letra) for letra in zen_python if letra.isalpha()}


"""
https://onlinegdb.com/stoeXzTYK
"""