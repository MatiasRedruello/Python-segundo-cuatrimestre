import json
from funciones_archivos import ROOT_DIR,leer_archivo_json
from funciones_menu import stark_marvel_app_ordenamiento

lista_personajes = leer_archivo_json(f"{ROOT_DIR}data_stark.json","heroes")
stark_marvel_app_ordenamiento(lista_personajes,ROOT_DIR)

