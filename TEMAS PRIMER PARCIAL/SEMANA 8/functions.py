import json
"""
1 - mostrar en consola los primeros N videos
2 - Exportar lista de videos con mas de 20K vistas. [csv]
3 - Exportar lista de videos de mas de 60 min. [csv]
4 - Exportar datos de video con mas vistas. [txt]
5 - Exportar lista de videos. [csv]
6 - Filtrar y exportar videos de milanesas. [json]
7 - Salir
"""
# py -m pip install -r ./Archivos/requirements.txt
ROOT_DIR = './Archivos/'
# C:\Users\Administrator\Desktop\Python\Python_UTN_LaboI\Archivos
# Archivos

texto = 'Escribi un archivo usando Python'

ruta_archivo = f'EJERCICIOS EXTRA CLASE SABADO/Ejercicio pasajeros/pasajeros.json'

archivo = open(ruta_archivo, 'a', encoding = 'utf-8')


#for linea in archivo:
    #print(linea)


archivo.close()