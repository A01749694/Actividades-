from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
state = {'mark': None, 'taps': 0}

def square(x, y):
    "Draw white square with black outline at (x, y)."
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
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
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
    write(f'Taps: {state["taps"]}', align='center', font=('Arial', 20, 'normal'))  #Crear el contador

def check_game_over():
    "Funcion que detecta cuando se destapan todos los cuadros y acaba el juego"
    if all(not hide[count] for count in range(64)): 
        up()
        goto(0, 0)
        color('blue') #Color de las letras 
        write("Fin del juego", align='center', font=('Arial', 30, 'normal'))  #Mensaje de fin



def draw():
    "Draw image and tiles."
    tracer(False)  # Desactivar actualizaciones automáticas de la pantalla

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
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    display_taps()  #LLamar a la funcion de desplegar tablero
    check_game_over()  #LLamar a la funcion que detecta los cuadros

    tracer(True)  # Actualizar la pantalla manualmente
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
