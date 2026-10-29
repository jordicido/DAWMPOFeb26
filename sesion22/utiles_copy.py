
def leer_entero():
    print("Estoy usando la funcion del utiles copy")


def leer_entero_limites(inferior, superior):
    entero = int(input(f"Introduce un número entero entre {inferior} y {superior}: "))
    while entero < inferior or entero > superior:
        print(f"Debes introducir un número entero entre {inferior} y {superior}")
        entero = int(input("Introduce un número entero: "))

def leer_texto():
    texto = input("Introduce una linea de texto: ")
    return texto

