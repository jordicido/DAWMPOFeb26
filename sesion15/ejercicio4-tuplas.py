numeros = input("Introduce una serie de numeros separados por coma: ").split(",")

numeros_enteros = []

for i in range(len(numeros)):
    numeros_enteros.append(int(numeros[i]))

tupla_nums = tuple(numeros_enteros)

suma = 0
maximo = tupla_nums[0]
minimo = tupla_nums[0]

for numero in tupla_nums:
    suma += numero
    if numero > maximo:
        maximo = numero
    elif numero < minimo:
        minimo = numero

print(f"Suma: {suma}")
print(f"Promedio: {suma/len(tupla_nums)}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")