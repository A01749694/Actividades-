"Juego de Pac-Man utilizando la biblioteca Turtle de Python"

from random import choice
from turtle import *
from freegames import floor, vector

# state almacena la puntuación del juego
state = {'score': 0}

# Dibujar el camino que sigue Pac-Man.
path = Turtle(visible=False)

# Escribir la puntuación del jugado
writer = Turtle(visible=False)

# Controlar la dirección en la que se mueve Pac-Man.
aim = vector(5, 0)

# Posición inicial de Pac-Man.
pacman = vector(-40, -80)

# Posición y dirección de movimiento de los 4 fantasmas en el juego.
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]

# Matriz, los 0s representan paredes y los 1s representan espacio libre (para moverse).
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0,
    0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,
    0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0,
    0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    "Dibuja un cuadrado usando la ruta en (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Devuelve el desplazamiento del punto en titles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    "Retorna True si el punto es válido en titles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    "Dibuja el mundo usando la ruta."
    bgcolor('black')
    path.color('#1F3A68')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    "Mueve a pacman y todos los fantasmas."
    writer.undo()
    writer.write(state['score'])

    clear()
    # Se verifica si la posición a la que el pacman está tratando de moverse es válida
    if valid(pacman + aim):
        pacman.move(aim)  # Pacman se mueve en esa dirección

    index = offset(pacman)  # Calcula el índice de la matriz para la nueva posición de Pacman

    if tiles[index] == 1:  # Si la nueva posición de Pacman contiene un punto
        tiles[index] = 2  # Se "come" el punto, se actualiza la matriz
        state['score'] += 1  # Se suma uno al puntaje del juego
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')  # Dibuja a Pac-Man

    for point, course in ghosts:  # Para cada fantasma en la lista de fantasmas
        if valid(point + course): # Si el fantasma puede moverse en la dirección actual
            point.move(course)  # Mueve el fantasma en esa dirección
        else:
            options = [  # Genera una lista de posibles direcciones para el fantasma
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)  # Elige una dirección aleatoria para el fantasma
            course.x = plan.x  # Actualiza la dirección x del fantasma
            course.y = plan.y  # Actualiza la dirección y del fantasma

        # Nuevo código para hacer que los fantasmas persigan más al jugador
        if abs(pacman - point) < 100:  # Cambia el valor 100 para ajustar la distancia de persecución
            direction = pacman - point
            direction.x = int(direction.x / abs(direction.x)) if direction.x != 0 else 0
            direction.y = int(direction.y / abs(direction.y)) if direction.y != 0 else 0
            course.x = direction.x
            course.y = direction.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, '#00FFFF') # Color de los fantasmas '#00FFFF'

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    # Llama a la función move() cada 100 milisegundos, velocidad de los fantasmas.
    ontimer(move, 20)

def change(x, y):
    """Cambia la dirección del movimiento de Pac-Man.

    Actualiza la variable aim, que representa la dirección
    del movimiento de Pacman, según la tecla presionada por el usuario. 
    """
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# Establece el tamaño de la ventana en píxeles (420 x 420) y la posición en la pantalla (370, 0).
setup(420, 420, 370, 0)

hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')

# Escribe la puntuación en la posición actual del cursor.
writer.write(state['score'])
listen()
# Establece las teclas de las flechas para que se mueva Pac-Man 5 píxeles
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')

# Inicializa el tablero del juego.
world()
# Inicia el movimiento de los objetos en el juego.
move()
done()
