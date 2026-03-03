"""
Entrada y salida de datos

* entrada --> input() nos introduce datos en nuestro programa en
formato ¡texto!
* salida --> print() nos imprime texto en la terminal
"""

modulo = input("¿Cuál es tu módulo preferido?\n")

print(f"El módulo que más me gusta es {modulo}")

# Operaciones aritméticas

a = 10
b = 3

print(f"Suma: {a+b}")                 # 13
print(f"Resta: {a-b}")                # 7
print(f"Multiplicación: {a*b}")       # 30
print(f"División decimal: {a/b}")     # 3.33
print(f"División entera: {a//b}")     # 3
print(f"Módulo(resto): {a%b}")        # 1
print(f"Potencia: {a**b}")            # 1000  

# Operaciones de comparación

edad = int(input("Qué edad tienes?\n")) # Un solo igual asigna un valor a una variable

print(f"Es igual a 18? {edad == 18}") # Dos iguales comparan valores
print(f"Es diferente a 18? {edad != 18}")
print(f"Es mayor que 18? {edad > 18}")
print(f"Es menor que 18? {edad < 18}")
print(f"Es mayor o igual a 18? {edad >= 18}")
print(f"Es menor o igual a 18? {edad <= 18}")

# Operadores lógicos

años_trabajados = 40

print(f"Estás en edad de trabar? {edad >= 18 and edad < 67}")
print(f"Te puedes prejubilar? {edad >= 60 or años_trabajados > 35}")
print(f"Puedes trabajar? {not edad < 18}")


# Asignación compuesta

numero = 1
numero += 2     # 3
numero -= 2     # 1
numero *= 5     # 5