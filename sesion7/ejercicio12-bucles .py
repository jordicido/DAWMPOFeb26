# 1 2 9 -1 -4 6 1 0
numero = int(input("Introduce un número: "))
maximo = 0
minimo = 0

while numero != 0:
    if numero > maximo:
        maximo = numero
    elif numero < minimo:
        minimo = numero
    numero = int(input("Introduce un número: "))

print(f"El mayor es {maximo}")
print(f"El menor es {minimo}")
