import os
from colorama import Fore, Style, Back

def pintar_terminal():
    print("Ejemplo de uso de colorama")
    print(Fore.GREEN + "Este texto es verde" + Style.RESET_ALL)
    print(Fore.BLUE + "Este texto es azul" + Style.RESET_ALL)
    print(Back.BLACK + Fore.YELLOW + "Este texto es amarillo" + Style.RESET_ALL)
    print(Fore.WHITE + "Este texto es blanco" + Style.RESET_ALL)
    print("Fin del ejemplo")

pintar_terminal()