def contar_lineas_y_palabras(contenido):
    num_lineas = len(contenido)
    num_palabras = 0
    for linea in contenido:
        linea = linea.rstrip("\n")
        if not len(linea) == 0:
            num_palabras += len(linea.split(" "))
    return num_lineas, num_palabras

def main():
    try:
        with open("sesion21/ejemplo.txt", "r") as archivo:
            contenido = archivo.readlines()
            num_lineas, num_palabras = contar_lineas_y_palabras(contenido)
            print(f"El archivo contiene {num_lineas} lineas y {num_palabras} palabras")
    except FileNotFoundError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()