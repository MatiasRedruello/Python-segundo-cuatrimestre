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
white = (0,0,0)
black = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
#Reloj
clock = pygame.time.Clock()
fps = 60
#Posicion figuras
    #ciculos
circle_x = 0
circle_y = screen_heigth // 2
circle_radius = 50
    # rectangulo
rect_x = 0
rect_y = 0
rect_width = screen_width // 5
rect_heigth = screen_heigth // 5

# Velocidad de movimiento
speed = 2
# Dirección inicial del movimiento (derecha)
direction = 1


# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Borrar pantalla
    screen.fill(red)
    # mover posicion del rectangulo
    rect_x += speed * direction
    # mover posicion circulo
    circle_x += speed * direction
    # Cambiar de sentido al chocar con el borde
    if rect_x <= 0 or rect_x >= screen_width - rect_width:
        direction *= -1


    # dibujar pantalla    

    # Logica del juegos
    pygame.draw.circle(screen,blue,(circle_x,circle_y),circle_radius,5)
    pygame.draw.rect(screen,green,(rect_x,rect_y,rect_width,rect_heigth),2)
    

    # Actualizar pantalla
    pygame.display.update()
    # Limitar velocidad
    clock.tick(fps)

# filnalizar pygame
pygame.quit()
sys.exit()