# este burbujero ordena del final al principio, reduce el indice final y el swich es con el adyacente 
def bubble_sort(arr):
    n = len(arr)  # Obtiene la longitud del arreglo
    for i in range(n):  # Itera a través de los elementos del arreglo
        for j in range(0, n - i - 1):  # Itera a través de los elementos no ordenados
            if arr[j] > arr[j + 1]:  # Compara elementos adyacentes
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambia los elementos si están en el orden incorrecto
            print(arr)       

# este burbujero ordena de el principio al final, aumenta el inidice inicial y el swich es en saltos
def ordenar_burbujeo(lista_numeros: list[int]):
    if not lista_numeros:
        print('La lista esta vacia')
    else:
        lista_copia = lista_numeros.copy()
        # Arranca nuestro algoritmo
        for indice_1 in range(len(lista_copia) - 1):
            for indice_2 in range(indice_1 + 1, len(lista_copia)):
                if lista_copia[indice_1] > lista_copia[indice_2]:
                    lista_copia[indice_1], lista_copia[indice_2] =\
                    lista_copia[indice_2], lista_copia[indice_1]
                print(lista_copia)
        return lista_copia
# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
#bubble_sort(arr)
#ordenar_burbujeo(arr)
#print("Arreglo ordenado:", arr)
#Nota: Bubble sort ordena una lista a partir de dos iteraciones simultaneas, realizando un swich entre los numeros ordenandolos.
# la primera iteracion marca el ritmo , esto quiere decir que si tengo 6 elemento va a recorrer la lista 5 veces.
# la segunda iteracion es la que te marca el cambio de lugar de los elementos entre el indice uno y el indice dos en caso de que sea posible
# por lo tanto una lista con 6 elementos va a realizar 5 vueltas: la primera vuelta compara el numero con idice 0 con el resto
# en el caso de que se pueda se cambia ej: 8341 -> 3841 -> 3841 -> 1843 (primmera vuetla)
#                                          1843 -> 1483 -> 1384  segunda vuelta 
#                                          1384 -> 1348 tercera vuetla
# a medida que se avanza en catidad de vueltas se reducen los numero a recorrer ya que los anteriores al indice acutal ya estan ordenados.                                       
"""
1) def bubble_sort(arr):: Esto define una función llamada bubble_sort que toma un arreglo arr como argumento.

2) n = len(arr): Calculamos la longitud del arreglo y la almacenamos en la variable n. Esto nos dará el número de elementos en el arreglo.

3) for i in range(n): Iniciamos un bucle externo que itera a través de los elementos del arreglo. Este bucle se ejecutará n veces, una vez por cada elemento 
del arreglo.

4)for j in range(0, n - i - 1):: Dentro del bucle externo, iniciamos otro bucle interno que itera a través de los elementos no ordenados del arreglo. n - i - 1 es 
el número de elementos no ordenados en cada iteración. En cada iteración, estamos seguros de que el elemento más grande se ha movido a la última posición, por lo 
que no es necesario volver a compararlo.

5)if arr[j] > arr[j + 1]:: Comparamos el elemento actual arr[j] con el siguiente elemento arr[j + 1] para ver si están en el orden incorrecto. Si el elemento 
actual es mayor que el siguiente, significa que están en el orden incorrecto y deben intercambiarse.

6)arr[j], arr[j + 1] = arr[j + 1], arr[j]: Si los elementos están en el orden incorrecto, los intercambiamos utilizando una tupla de asignación. Esto es lo que
 hace que los elementos se "burbujeen" hacia la posición correcta.

7)Después de que el bucle externo e interno haya terminado de ejecutarse, el arreglo estará ordenado de forma ascendente. El elemento más grande estará en la última 
posición, y el proceso se repite para los elementos restantes hasta que todo el arreglo esté ordenado.

El algoritmo de Bubble Sort es simple de entender, pero no es eficiente para arreglos grandes, ya que requiere un número cuadrático de comparaciones e 
intercambios en el peor caso. Sin embargo, es útil para propósitos educativos y para arreglos pequeños.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Arreglo ordenado:", arr)

"""
1)def selection_sort(arr):: Esto define una función llamada selection_sort que toma un arreglo arr como argumento.

2)n = len(arr): Obtenemos la longitud del arreglo y la almacenamos en la variable n. Esto nos proporciona el número de elementos en el arreglo.

3)for i in range(n):: Iniciamos un bucle externo que itera a través de los elementos del arreglo. Este bucle se ejecutará n veces, una vez por cada elemento del 
arreglo.

4)min_idx = i: Inicializamos una variable min_idx para llevar un seguimiento del índice del elemento más pequeño en el subarreglo no ordenado.

5)for j in range(i + 1, n):: Iniciamos un bucle interno que itera a través de los elementos no ordenados del arreglo, empezando desde i + 1.

6)if arr[j] < arr[min_idx]:: Comparamos el elemento actual arr[j] con el elemento más pequeño conocido arr[min_idx]. Si encontramos un elemento más pequeño, 
actualizamos min_idx con el nuevo índice del elemento más pequeño.

7)arr[i], arr[min_idx] = arr[min_idx], arr[i]: Una vez que hemos encontrado el elemento más pequeño en el subarreglo no ordenado, lo intercambiamos con el 
elemento en la posición i. Esto coloca el elemento más pequeño en su posición ordenada.

Repetimos este proceso para cada elemento del arreglo hasta que todo el arreglo esté ordenado de manera ascendente. El elemento más pequeño se coloca en la 
primera posición, el segundo elemento más pequeño en la segunda posición, y así sucesivamente.
"""
# Este quick sort funciona con listas que tengan datos comparables, numeros,str,etc.El pivot es elemento del medio de la lista
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Este quick sort funciona con listas que contenga diccionarios, el pivot es el ultimo elemento 
def quick_sort(lista: list[dict], key):

    if len(lista) < 2:
        return lista
    else:
        lista_copia = lista.copy()
        heroe_pivot = lista_copia.pop()
        mas_grandes = []
        mas_chicos = []

        for heroe in lista_copia:
            if heroe[key] > heroe_pivot[key]:
                mas_grandes.append(heroe)
            elif heroe[key] <= heroe_pivot[key]:
                mas_chicos.append(heroe)
        return quick_sort(mas_chicos, key) + [heroe_pivot] + quick_sort(mas_grandes, key)
    
# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("Arreglo ordenado:", sorted_arr)

"""
1)def quick_sort(arr):: Esto define una función llamada quick_sort que toma un arreglo arr como argumento.

2)if len(arr) <= 1:: Esto es la condición de parada para la recursión. Si el arreglo tiene 1 elemento o ninguno, se considera ordenado y se devuelve sin cambios.

3)pivot = arr[len(arr) // 2]: Seleccionamos un elemento del arreglo como pivote. En este ejemplo, tomamos el elemento en la mitad del arreglo.

4)left = [x for x in arr if x < pivot]: Creamos una lista left que contiene todos los elementos menores que el pivote.

5)middle = [x for x in arr if x == pivot]: Creamos una lista middle que contiene todos los elementos iguales al pivote.

6)right = [x for x in arr if x > pivot]: Creamos una lista right que contiene todos los elementos mayores que el pivote.

7)return quick_sort(left) + middle + quick_sort(right): Llamamos recursivamente a quick_sort en los subarreglos left y right, y luego combinamos los resultados 
junto con el arreglo middle. Esto da como resultado un arreglo ordenado.

El algoritmo de Quick Sort utiliza la técnica de "divide y conquista" para ordenar el arreglo de manera eficiente, dividiendo el arreglo en subarreglos más 
pequeños y ordenándolos por separado.
"""