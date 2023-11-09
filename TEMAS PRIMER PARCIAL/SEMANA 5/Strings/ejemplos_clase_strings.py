# Ej. de declaración de un string (uso de comillas)
texto_1 = "Esto es un texto simple linea y puedo meter comillas simples si quiero, mira '''''''''"
texto_2 = 'Esto es un texto simple linea y puedo meter comillas dobles si quiero, mira """""""'
texto_3 = """Esto es un texto multilinea
Puedo hacer esto sin necesidad de caracteres especiales
"""
texto_4 = '''Esto tambien es un texto multilnea, pero con 
comillas simples'''

# print(texto_1)
# print(texto_2)
# print(texto_3)
# print(texto_4)


# Ej. de caracteres especiales
# print("Esto esta en una linea\nEsto esta en la de abajo")
# print("Esto esta aca \t y esto esta tabeado")


# Ej. strip(), lstrip(), rstrip()
texto_con_espacios_1 = "       Esto tiene espacios de sobra 1               "
texto_con_espacios_2 = "       Esto tiene espacios de sobra 2               "
texto_con_espacios_3 = "       Esto tiene espacios de sobra 3               "

# print(texto_con_espacios_1)

texto_sin_espacios_1 = texto_con_espacios_1.strip()
# print(texto_sin_espacios_1)

texto_sin_espacios_2 = texto_con_espacios_2.rstrip()
# print(texto_sin_espacios_2)

texto_sin_espacios_3 = texto_con_espacios_3.lstrip()
# print(texto_sin_espacios_3)


# Ej. lower(), upper(), capitalize(), title(), swapcase()
# Pone todo el texto en minuscula
texto = "Hola, COMO Va?"
texto_minuscula = texto.lower()
# print(texto_minuscula)

# Pone todo el texto en mayuscula
texto_mayuscula = texto.upper()
# print(texto_mayuscula)

# Pone la primer letra en mayuscula de la primer palabra
texto_capitalizado = texto.capitalize()
# print(texto_capitalizado)

# Pone la primer letra en maysucula de cada palabra
titulo = texto.title()
# print(titulo)

# Ej. replace()
# Reemplaza el texto que le pasamos como primer argumento, por el segundo
texto_replace_1 = "Esto es un texto".replace("texto", "string")
# print(texto)

# Por default reemplaza todas las ocurrencias
texto_replace_2 = "Esto es un texto texto texto texto texto texto texto".replace("texto", "string")
#print(texto_replace_2)

# Si le pasamos un tercer parametro podemos determinar cuantas ocurrencias reemplazar. 
texto_replace_3 = "Esto es un texto texto texto texto texto texto texto".replace("texto", "string", 2)
#print(texto_replace_3)

# Si le pasamos -1 reemplaza todas. 
texto_replace_4 = "Esto es un texto texto texto texto texto texto texto".replace("texto", "string", -1)
# print(texto_replace_4)

# Ej. split()
# Nos permite dividir un string en varios substrings.
# El primer parametro es un delimitador. Puede ser un caracter o varios
# El delimitador se omite de la lista devuelta
texto_sin_separar = "Esto, es, un, texto, separado, por, comas"
texto_separado = texto_sin_separar.split('to')
# print(texto_separado)

# Ej. join()
# Recibe un iterable. Devuelve un string concatenando todos los elementos 
# del iterable con el valor del string
lista_palabras = ["Hola", "Como", "Va?"]
texto_join = "+".join(lista_palabras)
# print(texto_join)



# Ej. zfill()
puntaje = "10"
puntaje = puntaje.zfill(8)
# print(puntaje)

# Ej. isalpha()
texto_1 = "Hola123"
# print("texto_1", texto_1.isalpha())

texto_2 = "Hola"
# print("texto_2", texto_2.isalpha())



# Ej. count()
texto = "Cuantas veces aparece la letra a en este texto"
cantidad_a = texto.count("a")
# print(cantidad_a)

# Ej. format()
# Automatico
# print('{} {} {}'.format('Texto 1', 'Texto 2', 'Texto 3'))

# Con nombres
# print('{x} {y} {z}'.format(x='Valor 1', y='Valor 2', z='Valor 3'))

# Por posicion
# print('{0} {1} {1} {2:.2f}'.format("Hola", "Como", 3.14))


# Ej. f-string
PI = 3.14456465
# print(f"Esto es concatenacion utilizando f-string {PI:.2f}")

# Ej. len()
nombre_usuario = "o.villegas"
lista = [1, 2, 3, 5]
# print("La lista tiene", len(lista))
# print(len(nombre_usuario))

# Ej. Slice
# texto = "Hola como va? Hacemos un break, les parece?"
# print(texto[0:13:2])

# Ej. Recorrer strings
# palabra = "Tengo un hambreee"
# for letra in palabra:
#   print(letra)

# Ejemplo de concatenar metodos
# Primer se aplica el upper() y al string que devolvio el upper()
# se le aplica el replace() y asi sucesivamente de izq a derecha
texto = "hola mundo"
texto = texto.replace("MUNDO", "PLANETA")
# print(texto)
texto = texto.upper().replace("MUNDO", "PLANETA")
# print(texto) # output HOLA PLANETA





