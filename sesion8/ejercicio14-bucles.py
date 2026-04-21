numero = int(input("Introduce un número: "))

for i in range(2, numero):
    if numero % i == 0:
        print("No es un número primo")
    else:
        print("Es un número primo")
