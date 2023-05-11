"Juego de la serpiente utilizando la biblioteca Turtle de Python"

# Importar las librerías 
from turtle import *
from random import choice
from random import randrange
from freegames import square, vector

# Creación del objeto vector para representar la posición de la comida y la serpiente
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)  # Vector que almacena la dirección de la serpiente

def move():
    """Mueve la serpiente y la comida en la pantalla.

    La función se encarga de mover la serpiente en la dirección indicada por
    aim, y de actualizar la posición de la comida en la pantalla cada 20
    movimientos. Si la serpiente se sale de los límites de la pantalla o se
    choca consigo misma, el juego termina.

    """
    move.counter += 1  # Incrementa el contador de movimientos

    # Actualiza la posición de la comida cada 20 movimientos
    if move.counter % 20 == 0:
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    
    # Crea una copia de la cabeza de la serpiente
    head = snake[-1].copy()
    
    # Mueve la cabeza en la dirección indicada por aim
    head.move(aim)
    
    # Si la cabeza sale de los límites de la pantalla o se choca con la serpiente, el juego termina
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    # Agrega la cabeza a la lista de posiciones de la serpiente
    snake.append(head)

    # Si la cabeza alcanza la posición de la comida, la serpiente crece
    if head == food:
        print('Snake:', len(snake))
        # Actualiza la posición de la comida de forma aleatoria
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        # Si la serpiente no alcanza la comida, se elimina la cola para mantener el tamaño
        snake.pop(0)
        
    # Borra el dibujo anterior y dibuja la serpiente y la comida en sus nuevas posiciones
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

move.counter = 0  # Define el atributo contador de movimientos

snake_colors = ['black','blue','green','yellow','orange']
food_colors=['purple','yellow','green','blue','black']

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, choice(snake_colors))

    square(food.x, food.y, 9, choice(food_colors))
    update()
    ontimer(move, 100)


# Configuración de la pantalla y asignación de las teclas para mover la 
serpiente
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Inicia el juego
move()  
done()
