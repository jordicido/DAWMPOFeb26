nombre1 = input("Indica un nombre: ")
nombre2 = input("Indica otro nombre: ")
nombre3 = input("Indica otro nombre: ")

print(f"Alguien es Juan? {nombre1 == "Juan" or nombre2 == "Juan" or nombre3 == "Juan"}")
print(f"Alguien es Juan? {"Juan" in [nombre1, nombre2, nombre3]}")