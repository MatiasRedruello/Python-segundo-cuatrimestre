import pygame
import sys

pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Salto y Disparo de un Rectángulo')

# Color y dimensiones del rectángulo principal
rect_color = (0, 0, 255)  # Azul en formato RGB
rect_width = 50
rect_height = 50

# Posición y velocidad inicial del rectángulo principal
player_x = screen_width // 2 - rect_width // 2
player_y = screen_height - rect_height
player_speed_y = 0  # Velocidad inicial en el eje Y
player_speed_x = 10

gravity = 1  # Fuerza de gravedad
jump_height = 15  # Altura máxima del salto

# Color y dimensiones del proyectil
bullet_color = (255, 0, 0)  # Rojo en formato RGB
bullet_width = 10
bullet_height = 10

# Lista para almacenar los proyectiles
bullets = []

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()
fps = 60

# Bucle principal del juego
jumping = False
jump_count = jump_height  # Controla la altura del salto
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detecta la tecla de espacio para activar el salto
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not jumping:
            jumping = True
            player_speed_y = -jump_height  # Configura la velocidad inicial del salto

    
    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x += player_speed_x
        if player_x > screen_width - rect_width:
            player_x = screen_width - rect_width
    if keys[pygame.K_LEFT]:
        player_x -= player_speed_x
        if player_x < 0:
            player_x = 0

    # Simular la gravedad
    player_speed_y += gravity
    player_y += player_speed_y

    # Controlar el salto
    if player_y >= screen_height - rect_height:
        player_y = screen_height - rect_height
        jumping = False
        player_speed_y = 0  # Reinicia la velocidad vertical si toca el suelo

    # Detecta la tecla 'd' para activar el disparo
    if keys[pygame.K_d]:
        bullets.append([player_x + rect_width // 2 - bullet_width // 2, player_y - bullet_height])

    # Mover y dibujar los proyectiles
    for bullet in bullets:
        bullet[1] -= 10  # Velocidad de movimiento del proyectil
        pygame.draw.rect(screen, bullet_color, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Eliminar proyectiles fuera de la pantalla
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # Dibujar el fondo
    screen.fill((255, 255, 255))  # Color blanco como fondo

    # Dibujar el rectángulo principal en su nueva posición
    pygame.draw.rect(screen, rect_color, (player_x, player_y, rect_width, rect_height))

    # Actualizar la pantalla
    pygame.display.update()
    clock.tick(fps)

# Salir de Pygame
pygame.quit()
sys.exit()

