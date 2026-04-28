lista_palabras = input("Introduce una serie de palabras separadas por coma: ").split(",")
contador = 0

for palabra in lista_palabras:
    contador += 1

print(f"El número de palabras de la lista es {contador}")