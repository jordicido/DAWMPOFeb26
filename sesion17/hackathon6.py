# Adivina el numero 
import random

secreto = random.randint(1, 100)
intento = int(input("Adivina el número entre 1 y 100"))
intentos = 1

while(intento != secreto):
    if (intento > secreto):
        print("Demasiado alto!")
    else:
        print("Demasiado bajo!")
    intento = int(input("Adivina el número entre 1 y 100"))
    intentos += 1

print(f"Has acertado, el número secreto es: {secreto}")
print(f"Intentos: {intentos}")
