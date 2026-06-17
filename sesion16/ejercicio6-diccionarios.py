votos = {}

maximo = 0
ganador = ""

while True:
    candidato = input("Introduce el nombre del alumno candidato o FIN VOTACIONES para acabar\n")
    if candidato == "FIN VOTACIONES":
        break
    elif candidato in votos:
        votos[candidato] += 1
    else:
        votos[candidato] = 1

    if votos[candidato] > maximo:
        maximo = votos[candidato]
        ganador = candidato



print(f"El ganador ha sido {ganador} con {maximo} votos")
