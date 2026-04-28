numero = int(input("Introduce un número: "))

for i in range(2, numero):
    if numero % i == 0:
        print("El numero no es primo")
        break
    if i == numero-1:
        print("El numero es primo")
    

