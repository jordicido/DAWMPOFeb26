# Inventario de objetos

inventario = ["espada", "poción", "escudo"]

opcion = 0
while opcion != 5:
    print("""
1. Ver inventario
2. Añadir objeto
3. Usar objeto
4. Buscar objeto
5. Salir
""")
    opcion = int(input("Qué quieres hacer?\n"))
    match(opcion):
        case 1:
            print("Inventario:")
            for i in range(len(inventario)):
                print(f"{i+1}. {inventario[i]}")
        case 2:
            item = input("Qué objeto quieres añadir?\n")
            inventario.append(item)
        case 3:
            item = input("Qué objeto quieres usar?\n")
            if item in inventario:
                inventario.remove(item)
                print(f"Se ha usado un/a {item}")
            else:
                print(f"No existe {item} en el inventario")
        case 4:
            item = input("Qué objeto quieres buscar?\n")
            if item in inventario:
                print(f"Hay {inventario.count(item)} unidades de {item}")
            else:
                print(f"No existe {item} en el inventario")
        case 5:
            print("Au revoir") 
        case default:
            print("Escoge una opción de 1 a 5")
           

    