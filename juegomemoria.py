'Juego de Memoria'

from random import *
from turtle import *
from freegames import path

# Carga la imagen del auto
car = path('car.gif')

# Palabras para las tarjetas
palabras = [
    'Gato', 'Perro', 'Oso', 'Lobo', 'Zorro', 'Ratón', 'Topo', 'Oveja', 'Cabra',
    'Vaca', 'Cerdo', 'Burro', 'Mono', 'Rana', 'Pez', 'Abeja', 'Cuervo', 'Grillo',
    'Araña', 'Pulpo', 'Cangrejo', 'Nutria', 'Alce', 'Salamandra', 'Camaleón',
    'Iguana', 'Caracol', 'Gamba', 'Ciervo', 'Puma', 'Castor', 'Colibrí', 'Jirafa'
    ]
# Las palabras se duplican para tener parejas de imágenes para cada palabra
tiles = palabras * 2

state = {'mark': None}

# Imagen oculta
hide = [True] * 64

state = {'mark': None, 'taps': 0}

def square(x, y):
    "Dibuja un cuadrado blanco con contorno negro en (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convierte las coordenadas (x, y) en índice de los recuadros"
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Actualiza la marca y los recuadros ocultos según el tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        if hide[spot]:
            x, y = xy(spot)
            up()
            goto(x + 25, y + 7.5)
            color('black')
            # Ajustar la fuente para que el número quepa dentro del cuadrado y esté centrado.
            write(tiles[spot], align='center', font=('Arial', 15, 'normal'))
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    state['taps'] += 1

    display_taps()
    

def display_taps():
    "Despliega el contador de click arriba del tablero de juego"
    penup()
    goto(0, (500 // 2) - 20)  # Ajusta el valor de la altura
    color('black')
    write(f'Taps: {state["taps"]}', align='center', font=('Arial', 15, 'normal'))  #Crear el contador

def check_game_over():
    "Funcion que detecta cuando se destapan todos los cuadros y acaba el juego"
    if all(not hide[count] for count in range(64)): 
        up()
        goto(0, 0)
        color('blue') #Color de las letras 
        write("Fin del juego", align='center', font=('Arial', 30, 'normal'))  #Mensaje de fin



def draw():
    "Dibuja la imagen y los cuadrados del juego"
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 7.5)
        color('black')
        write(tiles[mark], align='center', font=('Arial', 15, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(600, 600, 370, 0)  #Aumentar el tamaño del lienzo
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
display_taps()
done()