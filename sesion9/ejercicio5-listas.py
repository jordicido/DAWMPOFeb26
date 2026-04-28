# 1,4,2,8,3,46,12,45
# [45, 12, 46, 3, 8, 2, 4, 1]

entrada = [int(num) for num in input("Introduce una serie de numeros separados por coma: ").split(",")]
entrada.reverse()

print(f"El resultado es: {entrada}")