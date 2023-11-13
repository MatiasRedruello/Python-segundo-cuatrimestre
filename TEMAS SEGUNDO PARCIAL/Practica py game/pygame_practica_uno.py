import  pygame
import sys

# Iniciar pygame
pygame.init()
# Configuracion pantalla
screen_width = 500
screen_heigth = 500
screen= pygame.display.set_mode((screen_width,screen_heigth))
pygame.display.set_caption("Figuras geometricas")
# Colores
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
#Reloj
clock = pygame.time.Clock()
fps = 60
#propiedades
x = 0
y = screen_heigth - 30
rect_width = 20
rect_heigth = 20
rect_speed_x = 5
rect_speed_y = 0
gravity = 1
jumping = True
jump_cout = 10


# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #detectar la tela
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not jumping:
            jumping = True
    # simular gravedad
    rect_speed_y += gravity
    y += rect_speed_y

    # controlar el salto
    if jumping:
        jump_cout -= 1
        y -= jump_cout
        if jump_cout <= 0:
            jumping = False
            jump_cout = 10
    # Evitar que el rectángulo salga de la parte inferior de la pantalla
    if y > screen_heigth - rect_heigth:
        y = screen_heigth - rect_heigth
        jumping = False
        jump_count = 10  # Restablece el contador si toca el suelo
        
    """
 ------------------------------------------------------------------------   
    #Movimiento automatico
    # Actualizar la posición del cuadrado
    # tiene que ser condiciones separas no un if-elif
    
    # se mueve a la derecha
    if x >= 0:
        x += rect_speed_x
            
    # Cambiar de dirección al llegar a los bordes de la pantalla 
    if x <= 0 or x >= screen_width - rect_width:
        rect_speed_x *= -1
    # Baja cada vez que choca
    if x >= screen_width - rect_width or x <= 0:
        y += rect_speed_y 
    
    # tendria que subir

    if y >= screen_heigth - rect_heigth:
        y = 0 
----------------------------------------------------------------------------        
    """  
    

    #color pantalla
    screen.fill(white)
    # crear figura
    pygame.draw.rect(screen,red,(x,y,rect_width,rect_heigth))    
    # Actualizar pantalla
    pygame.display.update()
    # Limitar velocidad
    clock.tick(fps)

# filnalizar pygame
pygame.quit()
sys.exit()