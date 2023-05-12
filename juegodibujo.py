from turtle import *
from freegames import vector

def line(start, end):
    "Funcion que dibuja una linea recta"
    up()
    goto(start.x, start.y)  #Punto de inicio
    down()
    goto(end.x, end.y)  #Punto final 

def square(start, end):
    "Funcion que dibuja un cuadrado en base a dos puntos"
    up()
    goto(start.x, start.y)  #Puntos iniciales
    down()
    begin_fill()  #Rellenar figura

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circulo(start, end):
    "Funcion que dibuja un circulo dado dos puntos"
    up()
    radius = abs(start - end)
    goto(start.x, start.y - radius)  #Calculo de radio en base a ambos puntos
    down()
    circle(radius)

def rectangle(start, end):
    "Funcion que dibuja un recangulo dado dos puntos"
    up()
    goto(start.x, start.y)  #Puntos iniciales 
    down()
    begin_fill()  #Rellenar figura 
    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
    end_fill()

def triangle(start, end):
    "Funcion que dibuja un triangulo dado dos puntos "
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(3):
        forward(end.x - start.x)
        left(120)
    end_fill()

def tap(x, y):
    "Funcion que almacena los puntos elegidos"
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Funcion que almacena la tecla que define la figura a dibujar"
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'A')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
