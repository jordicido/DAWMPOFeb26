# Comentario de una linea

'''
asdas
asdasd
print("Hello")
'''

# Las variables son contenedores para almacenar datos.
nombre = "Jordi"
# Se llaman variables porque pueden cambiar de valor durante
# la ejecución 
nombre = "Juan"
# Aquí imprimirá Juan porqué es lo último que se 
# ha asignado a la variable
print(nombre) 

'''
 En Python existen cuatro tipos de datos básicos:
 - Números enteros (1, 10, 30)
 - Números decimales (10.5, 9.2345, 3.1415)
 - Texto ("Jordi", "Juan", "Mi abuela se llamaba Julia")
 - Booleanos (True, False)
'''

numero = 6
nota = 9.99
texto = "ERROR"
activo = False

print("Los valores de los tipos básico son:")
print(numero)
print(nota)
print(texto)
print(activo)

# Python
numero = 0
print("La variable numero es de tipo: ")
print(type(numero)) # int
numero = "Jordi"
print("La variable numero es de tipo: ")
print(type(numero)) # str
numero = True
print("La variable numero es de tipo: ")
print(type(numero)) # bool
numero = 0.0
print("La variable numero es de tipo: ")
print(type(numero)) # float

# Las variables deben seguir la convención snake_case
numero_personas = 10

# Conversión de tipos
texto = "18"
numero = int(texto) 

print("Conversión de tipos")
print(type(texto))
print(type(numero))


