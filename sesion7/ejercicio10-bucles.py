import random

secreto = random.randint(1,100)
numero = int(input("Adivina el número [1-100]: "))

while numero != secreto:
    if numero < 1 or numero > 100:
        print("El número debe ser entre 1 y 100")
    elif numero > secreto:
        print("El número secreto es menor")
    else:
        print("El número secreto es mayor")
    
    numero = int(input("Adivina el número [1-100]: "))

print(f"Correcto! El numero secreto era {secreto}")