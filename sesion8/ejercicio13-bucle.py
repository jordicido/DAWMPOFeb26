numero = int(input("Introduce el siguiente número: "))

while numero != -1:
    longitud = 0
    while numero > 0:
        numero //= 10
        longitud += 1
    print(f"La longitud del número es {longitud}")
    numero = int(input("Introduce el siguiente número: "))