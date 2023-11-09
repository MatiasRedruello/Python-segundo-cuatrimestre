import json
from funciones_archivos import leer_archivo_json,ROOT_DIR
from funciones_menu import stark_marvel_app_5

lista_personajes = leer_archivo_json(f"{ROOT_DIR}data_stark.json","lista_heroes")
stark_marvel_app_5(lista_personajes)
