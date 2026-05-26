matriz = [
    [23, 55, 67, 89, 56],
    [11, 87, 52, 45, 77],
    [76, 51, 12, 90, 88],
    [78, 82, 37, 18, 99]
]
numero_filas = len(matriz)
numero_columans = len(matriz[0])
for fila in range(numero_filas):
    resultado = 0
    for columna in range(numero_columans):
        resultado += matriz[fila][columna]
    print(f"Fila {fila}: {resultado}")

