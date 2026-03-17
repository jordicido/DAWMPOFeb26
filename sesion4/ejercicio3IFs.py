pacman = int(input("Dime la casilla de Pacman\n"))
fantasma = int(input("Dime la casilla del fantasma\n"))

# 1- Si pacman = fantasma y normal -> atrapado
# 2- Si pacman = fantasma y caramelo -> comido
# 3- pacman != fantasma -> escapado
if pacman == fantasma:
    estado = input("Dime el estado de Pacman (normal/caramelo)\n")
    if estado == "normal":
        print("Pacman ha sido atrapado")
    elif estado == "caramelo":
        print("Pacman ha comido al fantasma")
else:
    print("Pacman ha escapado")