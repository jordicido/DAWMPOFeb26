evaluaciones = int(input("Introduce el número de evaluaciones: "))

for evaluacion in range(1, evaluaciones+1):
    nota = float(input(f"Notas de la evaluación {evaluacion}: "))
    suma_total = 0
    contador_notas = 0
    while nota != -1:
        suma_total += nota
        contador_notas += 1
        nota = float(input(f"Notas de la evaluación {evaluacion}: "))
    print(f"La nota media de la evaluación {evaluacion} es {suma_total/contador_notas:.2f}")