from colorama import Fore, Back, Style



'''
Muestra por pantalla el texto recibido con el color indicado.

Requisitos:
El primer parámetro será el texto a mostrar.
El segundo parámetro será opcional y permitirá elegir como mínimo entre rojo, verde, amarillo, azul, cian y blanco.
Si se utiliza el color por defecto, la salida debe mantener el aspecto normal de la terminal.
Después de mostrar un mensaje coloreado, debe restablecer el formato de la consola.
No devolverá ningún valor.'''
def mostrar_mensaje(texto, color="blanco"):
    if color == "blanco":
        print(texto)
    elif color == "rojo":
        print(Fore.RED + texto + Style.RESET_ALL)
    elif color == "azul":
        print(Fore.BLUE + texto + Style.RESET_ALL)
    elif color == "cian":
        print(Fore.CYAN + texto + Style.RESET_ALL)
    elif color == "amarillo":
        print(Fore.YELLOW + texto + Style.RESET_ALL)
    elif color == "verde":
        print(Fore.GREEN + texto + Style.RESET_ALL)

'''
Imprime un título destacado y centrado entre separadores.

Requisitos:

Recibir el texto del título y una anchura opcional.
Mostrar una línea separadora arriba y otra abajo.
Centrar el texto con relación a la anchura indicada.
Utilizar algún color o estilo para destacar el título.
Evitar que un título largo se corte: si no cabe en la anchura indicada, adaptar el formato para mostrarlo completo.
'''
def mostrar_titulo(texto, ancho=50):
    '''
    ====================
    TITULO
    ====================
    '''
    longitud_texto = len(texto)
    if longitud_texto > ancho:
        ancho = longitud_texto + 4
    mitad_ancho = ancho // 2
    mitad_texto = longitud_texto // 2
    numero_espacios = mitad_ancho - mitad_texto

    print("=" * ancho)
    print(" " * numero_espacios, texto.upper(), sep="")
    print("=" * ancho)
    pass

def mostrar_menu(titulo, opciones):
    pass

def mostrar_lista(elementos, titulo="Listado"):
    pass

def mostrar_ficha(datos, titulo="Información"):
    pass