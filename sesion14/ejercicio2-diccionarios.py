'''
Las flores son rojas y las nubes blancas

declarar un diccionario vacío
primero introducimos frase
separamos las palabras de la frase por espacio (.split(" "))
recorrer lista cogiendo palabra por palabra
    si palabra no existe aun en el diccionario
        crear una entrada con valor 1
    si la palabra ya existe
        buscar el valor que tenia
        y sumarle 1
imprimimos diccionario
'''
frecuencias = {}
frase = input("Introduce la frase a analizar:\n").lower()
lista_palabras = frase.split(" ")
for palabra in lista_palabras:
    if palabra not in frecuencias:
        frecuencias[palabra] = 1
    else:
        frecuencias[palabra] += 1

print(frecuencias)