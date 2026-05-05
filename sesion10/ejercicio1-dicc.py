'''
ESPAÑA-MADRID
FRANCIA-PARIS
HOLANDA-AMSTERDAM
RUMANIA-BUCAREST
FIN INSERCIONES
Que capital quieres consultar?
ESPAÑA
La capital de España es Madrid
Salir

0- Crear el diccionario vacio
1- Pedir al usuario que introduzca pares de PAIS-CAPITAL hasta que introduzca FIN INSERCIONES
2- Ir almacenando los pares Pais, capital en un diccionario
3- Pedir al usuario que introduzca un país del que quiera consultar su capital hasta que introduzca salir
4- Ir imprimiendo las capitales de los paises introducidos
'''
diccionario_paises = {}
entrada = input("Introduce un par PAIS-CAPITAL o FIN INSERCIONES: ")

while entrada != "FIN INSERCIONES":
    # "ESPAÑA-MADRID"
    pais, capital = entrada.split("-") # [ESPAÑA, MADRID]
    diccionario_paises[pais] = capital
    entrada = input("Introduce un par PAIS-CAPITAL o FIN INSERCIONES: ")

consulta_pais = input("Introduce un país para consultar su capital o SALIR: ")

while consulta_pais != "SALIR":
    # Si existe la entrada imprimir capital
    # sino imprimir no existe en el diccionario
    if consulta_pais in diccionario_paises:
        print(f"La capital de {consulta_pais} es {diccionario_paises[consulta_pais]}")
    else:
        print(f"La entrada {consulta_pais} no existe en el diccionario")    
    consulta_pais = input("Introduce un país para consultar su capital o SALIR: ")
