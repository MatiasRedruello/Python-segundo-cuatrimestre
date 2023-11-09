def formatear_puntaje(puntaje: str) -> str:
    return str(puntaje).zfill(5)

def formatear_nombre_jugador(nombre: str) -> str:
    lista_nombres = nombre.strip().lower().capitalize().split(" ")
    return lista_nombres[0]