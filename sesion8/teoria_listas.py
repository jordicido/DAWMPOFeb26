# Las listas son colecciones ordenadas y mutables de elementos.

mi_lista = [2, 1, 56, 7, 4]

# Print de la lista entera
print(mi_lista)
# Print del elemento 7 de la lista
print(mi_lista[3])
# Puedes contar índices desde el último
print(mi_lista[-1])
# Print del penúltimo de la lista
print(mi_lista[-2])

# Dos maneras de crear una lista vacía
nueva_lista = []
nueva_lista2 = list()

# Para modificar el valor de un elemento de la lista, accedo por índice
mi_lista[2] = 6

print(mi_lista)

# append(): Agrega un elemento al final de la lista.
mi_lista.append(56)
print(mi_lista)

# insert(): Inserta un elemento en una posición específica de la lista.
mi_lista.insert(3, 23)
print(mi_lista)

# remove(): Elimina el primer elemento con el valor especificado.
mi_lista.remove(23)
print(mi_lista)

# pop(): Elimina y devuelve el último elemento de la lista (o el elemento en la posición especificada).
print(mi_lista.pop())

# sort(): Ordena los elementos de la lista en orden ascendente.
mi_lista_ordenada = mi_lista.copy()
mi_lista_ordenada.sort()
print(mi_lista_ordenada)
print(mi_lista)

# reverse(): Invierte el orden de los elementos en la lista.
mi_lista.reverse()
print(mi_lista)

# len(): Devuelve la longitud de la lista (número de elementos).
print(len(mi_lista))