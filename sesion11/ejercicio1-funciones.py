import math

def area_circulo(radio):
    print(f"El area de un círculo de radio {radio} es {math.pi*(radio**2):.2f}")

radio = float(input("Introduce el radio de un círculo: "))
area_circulo(radio)