# se importa un modulo que genera un numero cualquiera 
import random  # nota  # noqa: I001

# se importa el robot para jugar 
import robot   # Aquí es donde se conecta robot.py

# def (funcion) y janken es el nombre que le ponemos 
def janken():
    print("\n--- PIEDRA, PAPEL, TIJERA ---")
    print("1. El primero que llegue a 3 victorias")
    print("2. Al mejor de 5 rondas")
# pedimos que el usuario escoje un numero 1 0 2
    modo = input("Elige el modo de juego (1 o 2): ")
    # si el usario escribe mal 1 0 2 saldra error y que escriba bien el numero
    while modo not in ["1", "2"]:
        modo = input("Opción incorrecta. Escribe 1 o 2: ")
# Creamos una copia funcional del robot a partir de la clase de robot.py
    oponente = robot.robot()
    puntos_usuario = 0
    puntos_robot = 0
    rondas_jugadas = 0
# Bucle principal del juego: se repite ronda tras ronda hasta que alguien gane
    while True:
    # Condición de parada 1: si eligió modo "1" y alguien llega a 3 puntos, salimos del bucle
        if modo == "1" and (puntos_usuario == 3 or puntos_robot == 3):
            break
        # Condición de parada 2: si eligió modo "2" y ya van 5 rondas, salimos del bucle
        if modo == "2" and rondas_jugadas == 5:
            break
# Pedimos la jugada al usuario y .lower() la convierte a minúsculas por si escribe "PEDRA"
        jugada_usuario = input("\nElige (piedra, papel, tijera): ").lower()
      # Filtro de seguridad: si escribió otra palabra, avisamos y saltamos al inicio del bucle (continue) 
        if jugada_usuario not in ["piedra", "papel", "tijera"]:
            print("Palabra incorrecta. Escribe exactamente: piedra, papel o tijera.")
            continue
# El robot ejecuta su función playing() y guardamos su respuesta
        jugada_robot = oponente.playing()
        print(f"El robot ha sacado: {jugada_robot}")
        # Sumamos 1 al contador de rondas válidas jugadas
        rondas_jugadas += 1
        #Comparamos tu jugada contra la del robot
        if jugada_usuario == jugada_robot:
            print("¡Empate en esta ronda!") # es un empate 
        # Comprobamos las 3 combinaciones en las que gana el jugador
        elif (jugada_usuario == "piedra" and jugada_robot == "tijera") or \
             (jugada_usuario == "papel" and jugada_robot == "piedra") or \
             (jugada_usuario == "tijera" and jugada_robot == "papel"):
            print("¡Ganas esta ronda!")
            puntos_usuario += 1
        # Si no fue empate ni ganaste tú, significa que ganó el robot
        else:
            print("El robot gana esta ronda.")
            puntos_robot += 1
        # Mostramos el resumen actual usando una f-string para meter variables dentro del texto
        print(f"Marcador -> Tú: {puntos_usuario} | Robot: {puntos_robot} (Rondas: {rondas_jugadas})")
    # Una vez roto el bucle (break), anunciamos el resultado final de la partida
    print("\n--- FIN DE LA PARTIDA ---")
    if puntos_usuario > puntos_robot:
        print("¡Has ganado la partida!")
    elif puntos_robot > puntos_usuario:
        print("El robot gana la partida...")
    else:
        print("¡La partida ha terminado en empate!")

# Definimos la función del segundo juego en este caso nana
def nana():
    print("\n--- ENDEVINAR EL NÚMERO (1 al 100) ---")
    numero_secreto = random.randint(1, 100) # Python inventa un número entero del 1 al 100
    intentos = 0 # Contador de intentos empezando en cero
    # Bucle que pide números sin parar hasta que el usuario acierte
    while True:
        try: # try/except evita que el programa explote si el usuario escribe letras en vez de números
            numero = int(input("Introduce un número del 1 al 100: ")) #Convierte el texto a entero
        except ValueError:
            print("Error: tienes que escribir un número entero.")
            continue # Vuelve arriba del bucle a pedir el número otra vez
        # Comprobamos que el número no se salga del rango permitido (1 a 100)
        if numero < 1 or numero > 100: 
            print("El número debe estar entre 1 y 100.")
            continue # Vuelve arriba sin gastar un intento

        intentos += 1 # Si el número es válido, sumamos 1 al contador de intentos
# Comparamos el número del usuario con el secreto para dar pistas
        if numero > numero_secreto:
            print("Massa alt (Demasiado alto).")
        elif numero < numero_secreto:
            print("Massa baix (Demasiado bajo).")
        # Si no es mayor ni menor, es que ha acertado
        else:
            print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
            break
