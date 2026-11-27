import jocs  # Conecta con jocs.py (que ya lleva robot dentro)

# Bucle infinito que mantiene el menú funcionando después de cada partida
while True:
    print("\n--- BIENVENIDO/DA AL MINI ARCADE LOCA🧠 ---")
    print("1. Jugar a Piedra, Papel, Tijera")
    print("2. Jugar a adivinar el Número")
    print("S. Salir")

    opcion = input("\nElige una opción: ").strip().upper()

    if opcion == "1":
        jocs.janken() # Entra en jocs.py y ejecuta la función janken()
    elif opcion == "2":
        jocs.nana() # Entra en jocs.py y ejecuta la función nana()
    elif opcion == "S":
        print("¡Gracias por jugar! Saliendo del Mini Arcade...")
        break
    else:
        print("Opción incorrecta. Por favor, elige 1, 2 o S.")
