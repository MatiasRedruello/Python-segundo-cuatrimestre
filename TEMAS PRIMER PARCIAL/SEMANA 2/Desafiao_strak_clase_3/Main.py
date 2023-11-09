from Data_stark import lista_personajes
from Desafio_strak_00 import *

while True:
    
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Nombres de los miembros")
    print("2. Nombres de los miembros y su altura")
    print("3. Superheroe mas alto")
    print("4. Superheroe mas bajo")
    print("5. El promedio de las alturas")
    print("6. Identidad del superheroe mas y menos alto")
    print("7. Superheroe menos y mas pesado")
    print("0. Salir del programa")

    opcion = input("\nIngrese la opción deseada: ")

    respuesta_nombres = nombre(lista_personajes,opcion)
    respuesta_nombre_y_altura = nombre_y_altura(lista_personajes,opcion)
    respuesta_altura_promedio = "La altura promedio es: {0}".format(altura_promedio(lista_personajes))
    respuesta_mas_alto = lista_personajes[calcular_mas_alto(lista_personajes)]["altura"] 
    respuesta_mas_bajo = lista_personajes[calcular_mas_bajo(lista_personajes)]["altura"]
    respuesta_identidad = identidad(lista_personajes,respuesta_mas_alto,respuesta_mas_bajo)
    respuesta_pesos = pesos(lista_personajes)
    
    match opcion:
        case "1":
            
            print(respuesta_nombres)
        case "2":
            
            print(respuesta_nombre_y_altura)
        case "3":
             
            print(respuesta_mas_alto)
        case "4":
             
            print(respuesta_mas_bajo)
        case "5":
             
            print(respuesta_altura_promedio)
        case "6":
            
            print(respuesta_identidad)
        case "7":
            
            print(respuesta_pesos)    
        case "0":
            break