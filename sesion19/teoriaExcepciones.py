def registrar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    # introducimos la edad en la BBDD
    print("Se ha registrado su edad correctamente")

try: 
    edad = int(input("Introduce tu edad: "))
    registrar_edad(edad)
except ValueError as error:
    print(f"Error: {error}")
