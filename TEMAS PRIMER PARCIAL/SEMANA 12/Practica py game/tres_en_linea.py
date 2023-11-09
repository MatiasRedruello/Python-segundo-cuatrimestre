import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana - Podrian ser constantes
screen_width = 300 #Ancho
screen_height = 300# Alto
screen = pygame.display.set_mode((screen_width, screen_height))# Crea una superficie
pygame.display.set_caption('Tic-Tac-Toe')# Cambio el nombre del juego

# Colores
white = (255, 255, 255) # Color del fondo
line_color = (0, 0, 0) # Color de las lineas
winner_color = (0, 200, 200) 

# Tamaño de la cuadrícula
grid_size = 3 # tamaño de la cuadricula. Se utiliza para realizar distintos calculos
cell_size = screen_width // grid_size #tamaño de la celda. realiza una divicion entera entre ancho ventana y tamaño de cuadricula

# Inicializar el tablero de juego
# board es una matriz
board = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]#list comprenhension- itera 3x1, tres veces, tablero de 3x3
player_turn = 'X' #¿quien arranca?

# Función para dibujar la cuadrícula
def draw_grid():
    for x in range(1, grid_size):
                        # pantalla - color linea- ubicacion 1er linea - ubicacion 2da linea - grosor
        pygame.draw.line(screen, line_color, (x * cell_size, 0), (x * cell_size, screen_height), 2) # lineas orizontales
                                            # 100;0 y 100;300     200;0 y 200;300
        pygame.draw.line(screen, line_color, (0, x * cell_size), (screen_width, x * cell_size), 2) # lineas verticales
                                            # 0;100 y 0;300        0;200 y 300;200 

# Función para dibujar las X y O
def draw_symbols():
    for row in range(grid_size):# fila 
        for col in range(grid_size): # columna
            #board als er matriz soporta que le pase indices (row y col)
            if board[row][col] == 'X':
                x = col * cell_size + cell_size // 2 
                y = row * cell_size + cell_size // 2
                # Calcula lo pares de coordenadas para dibjar las cruces 
                pygame.draw.line(screen, line_color, (x - 30, y - 30), (x + 30, y + 30), 3)
                pygame.draw.line(screen, line_color, (x + 30, y - 30), (x - 30, y + 30), 3)
            elif board[row][col] == 'O':
                x = col * cell_size + cell_size // 2
                y = row * cell_size + cell_size // 2
                # Calcula lo pares de coordenadas para dibjar las cruces
                pygame.draw.circle(screen, line_color, (x, y), 30, 3)

# Función para comprobar el ganador
def check_winner():
    # Comprobar filas, columnas y diagonales
    for i in range(grid_size):
        # verifica ta-te-ti en fila  o en columba. evalua que en los tres casilleros sean iguales y distinto a vacio
        # y retorna un el contenido de una de los tres cuadrados
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
        # verifica tateti por ambas diagonales y retorna el valor de un casillero
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

# Bucle principal del juego
running = True
while running:
    # recorre fila de eventos y los guarda en event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not check_winner():
            # desempaqueta la posicion en x e y
            x, y = event.pos
            # col y row son iguales al valor correspondiente dividio el tamaño de la celda
            col = x // cell_size
            row = y // cell_size
            # si la celda esta vacia, la celda toma el valor del jugador actual
            if board[row][col] == ' ':
                board[row][col] = player_turn
                if player_turn == 'X':
                    player_turn = 'O'
                else:
                    player_turn = 'X'

    # Limpiar la pantalla
    screen.fill(white)
    
    # Dibujar la cuadrícula
    draw_grid()
    
    # Dibujar los símbolos X y O
    draw_symbols()
    
    # Comprobar el ganador
    winner = check_winner()
    if winner:
        font = pygame.font.Font(None, 36)
        text = font.render(f'¡{winner} gana!', True, winner_color)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, 10))
    
    # Actualizar la pantalla
    pygame.display.update()

# Salir de Pygame
pygame.quit()
sys.exit()
