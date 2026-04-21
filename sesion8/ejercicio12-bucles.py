numero = int(input("Introduce una serie de números: "))
maximo = numero
minimo = numero

while numero != 0:
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero
    numero = int(input("Introduce el siguiente número: "))

print(f"El número mayor es {maximo}")
print(f"El número menor es {minimo}")