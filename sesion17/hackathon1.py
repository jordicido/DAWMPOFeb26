# Cuenta del restaurante

precio = float(input("Indica cual es el precio de la comida: "))
propina = float(input("Indica el porcentaje de la propina: "))

precio_propina = ((precio*propina)/100)
print(f"Propina: {precio_propina:.2f}")
print(f"Precio total: {(precio+precio_propina):.2f}")