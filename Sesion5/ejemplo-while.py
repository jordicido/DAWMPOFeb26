# Programa que vaya recibiendo números y los vaya sumando hasta recibir un 
# numero negativo

numero = int(input("Introduce un número\n"))
suma = 0

while numero >= 0:
    suma = suma + numero
    numero = int(input("Introduce otro número\n"))

print(suma)