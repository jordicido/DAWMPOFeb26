numeros = input("Introduce una serie de numeros separados por coma: ").split(",")
#lista_numeros = [int(num) for num in numeros]
lista_numeros = []
for num in numeros:
    lista_numeros.append(int(num))
lista_numeros.sort()
print(f"El mayor es {lista_numeros[-1]} y el menor es {lista_numeros[0]}")