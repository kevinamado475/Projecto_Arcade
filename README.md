# Practica 02: intrducion a la programacion de python"
-**alumne:** [kevin andres amado linares]
-**curs:** [smx2-b]
-**modul:** [proyecte intermodular]

# Máquina Arcade (Mini Arcade en Python)

## Descripción del proyecto
Este proyecto consiste en una aplicación de consola desarrollada en Python que simula una máquina recreativa con dos minijuegos clásicos: **Piedra, Papel o Tijera** (jugando contra un robot con elecciones aleatorias en dos modalidades de partida) y **Adivinar el Número** (con sistema de pistas y contador de intentos).


## Estructura del código
El proyecto sigue una arquitectura modular dividida en tres archivos principales dentro de la misma carpeta:

* **`main.py`**: Es el punto de entrada de la aplicación. Contiene el bucle principal (`while True`) que muestra el menú en pantalla, lee la opción del usuario, gestiona los errores de entrada y llama a las funciones correspondientes del módulo `jocs.py`.
* **`jocs.py`**: Contiene toda la lógica de los minijuegos separada en dos funciones (`janken()` para Piedra, Papel o Tijera y `nana()` para Adivinar el Número). Este archivo no se ejecuta directamente, sino que se importa desde `main.py`.
* **`robot.py`**: Módulo proporcionado que implementa la clase `robot` y su método `playing()`, encargado de generar de forma aleatoria las jugadas de la máquina para el juego de Piedra, Papel o Tijera.
