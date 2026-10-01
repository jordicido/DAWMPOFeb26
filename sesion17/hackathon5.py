# Cuenta atrás

contador = int(input("Introduce el tiempo de la cuenta atrás: "))

for i in range(contador, 0, -1):
    print(i, end="")
    if i <= 3:
        print(" ¡CORRE!", end="")
    print()

print("BOOM")