# Piedra, papel, tijera

jugador1 = input("Jugador 1: ").upper()
jugador2 = input("Jugador 2: ").upper()

if jugador1 == jugador2:
    print("EMPATE")
elif (jugador1 == "PIEDRA" and jugador2 == "TIJERA") or (jugador1 == "PAPEL" and jugador2 == "PIEDRA") or (jugador1 == "TIJERA" and jugador2 == "PAPEL"):
    print("JUGADOR 1 GANA")
else:
    print("JUGADOR 2 GANA")