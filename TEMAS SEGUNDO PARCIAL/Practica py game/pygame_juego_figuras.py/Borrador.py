import pygame
import sys
from clase_proyectil import Proyectil

pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Salto de un Rectángulo')

white = (255, 255, 255)

# Color y dimensiones del rectángulo
rect_color = (0, 0, 255)  # Azul en formato RGB
rect_width = 50
rect_height = 50

# Color y dimensiones del proyectil
bullet_image = pygame.image.load('Power/gema_roja.png')
bullet_width = 30
bullet_height = 15

class Jugador(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.rect_width = x
        self.rect_height = y
        self.image = pygame.Surface((self.rect_width, self.rect_height))
        self.image.fill(rect_color)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - self.rect_height//2)
        self.speed_x = 10
        self.rect_speed_y = 0
        self.gravity = 1
        self.jump_force = 0
        self.jumping = False
        
        
    def do_move(self,lado= ""):
        if lado == "left":
            self.rect.x += -self.speed_x
            if self.rect.x < 0:
                self.rect.x += self.speed_x
        elif lado == "right":
            self.rect.x += self.speed_x
            if self.rect.x > screen_width - self.rect_width:
                self.rect.x += -self.speed_x 
                
    def do_jump(self):
        if self.jumping:
            self.jump_force += self.gravity
            self.rect.y += self.jump_force
        if self.rect.y >= screen_height - self.rect_height :
            self.rect.y =  screen_height - self.rect_height
            self.jumping = False
                
    def update(self):
        self.do_move()
        self.do_jump()

    

# Lista para almacenar los proyectiles
bullets = pygame.sprite.Group()

# Crear el jugador
jugador = Jugador(rect_width,rect_height)

#clock
clock = pygame.time.Clock()
fps = 60

# Bucle principal del juego
running_game = True
jumping = False
while running_game:
    letras_precionadas = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jugador.jumping = True
                jugador.jump_force = -20

            if event.key == pygame.K_d:
                nuevo_proyectil = Proyectil(jugador.rect.x, jugador.rect.y, True)
                bullets.add(nuevo_proyectil)

            if event.key == pygame.K_a:
                nuevo_proyectil = Proyectil(jugador.rect.x, jugador.rect.y, False)
                bullets.add(nuevo_proyectil)

    if letras_precionadas[pygame.K_LEFT] and not letras_precionadas[pygame.K_RIGHT]:
        jugador.do_move("left")
        
    if letras_precionadas[pygame.K_RIGHT] and not letras_precionadas[pygame.K_LEFT]:
        jugador.do_move("right")
        

    # Actualizar jugador y proyectiles
    jugador.update()
    bullets.update()

    # Dibujar el fondo
    screen.fill(white)

    # Dibujar el jugador y los proyectiles
    screen.blit(jugador.image, jugador.rect)
    bullets.draw(screen)

    pygame.display.update()
    clock.tick(fps)

# Salir de Pygame
pygame.quit()
sys.exit()
