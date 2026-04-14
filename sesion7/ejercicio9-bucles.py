numero = int(input("Ingrese un número (0 para acabar)"))
suma = 0

while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número (0 para acabar)"))

print(f"La suma total es {suma}")