'''
[{
"libro": "El señor de los anillos,
"autor": "JRR Tolkien",
"año": 1975
},
{
"libro": "El señor de los anillos,
"autor": "JRR Tolkien",
"año": 1975
}]


'''
biblioteca = []

while True:
    print("OPCIONES DE BIBLIOTECA")
    print("1. Añadir libro")
    print("2. Consultar libros por autor")
    print("3. Consultar libros por año de publicación")
    print("4. Salir")
    opcion = int(input("Elige una opción: "))

    match opcion:
        case 1:
            titulo = input("Introduce el título del libro: ")
            autor = input("Introduce el autor del libro: ")
            año = int(input("Introduce el año de publicación del libro: "))
            libro = {
                "titulo": titulo,
                "autor": autor,
                "año": año
            }
            biblioteca.append(libro)
            print(f"Se ha añadido el libro {titulo} correctamente")
        case 2:
            autor = input("Introduce el autor del libro: ")
            for i in range(len(biblioteca)):
                if biblioteca[i]["autor"] == autor:
                    print(biblioteca[i]["titulo"])
        case 3:
            año = int(input("Introduce el año de publicación del libro: "))
            for i in range(len(biblioteca)):
                if biblioteca[i]["año"] == año:
                    print(biblioteca[i]["titulo"])
        case 4:
            print("Adiós")
            break