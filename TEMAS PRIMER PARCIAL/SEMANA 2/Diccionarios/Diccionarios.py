"""
1)

Crea un diccionario que represente los días de la semana, donde las claves son los nombres de los días y
los valores son los números correspondientes (por ejemplo, {"lunes": 1, "martes": 2, ...}). Imprime el valor
correspondiente al día "miércoles".
"""

# semana = {"Lunes":1,"Martes":2,"Miercoles":3,"Jueves":4,"Vieres":5,"Sabado":6,"Domingo":7}
# print(semana["Miercoles"])

# Otra forma:

# semana_b = {}
# semana_b["Lunes"] = 1
# semana_b["Martes"] = 2
# semana_b["Miercoles"] = 3
# semana_b["Jueves"] = 4
# semana_b["Viernes"] = 5
# semana_b["Sabado"] = 6
# semana_b["Domingo"] = 7

# print(semana_b["Miercoles"])

"""
2)
Crea un diccionario que represente los meses del año, 
donde las claves son los nombres de los meses y los valores
son sus números correspondientes (por ejemplo, {"enero": 1, "febrero": 2, ...}).
Imprime el número correspondiente al mes "julio".
"""


# meses = {}
# meses["Enero"] = 1
# meses["Febrero"] = 2
# meses["Marzo"] = 3
# meses["Abril"] = 4
# meses["Mayo"] = 5
# meses["junio"] = 6
# meses["Julio"] = 7
# meses["Agosto"] = 8
# meses["Septiembre"] = 9
# meses["Octubre"] = 10
# meses["Noviembre"] = 11
# meses["Diciembre"] = 12

# print(meses["Julio"])

# print(meses.get("Enero","Not Found"))

"""
3)
Crea un diccionario que contenga la información de una película,
como título, director y año de estreno. Luego, imprime el
título de la película.
"""

# pelicula = {"Titulo":"Space Jam: El juego del siglo ","Director":"David F. Klassen","Año de estreno":1996 }

# print(pelicula.get("Titulo","Clave incorrecta"))

"""
4)
Crea un diccionario que contenga la información de una 
dirección: nombre de la calle, altura, localidad, código postal,
partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.
"""

# direccion = {"nombre de la calle":"Florida","altura":1000,"localidad":"Piñeiro","codigo postal":2030,"partido":"Avellaneda","provincia":"Buenos Aires"}

# print(r"Nombre de la calle es {0} y la altura es {1}".format(direccion["nombre de la calle"],direccion["altura"]))
# ficha = f"""El nombre de la calle es: {direccion.get("nombre de la calle")} y la altura es: {direccion.get("altura")}"""
# print(ficha)


"""
5)
Crea un diccionario que represente los continentes, donde las claves son los
nombres de los continentes y los valores son los números correspondientes 
(por ejemplo, {"América": 1, "Europa": 2, ...}). 
Imprime el valor correspondiente al continente "África"
"""

# continentes = {"America":1,"Europa":2,"Asia":3,"Africa":4,"Ociania":5}
# print(continentes.get("Africa"))

"""
6)
Crea un diccionario que represente las estaciones del año, donde las claves
son los nombres de las estaciones y los valores son los números correspondientes 
(por ejemplo, {"primavera": 1, "verano": 2, ...}). Imprime el valor correspondiente
a la estación "invierno".
"""
# estaciones_del_ano = {"Verano":1,"Otoño":2,"Invierno":3,"Primero":4}
# print(estaciones_del_ano["Invierno"])

"""
7)
Crea un diccionario que contenga la información de una canción: título, artista y
duración. Luego, imprime la duración de la canción.
"""

# cancion = {"Titulo":"Animal","Artista":"Three Days Grace","Duracion":5.15}
# print(cancion["Duracion"])

"""
8)
Crea un diccionario que represente las edades de varias personas, 
donde las claves son los nombres de las personas y los valores son sus edades. 
Imprime la edad de la persona más joven.
"""

# nombres = {"Marcos":20,"Ariel":10,"Matias":26}
# menor = ""
# flag = True
# for edades in nombres:
#     if flag or menor > edades: 
#         menor = edades
#         flag = False
# print(menor)
"""
9)
Crea un diccionario que contenga las capitales de los países de América del Sur. 
Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.
"""

# paises = {"Argentina":" Buenos Aires","Bolivia": "Sucre","Brasil": "Brasilia","Chile": "Santiago","Colombia": "Bogotá",
#           "Ecuador": "Quito","Guyana": "Georgetown","Paraguay": "Asunción","Perú": "Lima","Surinam": "Paramaribo",
#           "Uruguay": "Montevideo","Venezuela": "Caracas"}

# nombre_ingresado = """input("Ingrese un pais de America del Sur")"""

# for pais in paises:
#     if nombre_ingresado not in paises:
#         mensaje = "El pais ingresado no esta en la base de datos"
#     else:
#         mensaje = "La capital del pais es:{0}".format(paises[nombre_ingresado])  
    
# print(mensaje)

"""
10)
Crea un diccionario que represente las notas de un examen de varios estudiantes, 
donde las claves son los nombres de los estudiantes y los valores son sus notas. 
Imprime el promedio de las notas.
"""

# alumnos = {"Marcos":6,"Ariel":7,"Matias":5,"Ramon":7,"julian":9}
# suma = 0
# for notas in alumnos.values():
#     suma += notas

# print(suma/len(alumnos))

"""
11)
Crea un diccionario que represente una lista de tareas por hacer. Cada clave del diccionario debe ser el nombre de una 
tarea y cada valor debe ser su estado (los estados son:  pendiente, en proceso, completada). Imprimir todas las tareas 
seguido de su estado.
"""

# tareas = {"cama":"completado","platos":"completado","limpiar":"pendiente","estudiar":"en proceso"}

# print(tareas)

"""
12)
Crea un diccionario que represente una lista de las compras. Cada clave del diccionario debe ser el nombre de un producto
y cada valor debe ser su cantidad. Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad
"""

# compras = {"tomates":5,"enlatados":6,"bananas":3,"azucar":1,"cafe":1}

# while True:
#     articulo_ingresado = input("Ingrese un articulo").lower()
#     if articulo_ingresado not in compras:
#          print(r"El articulo {0} no esta en la lsita, no hay que llevarlo".format(articulo_ingresado))
         
#     else:
#         mensaje = r"El articulo es:{0} y lleva {1}".format(articulo_ingresado,compras[articulo_ingresado])
#         break

# print(mensaje)

"""
13)
Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa. Luego, pedirle al usuario 
un nivel de dificultad, buscar los que coinciden e imprimir sus nombres
"""

# juegos = {}

# juegos["Ajedrez"] = "alta"
# juegos["Catan"] = "media"
# juegos["Ticket to Ride"] = "baja"
# juegos["Risk"] = "media"
# juegos["Dominion"] = "media"

# respuesta = input("Elija un nivel de dificultad: Alta,Media,Baja").lower()
# lista = []
# for juego,dificultad in juegos.items():
#     if respuesta == dificultad:
#         lista.append(juego)
# print(lista)

"""
14)
Crea un diccionario que contenga el nombre como clave y el puntaje como valor de varios jugadores en un juego. 
Luego, pedirle al usuario el nombre del jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.
"""

# jugadores = {"Messi":50,"Lewandowski":54,"Mbappé":39,"Immobile":39,"Ronaldo":39 }

# jugador = input("Jugador")
# if jugador in jugadores:
#     actualizar = input("Ingrese el nuevo score")
#     if actualizar.isdigit():
#         jugadores[jugador] = actualizar
#         mensaje = jugadores
#     else:
#         mensaje = "No ingreso un numero"
# else:
#     mensaje = "Ese jugaodr no es un goleador del 2019"

# print(mensaje)

"""
15)
Crea un diccionario que contenga el nombre y el sueldo de varios empleados. Luego, permite al usuario aumentar el sueldo de un 
empleado y actualizar el valor correspondiente en el diccionario.
"""
# empleados = {"Messi":5000000,"Lewandowski":540000,"Mbappé":390000,"Immobile":398000,"Ronaldo":3900000}

# nombre = input("Jugador")
# if nombre in empleados:
#     actualizar = input("Ingrese nuevo sueldo")
#     if actualizar.isdigit():
#         empleados[nombre] = actualizar
#         mensaje = "Los sueldos de los empleados quedaron: {0}".format(empleados)
#     else:
#         mensaje = "No ingreso un numero"
# else:
#     mensaje = "Ese jugaodr no es un goleador del 2019"

# print(mensaje)

"""
16)
Crea un diccionario que represente una lista de tareas pendientes, donde las claves son las tareas y 
los valores son "True" si están completadas y "False" si no lo están. Solicita al usuario el nombre 
de una tarea y modifica el valor para marcarla como completada. Imprimir el listado de tareas pendientes.
"""
# tareas = {"cama":False,"platos":False,"limpiar":False,"estudiar":False}
# lista_aux = []
# completado = input("Que tarea completo?").lower()

# if completado in tareas:
#     tareas[completado] = True
#     for tarea in tareas:
#         if tareas[tarea] == False:
#             lista_aux.append(tarea)
#             mensaje = "Las tareas pendientes son {0}".format(lista_aux)
        
# print(lista_aux)

"""
17)
Crea un diccionario que represente las películas de un cine, donde las claves son los nombres de las películas 
y los valores son los horarios correspondientes. Modifica el horario de la película "Avengers: Endgame" a las 19:30.
"""

# cine = {"Avengers Endgame": "20:00","The Conjuring": "14:30","The Unholy": "22:30","Cruella": "19:30","Avatar": "15:00"}

# cine["Avengers Endgame"] = "19:30"

# print(cine)

"""
18)
Crea un diccionario que represente los juegos de una consola, donde las claves son los nombres de los juegos y 
los valores son las puntuaciones correspondientes. Solicita al usuario el nombre de un juego y luego su puntuación, 
si el juego no existe agregarlo y si existe actualizar su puntuación 
"""

# juegos = {"The Legend of Zelda":100,"Red Dead Redemption":80,"The Witcher":150,"Super Mario Odyssey":500}

# pregunta = input("Que juego elige?")
# score = input("puntaje")

# if pregunta not in juegos:
#     juegos[pregunta] = score
# else:
#     juegos[pregunta] = score
# print(juegos)

"""
19)
Crea un diccionario que represente las temperaturas de una ciudad durante una semana, donde las claves son los días 
de la semana y los valores son las temperaturas correspondientes. Calcula la temperatura promedio de la semana
"""
# semana = {"lunes":10,"martes":8,"miercoles":9,"jueves":11,"vieres":9,"sabado":8,"domingo":7}
# acumulador = 0

# for dia in semana:
#     acumulador  += semana[dia]
# promedio = acumulador/len(semana)
# print("La temperatura promedio de la semana es: {0}".format(promedio))

"""
20)
Crea un diccionario que represente los asientos de un avión, donde las claves son los números de asientos y los valores 
son "True" si están ocupados y "False" si no lo están. Solicita al usuario un número de asiento y modifica su valor para 
marcarlo como ocupado. Luego imprimí la lista de asientos libres
"""
# asientos = {"1":False,"2":False,"3":False,"4":False,"5":False,"6":False,"7":False,"8":False,"9":False,"10":False,"11":False}
# lista_aux = []
# pregunta = input("Que asiento tiene?")
# if pregunta not in asientos:
#     mensaje = "Lo sentimos pero se equivo de vuelo"
# elif asientos[pregunta] == False:
#     asientos[pregunta] = True
#     for butaca in asientos:
#         if asientos[butaca] == False:
#             lista_aux.append(butaca)
#             mensaje = "los asientos libres son {0}".format(lista_aux)
        
# print(mensaje)

"""
21)
Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de 
las categorías y los valores son los gastos correspondientes. Calcula el total de gastos de la persona.
"""

# gastos = {"comida":60000,"alquiler":40000,"servicios":10000,"salidas":20000}
# acumulador = 0

# for categoria in gastos:
#     acumulador += gastos[categoria]
# print("Los gastos de este mes fueron {0}".format(acumulador))

"""
22)
Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las 
categorías y los valores son los gastos correspondientes. Calcula el total de gastos de la persona en el año.
"""
# gastos = {"comida":60000,"alquiler":40000,"servicios":10000,"salidas":20000}
# acumulador = 0

# for categoria in gastos:
#     acumulador += gastos[categoria] * 12
# print("Los gastos de este mes fueron {0}".format(acumulador))

"""
23)
Crea un diccionario que represente los contactos de un teléfono, donde las claves son los nombres de las personas y los valores 
son los números de teléfono correspondientes. Solicitar al usuario el nombre de un contacto: agregarlo al diccionario en caso de 
que no exista. En caso de que exista modificar el número de teléfono del contacto.
"""
# contactos = {"martin":1512131411,"juan":1512131412,"pablo":1512131413,"matias":1512131414,"maria":1512131415,"jose":1512131416}
# nombre = input("Cual es su nombre?").lower()
# numero = input("Cual es su numero?")
# if nombre not in contactos:
#     contactos[nombre] = numero 
# else:
#     contactos[nombre] = numero
# print("La lista esta actualizada: {0}".format(contactos))