"""
1) pygame.init(): Esta función inicializa Pygame. Debe ser llamada al comienzo de cualquier programa de Pygame antes de usar cualquier otra función de Pygame.

2) pygame.quit(): Cierra Pygame y libera los recursos utilizados. Debe ser llamada al finalizar el programa para asegurarse de que todos los recursos se liberan correctamente.

3)  pygame.display.set_mode(): Crea una ventana o pantalla donde se mostrará el juego o la aplicación. Puedes especificar el tamaño de la ventana y otras opciones.

4)  pygame.display.set_caption(): Establece el título de la ventana.

5)  pygame.event.get(): Devuelve una lista de todos los eventos que han ocurrido desde la última vez que se llamó a esta función. Es útil para manejar eventos como presionar teclas, hacer clic en el ratón, etc.

6)  pygame.draw.rect(): Dibuja un rectángulo en la pantalla. Puedes especificar las coordenadas, tamaño y color del rectángulo.

7)  pygame.draw.circle(): Dibuja un círculo en la pantalla. Puedes especificar las coordenadas del centro, el radio y el color del círculo.

8)  pygame.draw.line(): Dibuja una línea en la pantalla. Puedes especificar las coordenadas de inicio y fin, y el color de la línea.

9)  pygame.image.load(): Carga una imagen desde un archivo en memoria para su uso en el juego.

10)  pygame.image.get_rect(): Obtiene el rectángulo que rodea una imagen cargada, lo que facilita su manipulación y posicionamiento en pantalla.

11) pygame.key.get_pressed(): Devuelve una lista de booleanos que indican si cada tecla está siendo presionada en ese momento. Útil para el control de teclas.

12) pygame.mouse.get_pos(): Devuelve las coordenadas (x, y) del cursor del ratón en la ventana.

13) pygame.time.Clock(): Crea un objeto Clock que se utiliza para controlar la velocidad de fotogramas del juego, lo que permite mantener una tasa de cuadros por segundo constante.

14) pygame.mixer.Sound(): Crea un objeto de sonido que se puede reproducir en el juego. Útil para efectos de sonido.

15) pygame.mixer.music.load(): Carga una pista de música para su reproducción en el juego.

16) pygame.mixer.music.play(): Inicia la reproducción de la música cargada.

17) pygame.mixer.music.stop(): Detiene la reproducción de la música.

-------------------------------------------------------------FUENTES--------------------------------------------------------------------------------------------------------
1) pygame.font.Font():este método se utiliza para crear un objeto Font que representa una fuente de texto. Puedes especificar la fuente y el tamaño.

2)  Font.render(text, antialias, color, background=None): Este método se llama en un objeto Font para renderizar texto en una nueva superficie. Puedes especificar el texto, si se debe aplicar antialiasing, el color del texto y, opcionalmente, el color de fondo.

3)  Font.set_bold(value): Establece si la fuente es en negrita.

4)  Font.set_italic(value): Establece si la fuente es en cursiva.

5)  Font.set_underline(value): Establece si el texto subrayado.

6)  Font.set_strikeout(value): Establece si el texto tiene una línea a través de él.

7)  Font.size(text): Devuelve el tamaño de una cadena de texto si se representara con esta fuente.

8)  Font.metrics(text): Devuelve información sobre las métricas de la fuente, como el ancho y la altura de cada carácter.

9)  Font.get_height(): Obtiene la altura de la fuente.

10)  Font.get_linesize(): Obtiene la altura de una línea de texto.

11)  Font.get_ascent(): Obtiene la altura de ascenso de la fuente.

12) Font.get_descent(): Obtiene la altura de descenso de la fuente.

13) Font.get_name(): Obtiene el nombre de la fuente.

14) Font.get_bold(): Obtiene si la fuente es en negrita.

15) Font.get_italic(): Obtiene si la fuente es en cursiva.

16) Font.get_underline(): Obtiene si el texto está subrayado.

17) Font.get_strikeout(): Obtiene si el texto tiene una línea a través de él.
--------------------------------------------------------IMAGENES-----------------------------------------------------
1) pygame.image.load(file_path): Carga una imagen desde un archivo y devuelve una superficie (Surface) que representa la imagen.

2) pygame.image.get_extended(): Comprueba si Pygame ha sido compilado con soporte para formatos de imagen adicionales.

3) pygame.image.save(surface, file_path): Guarda una superficie (Surface) como una imagen en el archivo especificado.

4) pygame.image.get_extended(): Comprueba si Pygame ha sido compilado con soporte para formatos de imagen adicionales.

5) pygame.image.load_extended(file_path): Carga una imagen desde un archivo con soporte para formatos de imagen adicionales.

6) Surface.set_colorkey(color, flags=0): Define un color transparente en una superficie. Cualquier píxel con el mismo color se considerará transparente.

7) Surface.convert(): Crea una nueva superficie con el mismo contenido pero optimizada para el tipo de pantalla actual.

8) Surface.convert_alpha(): Similar a convert(), pero también maneja la transparencia alfa.

9) Surface.subsurface(rect): Devuelve una nueva superficie que es una parte de la superficie original, definida por el rectángulo especificado.

10) pygame.transform.scale(surface, size, dest_surface=None): Escala una superficie a un nuevo tamaño.

11) pygame.transform.rotate(surface, angle): Rota una superficie por el ángulo especificado.

12) pygame.transform.flip(surface, xbool, ybool): Voltea una superficie horizontal o verticalmente según los valores booleanos dados.

"""
# ESTRUCTURA BASICA
import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
screen_width = 300 # ANCHO
screen_height = 300 # ALTO
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mi primer juego con Pygame')

# Colores
white = (255, 255, 255)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Limpiar la pantalla
    screen.fill(white)
    
    # Lógica del juego
    
    # Dibujar en la pantalla
    
    # Actualizar la pantalla
    pygame.display.update()

# Salir de Pygame
pygame.quit()
sys.exit()