def dibujar_rectangulo(filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            print("*", end="")
        print()

def dibujar_triangulo(altura, invertido=False):
    if invertido:
        inicio = altura
        fin = 0
        step = -1
    else:
        inicio = 1
        fin = altura+1
        step = 1
    for i in range(inicio, fin, step):
        for j in range(i):
            print("*", end="")
        print()
'''
   *
  ***
 *****
*******
'''
def dibujar_piramide(altura):
    espacios = altura - 1
    simbolos = 1
    for i in range(1,altura+1):
        print(" "*espacios+"*"*simbolos)
        espacios -= 1
        simbolos += 2

while True:
    print("""
----- GENERADOR DE PATRONES -----

1. Rectángulo
2. Triángulo normal
3. Triángulo invertido
4. Pirámide centrada
5. Salir
""")
    opcion = int(input("Escoge una opción: "))
    if opcion == 1:
        filas = int(input("Introduce el número de filas: "))
        columnas = int(input("Introduce el número de columnas: "))
        dibujar_rectangulo(filas, columnas)
    elif opcion == 2:
        altura = int(input("Introduce la altura del triangulo: "))
        dibujar_triangulo(altura)
    elif opcion == 3:
        altura = int(input("Introduce la altura del triangulo: "))
        dibujar_triangulo(altura, True)
    elif opcion == 4:
        altura = int(input("Introduce la altura del triangulo: "))
        dibujar_piramide(altura)
    elif opcion == 5:
        print("Gracias por usar el generador de patrones")
        break
    else:
        print("Opción no válida.")