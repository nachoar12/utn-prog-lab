from random import randint, randrange

# tamaño pantalla principal
WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)
CENTER_SCREEN = (WIDTH // 2, HEIGHT // 2)

# cuadros por segundo para el muestreo de pantalla
FPS = 60
SPEED = 5


# colours

# Valores RGB de colores primarios
red = (255, 0, 0)     # RGB values for red
green = (0, 255, 0)   # RGB values for green
blue = (0, 0, 255)    # RGB values for blue

# Valores RGB de colores secundarios
cyan = (0, 255, 255)      # RGB values for cyan
magenta = (255, 0, 255)   # RGB values for magenta
yellow = (255, 255, 0)    # RGB values for yellow

# Valores RGB de blanco y negro
white = (255, 255, 255)   # RGB values for white
black = (0, 0, 0)         # RGB values for black

# block = {
#     "pos_y":,
#     "pos_x":,
#     "ancho":,
#     "alto":,
#     "color":,
#     "direccion":
# }

colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'gray': (128, 128, 128),
}