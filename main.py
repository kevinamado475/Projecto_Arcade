import jocs  # Conecta con jocs.py (que ya lleva robot dentro)

while True:
    print("\n--- BENVINGUT/DA AL MINI ARCADE ---")
    print("1. Jugar a Pedra, Paper, Tisora")
    print("2. Jugar a Endevinar el Número")
    print("S. Sortir")

    opcion = input("\nElige una opción: ").strip().upper()

    if opcion == "1":
        jocs.janken()
    elif opcion == "2":
        jocs.nana()
    elif opcion == "S":
        print("¡Gracias por jugar! Saliendo del Mini Arcade...")
        break
    else:
        print("Opción incorrecta. Por favor, elige 1, 2 o S.")
