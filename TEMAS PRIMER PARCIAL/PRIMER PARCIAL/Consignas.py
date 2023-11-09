"""
----------------------------------------23/9--------------------------------------------------------
Ejercicio gestión de Pasajeros

Deberán crear un programa para gestionar la lista de pasajeros de un viaje. La lista de
pasajeros se almacenará en una lista de diccionarios, donde cada diccionario
representa a un pasajero con su información personal
La estructura pasajero deberá contener: Nombre, Apellido, Nro. Pasaporte, Email, Nro.
Teléfono.

El programa deberá ofrecer un menú interactivo con las siguientes opciones:
-Agregar Pasajero
-Modificar Pasajero
-Borrar Pasajero
-Buscar Pasajero por Nombre
-Buscar Pasajero por número de pasaporte
-Mostrar la lista de pasajeros (deberán aplicar algún formato de tablas donde la
información se muestre de forma ordenada y prolija)
-Mostrar estadísticas por edades: Deberá imprimir la edad más común (mayor cantidad
de repeticiones) y el promedio
-Salir

Requerimientos:
1) El programa deberá validar que los datos ingresados sean del tipo correcto.
2) Deberá estar modularizado en funciones.
3) Debe ser posible agregar múltiples pasajeros en una sola sesión del programa
antes de salir.
4) Si un pasajero se repite (nombre y nro. pasaporte) se deberá mostrar un
mensaje de error indicando que ese pasajero ya existe.

----------------------------------------17/9--------------------------------------------------------
Crear un bucle infinito que debería por cada punto de las consignas tener un función
correspondiente que resuelva cada uno de estos.

1. Mostrar menú de opciones para cada uno de los siguientes puntos
2. Pedir un número entero.
3. Validar numero que el número esté entre -500 y 500
4. En una función cargar una lista de 20 números a partir de números aleatorios
generados desde -1000 a 1000 pero agregar a la lista solamente números entre -500
y 500.
Con la lista generada en el punto anterior realizar los siguientes puntos.
5. Crear una función que determina mediante un booleano si el número es par o impar
6. Crear una función que determina mediante un booleano si el número es positivo o
negativo
7. Crear una función que determine la sumatoria de los pares de la lista.
8. Crear una función que encuentre el mayor de los impares.
9. Crear una función que encuentre el menor de los pares
10. Crear una función que devuelva un diccionario con mayor de los impares, menor de
los pares y el promedio de los números en la lista.
11. Crear una función que muestre cada uno de los puntos anteriormente definidos.

----------------------------------------30/9-------------------------------------------------------
VER CLASE GERMAN , LISTA QUE SE USO EXPLICACION: lista_productos_str = [
    "1, coca cola, 100, 1.50,2021-04-29",
    "2, pepsi, 75, 1.25, 2022-05-28",
    "3, sprite, 50, 1.75, 2021-09-27",
    "4, 7up, 60, 1.40, 2022-10-26",
    "5, fanta, 80, 1.60,2023-12-25  ",
    "6, mountain dew, 70, 1.70, 2023-09-24   ",
    "7, dr pepper, 45, 1.90, 2022-09-23",
    "8, mirinda, 55, 1.45, 2023-03-22",
    "9, tonic, 30, 2.00, 2021-03-21",
    "10, soda, 65, 1.35, 2020-09-20",
    "11, ginger ale, 40, 1.85, 2023-09-19",
    "12,  root beer,35, 2.10, 2023-09-18",
    "13, cream soda, 25, 2.25, 2020-02-17",
    "14, lemon-lime, 20, 2.30, 2023-02-16",
    "15, orange soda, 55, 1.55, 2023-09-15"
]

NO HAY RELACION ENTRE EL EJERCICIO DE LA CLASE Y EL EJERCICIO EXTRA, SALVO EL TEMA A TRATAR.

EJERCICIO EXTRA:
Inscripcion alumnos

-legajo int
-nombre str
-fecha datetime

1. normalizar los datos
2. cada alumno tendra una nota final. No esta en la lista de strings (tiene que sea aleatoria) 1-10
3. solo mostrar los alumnos que rindieron en 2020, que aprobaron el final con nota 6 o superior.

"""