numero = int(input("Introduce un número\n"))
factorial = 1

for i in range(numero, 0, -1):
    factorial *= i

print(f"El resultado de {numero}! es {factorial}")
