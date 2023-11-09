import pygame as pg # import pygamen y lo guardo en pg
from models.constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)
from models.player.main_player import Jugador

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) # seteo vent ana
pg.display.set_caption("PyGame DragonBall")# seteo el titulo

pg.init()# inicio pyga mes
clock = pg.time.Clock()# creo un reloj

back_img = pg.image.load('./assets/img/background/goku_house.png')# Cargo imagen de fondo
back_img = pg.transform.scale(back_img, (ANCHO_VENTANA, ALTO_VENTANA))#Adapto imagen a la pantalla 


juego_ejecutandose = True

vegeta = Jugador(0, 0, frame_rate=70, speed_walk=20, speed_run=40)#In stacio jugador

#Bucle principal
while juego_ejecutandose:
    
    #print(delta_ms)
    lista_eventos = pg.event.get() #Guardo eventos en una variable
    for event in lista_eventos:#Recorro eventos
        match event.type:# Traigo el tipo de evento y macheo
            case pg.KEYDOWN: 
                if event.key == pg.K_SPACE: # Si se preciona la barra espaciadora
                    vegeta.jump(True) #Paso true al metodo jump de la clase jugador
            # case pg.KEYUP:
            #     if event.key == pg.K_SPACE:
            #         print('Estoy SOLTANDO el espacio')
            case pg.QUIT:# Si se preciona  quit se termina el juego
                print('Estoy CERRANDO el JUEGO')
                juego_ejecutandose = False
                break
    
    lista_teclas_presionadas = pg.key.get_pressed()# Lista con las teclas que son presionadas
    if lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:#Si presiono derecha y no esta presionada izquierda
        vegeta.walk('Right')# le paso derecha el metodo de la clse jugador
    if lista_teclas_presionadas[pg.K_LEFT] and not lista_teclas_presionadas[pg.K_RIGHT]:# lo inverso y proporcional 
        vegeta.walk('Left')
    if not lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:# si no toco derecha o izquierda
        vegeta.stay()
    
    if lista_teclas_presionadas[pg.K_RIGHT] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_LEFT]:
        #Si toco deerecha y shift y no izqui erda
        vegeta.run('Right')
    if lista_teclas_presionadas[pg.K_LEFT] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        # lo inverso y proporcional 
        vegeta.run('Left')
    
        
    
    screen.blit(back_img, back_img.get_rect()) # Esta forma es útil cuando deseas que la imagen ocupe toda la pantalla o mantener su tamaño y posición originales.
    delta_ms = clock.tick(FPS) # Representa el tiempo en milisegundos transcurrido desde el último fotograma.
    vegeta.update(delta_ms) # Controla la velocidad de ejecución actualizando constantemente
    vegeta.draw(screen) # Dibujo a el personaje en pantalla
    pg.display.update() # Se actualiza el programa

pg.quit()