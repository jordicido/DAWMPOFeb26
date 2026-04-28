numeros1 = input("Introduce una serie de numeros separados por coma: ").split(",")
numeros2 = input("Introduce una serie de numeros separados por coma: ").split(",")
# [1,2,3,4,5,6]
# [7,8,9,0,1,2]
resultado = []

if len(numeros1) != len(numeros2):
    print("La longitud de las listas no puede ser diferente")
else:
    for i in range(len(numeros1)):
        resultado.append(int(numeros1[i]) + int(numeros2)[i])

    print(f"La lista resultado es: {resultado}")