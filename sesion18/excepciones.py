# Lee un número y dice si es par o impar
while True:
    try:
        num = int(input("Escribe un número: "))
        if num%2 == 0:
            print("Es par")
        else:
            print("Es impar")
    except Exception:
        print(f"Entro en exception")
    except TypeError:
        print("Entro en typeError")

