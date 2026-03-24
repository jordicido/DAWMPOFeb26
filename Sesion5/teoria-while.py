# Bucle while
# while condición:
#   lineas de codigo que se van a ejecutar

# Programa que cuenta el número de la clase hasta que pongamos
# el nombre del profesor (Jordi)
# nada
nombre = input("Introduce nombre de alumno(o de profesor para acabar):\n")
# nombre = "Jesus"
num_alumnos = 0
# num_alumnos = 0

while nombre != "Jordi": # Jordi != Jordi ???
    num_alumnos += 1
    # num_alumnos = 2
    nombre = input("Introduce nombre de alumno(o de profesor para acabar):\n")
    # nombre = Jordi


print(f"Total de alumnos: {num_alumnos}")