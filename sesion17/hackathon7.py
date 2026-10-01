# Multiplos de 3

limite = int(input("Introduce un límite: "))
cantidad = 0
suma = 0

for i in range(1,limite+1):
    if i % 3 == 0:
        cantidad += 1
        suma += i
        print(i, end=" ")
print()
print(f"Cantidad: {cantidad}")
print(f"Suma: {suma}")