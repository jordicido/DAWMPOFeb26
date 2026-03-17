# le pasas un numero y te dice si:
#1. es multiple de 3
#2. si es mutiple de 5
#3. si es multiple de 3 y de 5
#4. No es multiple de ninguno de los dos

numero = int(input("Dime un número:\n"))

if numero%3 == 0 and numero%5 == 0:
    print("Es múltiplo de 3 y de 5")
elif numero%3 == 0:
    print("Es múltiplo de 3")
elif numero%5 == 0:
    print("Es múltiplo de 5")
else:
    print("No es múltiplo de ninguno")