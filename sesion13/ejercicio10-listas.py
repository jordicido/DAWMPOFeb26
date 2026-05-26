matriz = [
    [23, 55, 67, 89, 56],
    [11, 87, 52, 45, 77],
    [76, 51, 12, 90, 88],
    [78, 82, 37, 18, 99]
]
valor = int(input("Introduce el valor que quieres buscar: "))
encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if valor == matriz[i][j]:
            encontrado = True
            print(f"El valor {valor} encontrado en la fila {i} y columna {j}")

if encontrado == False:
    print(f"El valor {valor} no se encuentra en la matriz")
