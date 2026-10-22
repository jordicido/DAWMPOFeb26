
try:
    with open("sesion21/ejemplo.txt", "r") as archivo:
        print(f"EL archivo tiene {len(archivo.readlines())} lineas")
except FileNotFoundError as error:
    print(f"Error: {error}")