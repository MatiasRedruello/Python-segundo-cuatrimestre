from functions import (
    ROOT_DIR
)


def paulinApp(videos_list: list[dict]):
    """
    The function `paulinApp` is a Python function that takes a list of dictionaries representing videos
    as input and provides a menu-driven interface to perform various operations on the videos.
    
    :param videos_list: The `videos_list` parameter is a list of dictionaries. Each dictionary
    represents a video and contains information about the video such as its title, views, duration, etc
    """
    
    option_selected = choose_option()
    while True:
        match option_selected:
            case 1: #1 - mostrar en consola los primeros N videos
                pass
            case 2: #2 - Exportar lista de videos con mas de 20K vistas. [csv]
                pass
            case 3: #3 - Exportar lista de videos de mas de 60 min. [csv]
                pass
            case 4: #4 - Exportar datos de video con mas vistas. [txt]
                pass
            case 5: #5 - Exportar lista de videos. [csv]
                pass
            case 6: #6 - Filtrar y exportar videos de milanesas. [json]
                pass
            case 7: #7 - Salir
                break

if __name__ == "__main__":
    lista_videos = abrir_archivo(path = '', mode = '', key = '')
    paulinApp(lista_videos)