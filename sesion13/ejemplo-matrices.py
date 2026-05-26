'''
filas = 3
columnas = 5
[[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]]
'''
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de filas: "))
matriz = []

for i in range(filas):
    columna = []
    for j in range(columnas):
        columna.append(i)
    matriz.append(columna)

for i in range(filas):
    print(matriz[i])
