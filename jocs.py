import random  # nota  # noqa: I001

import robot   # Aquí es donde se conecta robot.py


def janken():
    print("\n--- PIEDRA, PAPEL, TIJERA ---")
    print("1. El primero que llegue a 3 victorias")
    print("2. Al mejor de 5 rondas")
    
    modo = input("Elige el modo de juego (1 o 2): ")
    while modo not in ["1", "2"]:
        modo = input("Opción incorrecta. Escribe 1 o 2: ")

    oponente = robot.robot()
    puntos_usuario = 0
    puntos_robot = 0
    rondas_jugadas = 0

    while True:
        if modo == "1" and (puntos_usuario == 3 or puntos_robot == 3):
            break
        if modo == "2" and rondas_jugadas == 5:
            break

        jugada_usuario = input("\nElige (pedra, paper, tisora): ").lower()
        
        if jugada_usuario not in ["pedra", "paper", "tisora"]:
            print("Palabra incorrecta. Escribe exactamente: pedra, paper o tisora.")
            continue

        jugada_robot = oponente.playing()
        print(f"El robot ha sacado: {jugada_robot}")

        rondas_jugadas += 1

        if jugada_usuario == jugada_robot:
            print("¡Empate en esta ronda!")
        elif (jugada_usuario == "pedra" and jugada_robot == "tisora") or \
             (jugada_usuario == "paper" and jugada_robot == "pedra") or \
             (jugada_usuario == "tisora" and jugada_robot == "paper"):
            print("¡Ganas esta ronda!")
            puntos_usuario += 1
        else:
            print("El robot gana esta ronda.")
            puntos_robot += 1

        print(f"Marcador -> Tú: {puntos_usuario} | Robot: {puntos_robot} (Rondas: {rondas_jugadas})")

    print("\n--- FIN DE LA PARTIDA ---")
    if puntos_usuario > puntos_robot:
        print("¡Has ganado la partida!")
    elif puntos_robot > puntos_usuario:
        print("El robot gana la partida...")
    else:
        print("¡La partida ha terminado en empate!")


def nana():
    print("\n--- ENDEVINAR EL NÚMERO (1 al 100) ---")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            numero = int(input("Introduce un número del 1 al 100: "))
        except ValueError:
            print("Error: tienes que escribir un número entero.")
            continue

        if numero < 1 or numero > 100:
            print("El número debe estar entre 1 y 100.")
            continue

        intentos += 1

        if numero > numero_secreto:
            print("Massa alt (Demasiado alto).")
        elif numero < numero_secreto:
            print("Massa baix (Demasiado bajo).")
        else:
            print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
            break
