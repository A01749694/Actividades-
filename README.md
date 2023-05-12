# Actividades-
# Juegos en Python con Turtle y freegames

>Equipo: 
>Sebastian Antonio Almanza A01749694.  
>Michelle Rergis Novelo A01798576  

Este repositorio contiene 5 juegos a los cuales de manera colaborativa se mejoraron/arreglaron, agregando nuevas funciones que realizarán nuevas acciones dentro de ellos o para mejorar las ya existentes, esto con el fin de poner en práctica conocimientos de programación en Python así como el uso de la plataforma Github para aplicar el control de manejo de versiones al trabajo colaborativo. 
Para este repositorio es necesario contar con la instalación de python 3 y de las librerías de freegames.
Los juegos fueron los siguientes: 

**Juego de dibujo:** Este juego permite al usuario en un lienzo dibujar diferentes formas como lo son una línea, un cuadrado, un rectángulo, un triángulo y un círculo dado dos puntos principales, en este se completó las funciones de las últimas tres figuras para que estas pudieran ser dibujadas correctamente por el usuario.

**Juego de la vibora:** Este juego hace que el usuario controle a una vibora y que recolecte comida en el escenario, en este juego se mejoró que la comida se mueva en el escenario mientras el juego esta activo sumado a que tanto la comida como la vibora cambien de color entre 5 colores distintos al azar.

**Juego de Pac-man:** Este juego es el clásico juego donde el jugador debe recolectar todos los puntos evitando ser atrapado por los fantasmas, en este se modificó la forma del tablero, la velocidad de los fantasmas y que estos fuesen más "inteligentes".

**Juego de tiro parabólico:** Este juego consiste en disparar a objetivos que se mueven en el ambiente con un proyectil parabólico, en este programa se modificó la velocidad a la que los objetivos se mueven y la velocidad del proyectil, además de hacer el juego infinito al hacer que los objetivos reboten al tocar las paredes.

**Juego de memoria:** En este juego el usuario debe destapar una imagen debajo de unos recuadros con números en ellos que al formar pares de números son destapados, en este código se realizó una serie de cosas, se agregó un contador de clicks, una función que detectara cuando todo el memorama ha sido descubierto, los números aparecen centrados en sus respectivos cuadros y por último el cambiar los números por otro elemento que estimule la memoria del usuario, en este caso se cambiaron por palabras.

## Guía para instalar los paquetes y herramientas necesarias:

>Para utilizar la terminal:
>Aunque para descargar y utilizar estos juegos no es del todo necesaria la terminal, si le interesa trabajar con repositorios en Github será de utilidad.

-Para los usuarios de **MacOS**, **Linux** u otros sistemas de **tipo UNIX**, deben identificar cómo abrir una terminal, en Mac usualmente viene en las aplicaciones con el nombre de terminal.
-Para usuarios de **Windows** podrán utilizar PowershellLinks to an external site.. También es recomendable instalar uno de los siguientes emuladores de terminal UNIX
WSL https://docs.microsoft.com/en-us/windows/wsl/install-win10 (Links to an external site.)
Cmdr https://cmder.app/Links to an external site.
Git Bash https://git-scm.com/downloads

En la siguiente imagen se puede observar la lista de comandos desde la terminal.
![Comandos terminal](https://github.com/A01749694/Actividades-/assets/122414903/742bd751-ed60-4c6c-8739-52a98a957d48)


## Para instalar Python 3

1. Descarga el instalador de Python 3 desde el sitio web oficial de Python: https://www.python.org/downloads/

2. Selecciona la versión de Python 3 que deseas descargar. Se recomienda la versión más reciente disponible, a menos que necesites una versión específica para algún propósito.

4. Descarga el instalador para el sistema operativo que estés utilizando (Windows, macOS, Linux, etc.)

5. Una vez que se haya descargado el instalador, haz doble clic en el archivo para iniciar la instalación.

6. Sigue las instrucciones del instalador. Asegúrate de leer cuidadosamente cada paso antes de continuar. Es posible que se te solicite que selecciones la ubicación de instalación y otras opciones personalizadas.

7. Después de completar la instalación, abre una terminal o línea de comandos y verifica que Python 3 se haya instalado correctamente. En la línea de comandos, ingresa "python --version" (sin las comillas) y presiona enter. Deberías ver la versión de Python 3 que acabas de instalar.

8. Ya puedes comenzar a escribir y ejecutar programas en Python 3.

## Módulo Pip en Python
>El módulo Pip es una herramienta de administración de paquetes en Python que permite instalar, actualizar y desinstalar paquetes de software de terceros que no están incluidos en la biblioteca estándar de Python.

1. Instala el modulo pip de Python, que ayuda a descargar otros módulos
2. Puedes revisar si ya lo tienes instalado desde la terminal usando python -m pip --version 
3. En caso de no estar instalado, sigue los pasos en https://pip.pypa.io/en/stable/installation/
4. Una vez instalado pip, instala las librerías de Python que se utilizarán según el reto:
freegames para videojuegos:
-pip install freegames

