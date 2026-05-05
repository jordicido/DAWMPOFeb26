# Un diccionario es un tipo de dato complejo
# que almacena pares de clave-valor

# Para inicializar un diccionario podemos:
mi_diccionario = {}
mi_diccionario2 = dict(nombre_profe="Vic", modulos=["PSP", "DIW"])

# Para crear una entrada en el diccionario podemos usar:

mi_diccionario["Jordi"] = ["EDD", "MPO"]
mi_diccionario["Jose"] = ["PROG"]
mi_diccionario["Alberto"] = ["BBDD"]
mi_diccionario["Susana"] = ["LM", "SSII"]
mi_diccionario["Ismael"] = ["IPE"]

# Para acceder a un valor del diccionario, debo hacerlo por su clave:
nombre_profe = "Jordi"
print(f"El profesor {nombre_profe} es {mi_diccionario[nombre_profe]}")

# Para eliminar un par clave/valor usaremos del o pop()
del mi_diccionario["Jose"]
print(mi_diccionario.pop("Jordi"))

# Para comprobar si una llave existe, podemos hacerlo del siguiente modo
if "Alberto" in mi_diccionario:
    print(f"La clave Alberto existe y tiene el valor {mi_diccionario["Alberto"]}")

# Recorrer un diccionario podemos hacerlo de 3 maneras:
# 1- Por claves
# 2- Por valores
# 3- Por pares de clave-valor

for nombre_profe in mi_diccionario:
    print(f"La clave {nombre_profe} tiene el valor {mi_diccionario[nombre_profe]}")

for asignaturas in mi_diccionario.values():
    print(f"Módulos impartidos: {asignaturas}")

for nombre_profe, asignaturas in mi_diccionario.items():
    print(f"El profe {nombre_profe} imparte los modulos {asignaturas}")

mi_diccionario["Jesus"] = ["Aun nada"]