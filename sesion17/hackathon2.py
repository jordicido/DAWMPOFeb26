# Calculo de tiempo a partir de segundos

segundos = int(input("Introduce segundos: "))

horas = segundos // 3600
segundos = segundos%3600
minutos = segundos // 60
segundos = segundos%60

print(f"{horas} h {minutos} min {segundos} s")

# 02:MM:SS