import pygame

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y,rect_width,rect_height,bullet_width,bullet_height,lado="rigth"):
        self.bullet_image = pygame.image.load('C:/Users/PC/OneDrive/Documents/GitHub/Python-segundo-cuatrimestre/TEMAS SEGUNDO PARCIAL/Practica py game/pygame_juego_figuras.py/Power/gema_roja.png').convert_alpha()
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height
        self.image = pygame.transform.scale(self.bullet_image, (self.bullet_width, self.bullet_height))
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.rect = self.image.get_rect()
        self.rect.center = (x+(rect_width//2), y+(rect_height//2))
        self.speed_x = 5
        self.lado = lado

    def do_shoot(self):
        if self.lado == "rigth":
            self.rect.x += self.speed_x
        elif self.lado == "left":
            self.rect.x += -self.speed_x     

    def update(self):
        self.do_shoot()
