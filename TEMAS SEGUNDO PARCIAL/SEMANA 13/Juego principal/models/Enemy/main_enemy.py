from models.auxiliar import SurfaceManager as sf
import pygame as pg
from models.constantes import ANCHO_VENTANA, DEBUG


class enemigo:
    def __init__(self,coord_x, coord_y, frame_rate = 100, speed_walk = 6, speed_run = 12, gravity = 16) -> None:
        self.__iddle_r = sf.get_surface_from_spritesheet('./assets/img/enemy/walk/npc_batterfly__x1_profile_turned_png_1354831846.png', 8, 5,2)
        self.__iddle_l = sf.get_surface_from_spritesheet('./assets/img/enemy/walk/npc_batterfly__x1_profile_turned_png_1354831846.png', 8, 5,2, flip=True)
        self.__walk_r = sf.get_surface_from_spritesheet('./assets/img/enemy/walk/npc_batterfly__x1_profile_turned_png_1354831846.png', 8, 5)
        self.__walk_l = sf.get_surface_from_spritesheet('./assets/img/enemy/walk/npc_batterfly__x1_profile_turned_png_1354831846.png', 8, 5, flip=True)
        self.__move_x = coord_x # Coordenada en x(ojo que se puede usar en el movimieno)
        self.__move_y = coord_y # Coordenada en yojo que se puede usar en el movimieno)
        self.__speed_walk = speed_walk # Velodidad con la que camina
        self.__frame_rate = frame_rate # Cuadros por segundo
        self.__player_move_time = 0  # preseteo  cada cuanto tiempo puedo realizar un movimiento
        self.__player_animation_time = 0 # Tiempo que vamos a usar para la animacion
        self.__gravity = gravity # Fuerza de gravedad 
        self.__initial_frame = 0 # Cuadro incial en cero (el primero)
        self.__actual_animation = self.__iddle_l # Es la lista de animacion con la que el personaje arranca
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]# Primera imagen
        self.__rect = self.__actual_img_animation.get_rect() # Rectangulo de la primera imagen
        self.__is_looking_right = True        
