matriz = [
    [23, 45, 67, 89, 56],
    [11, 87, 23, 45, 56],
    [76, 51, 12, 90, 56],
    [78, 82, 37, 18, 56]
]
resultado = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        resultado += matriz[i][j]

print(f"El resultado de la suma de los elementos de la matriz es {resultado}")