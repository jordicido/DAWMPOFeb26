'''
         0      1         2   3          4
lista = [Jordi, Cidoncha, 37, masculino, poco pelo]

lista[1] # -> 2

persona = {
    "nombre" : "Jordi",
    "apellido" : "Cidoncha",
    "edad" : 37,
    "sexo" : "masculino"
}

persona["apellido"] # -> Cidoncha

diccionario -> buscar
     buscar -> definicion

'''
# las listas se pueden recorrer de dos formas distintas
lista = [23, 22, 133, 74, 95]

# por indice 
for i in range(len(lista)):
    print(f"Valor de i: {i}")
    print(f"Valor de la posición {i} en la lista {lista[i]}")

# por valor
for num in lista:
    print(num)

#los diccionarios se pueden recorrer de 3 formas distintas
persona = {
    "nombre" : "Jordi",
    "apellido" : "Cidoncha",
    "edad" : 37,
    "sexo" : "masculino"
}

# por llave
for llave in persona.keys():
    print(f"La llave {llave} tiene el valor {persona[llave]}")

# por valor
for valor in persona.values():
    print(valor)

# por llave y valor
for llave, valor in persona.items():
    print(f"La llave {llave} tiene el valor {valor}")
