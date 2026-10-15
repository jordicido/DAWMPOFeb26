# Manejo de archivos

try: 
    with open("sesion20/datos-compras.txt", "r+") as datos:
        asistentes = datos.readlines()
        if "Fabian\n" not in asistentes:
            datos.write("Fabian\n")  
except FileNotFoundError as error:
    print(f"Error: {error}")
  
print("Fin del programa")
