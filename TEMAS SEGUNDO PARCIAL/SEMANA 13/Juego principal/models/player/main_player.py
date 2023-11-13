from models.auxiliar import SurfaceManager as sf
import pygame as pg
from models.constantes import ANCHO_VENTANA, DEBUG


class Jugador:

    def __init__(self, coord_x, coord_y, frame_rate = 100, speed_walk = 6, speed_run = 12, gravity = 16, jump = 32):
        # Se guardan los sprites en c/u de los atributos correspondientes
        self.__iddle_r = sf.get_surface_from_spritesheet('./Juego principal/img/player/iddle/player_idle.png', 5, 1)
        self.__iddle_l = sf.get_surface_from_spritesheet('./Juego principal/img/player/iddle/player_idle.png', 5, 1, flip=True)
        self.__walk_r = sf.get_surface_from_spritesheet('./Juego principal/img/player/walk/player_walk.png', 6, 1)
        self.__walk_l = sf.get_surface_from_spritesheet('./Juego principal/img/player/walk/player_walk.png', 6, 1, flip=True)
        self.__run_r = sf.get_surface_from_spritesheet('./Juego principal/img/player/run/player_run.png', 2, 1)
        self.__run_l = sf.get_surface_from_spritesheet('./Juego principal/img/player/run/player_run.png', 2, 1, flip=True)
        self.__jump_r = sf.get_surface_from_spritesheet('./Juego principal/img/player/jump/player_jump.png', 6, 1)
        self.__jump_l = sf.get_surface_from_spritesheet('./Juego principal/img/player/jump/player_jump.png', 6, 1, flip=True)
        self.__move_x = coord_x # Coordenada en x(ojo que se puede usar en el movimieno)
        self.__move_y = coord_y # Coordenada en yojo que se puede usar en el movimieno)
        self.__speed_walk = speed_walk # Velodidad con la que camina
        self.__speed_run = speed_run # Velodidad con la que corre
        self.__frame_rate = frame_rate # Cuadros por segundo
        self.__player_move_time = 0  # preseteo  cada cuanto tiempo puedo realizar un movimiento
        self.__player_animation_time = 0 # Tiempo que vamos a usar para la animacion
        self.__gravity = gravity # Fuerza de gravedad 
        self.__jump = jump # Fuerza de salto
        self.__is_jumping = False  # Indica que esta saltando, por defecto no
        self.__initial_frame = 0 # Cuadro incial en cero (el primero)
        self.__actual_animation = self.__iddle_r # Es la lista de animacion con la que el personaje arranca
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]# Primera imagen
        self.__rect = self.__actual_img_animation.get_rect() # Rectangulo de la primera imagen
        self.__is_looking_right = True #Indica que esta mirando hacia al derecha, por defecto si

    
    def __set_x_animations_preset(self, move_x, animation_list: list[pg.surface.Surface], look_r: bool):
        """
        self: Por defecto
        move_x: Lo que me puedo mover en x.
        animation_list: Lista de animaciones.
        look_r: Me indica si miero a la izquierda o derecha, es un bool

        Funcion:
        Controla si esta caminando
        """
        self.__move_x = move_x 
        self.__actual_animation = animation_list
        self.__is_looking_right = look_r
        
    
    def __set_y_animations_preset(self):
        """
        self: Por defecto
        move_x: Lo que me puedo mover en x.
        animation_list: Lista de animaciones.
        look_r: Me indica si miero a la izquierda o derecha, es un bool

        Descripcion:
        Controla si esta saltando y en que direccion lo hace
        """        
        self.__move_y = -self.__jump # En la y resto pixeles. Ej si mi personaje salta
        self.__move_x = self.__speed_run if self.__is_looking_right else -self.__speed_run
        self.__actual_animation = self.__jump_r if self.__is_looking_right else self.__jump_l
        self.__initial_frame = 0
        self.__is_jumping = True
    
    def walk(self, direction: str = 'Right'):
        """
        self: Por defecto
        direccion: Es un str por defecto es hacia ala derecha
        Descripcion:
        Permite que el personaje camine, utiliza la funcion de preset
        """           
        match direction:
            case 'Right':
                look_right = True
                self.__set_x_animations_preset(self.__speed_walk, self.__walk_r, look_r=look_right)
            case 'Left':
                look_right = False
                self.__set_x_animations_preset(-self.__speed_walk, self.__walk_l, look_r=look_right)
    
    def run(self, direction: str = 'Right'):
        self.__initial_frame = 0
        match direction:
            case 'Right':
                look_right = True
                self.__set_x_animations_preset(self.__speed_run, self.__run_r, look_r=look_right)
            case 'Left':
                look_right = False
                self.__set_x_animations_preset(-self.__speed_run, self.__run_l, look_r=look_right)
    
    def stay(self):
        """
        self: Por defecto
        Descripcion:
        Permite que el personaje este quieto si no hay ninguna otra animacion distinta a iddle activa
        """          
        if self.__actual_animation != self.__iddle_l and self.__actual_animation != self.__iddle_r:#no es ninguna de las otras y es iddle l o r
            self.__actual_animation = self.__iddle_r if self.__is_looking_right else self.__iddle_l
            self.__initial_frame = 0
            self.__move_x = 0
            self.__move_y = 0
    
    def jump(self, jumping=True):
        if jumping and not self.__is_jumping:
            self.__set_y_animations_preset()
        else:
            self.__is_jumping = False
            self.stay()
    
    def __set_borders_limits(self):
        """
        self: Por defecto

        Descripcion:
        Determina hasta donde se puede mover el personaje y cuando llegue al limite de pantalla no lo permita
        """        
        pixels_move = 0
        if self.__move_x > 0:# estoy en movimiento,no estoy en stey
            pixels_move = self.__move_x if self.__rect.x < ANCHO_VENTANA - self.__actual_img_animation.get_width() else 0
        elif self.__move_x < 0:
            pixels_move = self.__move_x if self.__rect.x > 0 else 0
        return pixels_move


    def do_movement(self, delta_ms):
        """
        self: Por defecto
        delta_ms: Permite controla la ejecucion de una aniacion 
        Descripcion:
        Controlo el movimiento, cada cuanto tiempo voy a generar esa inimacion manejando las coordenadas directamente en el rectangulo de la imagen
        """        
        self.__player_move_time += delta_ms # al preseteo en 0 le sumo el delta (la diferencia del tiempo) por cada vuelta
        if self.__player_move_time >= self.__frame_rate: # esto quiere dicr que ya estamos en un tiempo produnte para realizar un movimiento
            self.__player_move_time = 0 # reinicio
            self.__rect.x += self.__set_borders_limits()#le sumo los pixeles al rectangulo de mi imagen hasta que choque contra los bordes
            self.__rect.y += self.__move_y # cin la i no seria necesario porque tengo que limitar el salto
            # Parte relacionado a saltar
            if self.__rect.y < 300:
                self.__rect.y += self.__gravity

    def do_animation(self, delta_ms):
        """
        self: Por defecto
        delta_ms: Permite controla la ejecucion de una aniacion 
        Descripcion:
        Controla el teimpo de animacion y ademas permite que se pase de una imagen a la siguiente
        """        
        self.__player_animation_time += delta_ms 
        if self.__player_animation_time >= self.__frame_rate:
            self.__player_animation_time = 0
            # en initial frame se guarda un numero del indice de la imagen que queremos mostrar
            if self.__initial_frame < len(self.__actual_animation) - 1: # mientras ese indice es menor al ultimo indice de la imagen sumo uno
                self.__initial_frame += 1
            else:
                self.__initial_frame = 0#reiniciamos
                # if self.__is_jumping:
                #     self.__is_jumping = False
                #     self.__move_y = 0
    
    def update(self, delta_ms):
        """
        self: Por defecto
        delta_ms: Permite controla la ejecucion de una aniacion 
        Descripcion:
        Llama do_movement y do_animation para pasarle poder controlar las animaciones
        """            
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
    
    def draw(self, screen: pg.surface.Surface):
        """
        self: Por defecto
        screen: Recibe la pantalla
        Descripcion:
        Agarramos una imagen y la fundimos en la pantalla
        """        

        if DEBUG:
            pg.draw.rect(screen, 'red', self.__rect)
            #pg.draw.rect(screen, 'green', self.__rect.bottom)
            
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]#Traemos la imagen actual
        screen.blit(self.__actual_img_animation, self.__rect) #fundimos el rectangulo en la pantalla