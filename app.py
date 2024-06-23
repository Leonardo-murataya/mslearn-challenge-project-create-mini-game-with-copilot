# Crear una juego de piedra papel o tijera
# 1. el usuario elige una opcion
# 2. la computadora elige una opcion
# 3. se imprime el resultado
# 4. se pregunta si se quiere jugar de nuevo
# 5. si se quiere jugar de nuevo se repite el proceso
# 6. si no se quiere jugar de nuevo se termina el juego

import random

def game():
    print("Juguemos piedra, papel o tijera")
    user = input("Tu eleccion: ").lower()
    computer = random.choice(["piedra", "papel", "tijera"])
    print(f"La computadora eligio: {computer}")

    if user == computer:
        return "Es un empate"
    if is_win(user, computer):
        return "Ganaste!"
    return "Perdiste!"

def is_win(player, opponent):
    # return true si el jugador gana
    # piedra > tijera, tijera > papel, papel > piedra
    if (player == "piedra" and opponent == "tijera") or (player == "tijera" and opponent == "papel") or (player == "papel" and opponent == "piedra"):
        return True
    
while True:
    print(game())
    if input("Quieres jugar de nuevo? (si/no): ").lower() != "si":
        break
