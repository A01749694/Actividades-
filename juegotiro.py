"Juego tiro parabolico con freegames y turtle"

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)    # Crea un vector con las coordenadas (-200, -200) que representa la pelota
speed = vector(0, 0)         # Crea un vector que representa la velocidad inicial de la pelota
targets = []                 # Crea una lista vacía que contendrá los objetos objetivo (targets)

def tap(x, y):
    "Responde a los clics del usuario en la pantalla"
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = 2*(x + 200) / 25  #Multiplicar con un factor para duplicar la velocidad  
        speed.y = 2*(y + 200) / 25  

def inside(xy):
    "Comprueba si el vector xy está dentro de la ventana de juego."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Dibuja la pelota y los objetivos en la ventana de juego.
    Primero limpia la pantalla, luego dibuja los objetivos """
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """Mueve la pelota y los objetivos.
    Primero, con una probabilidad de 1/40, crea un nuevo objetivo en una posición aleatoria a la derecha de la ventana.
    Luego, mueve cada objetivo hacia la izquierda. Si un objetivo sale de la pantalla,
    lo reposiciona en la parte derecha de la pantalla."""
    
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 2.0  #Aumentar la velocidad de los objetivos a 2.0 

        # Si el objetivo está fuera de la pantalla, vuelva a colocarlo en el otro lado
        if not inside(target):
            target.x = 200

    if inside(ball):  
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
