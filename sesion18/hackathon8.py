# Analizador de notas

# 7,5,4,6,7,4,6 => ["7","5","4"...] => [7,5,4,6,7,4,6]
notas = [int(num) for num in input("Introduce una lista de notas separadas por coma: ").split(",")]

maxima = notas[0]
minima = notas[0]
aprobados = 0
suspendidos = 0
nota_total = 0
for nota in notas:
    if nota > maxima:
        maxima = nota
    elif nota < minima:
        minima = nota
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    nota_total += nota

print(f"Máxima: {maxima}")
print(f"Minima: {minima}")
print(f"Aprobados: {aprobados}")
print(f"Suspendidos: {suspendidos}")
print(f"Media: {nota_total/len(notas)}")