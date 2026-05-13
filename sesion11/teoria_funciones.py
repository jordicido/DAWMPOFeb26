'''
def: palabra reservada que indica que se va a definir una función.
nombre_funcion: identificador que le damos a la función. Se recomienda usar minúsculas y guiones bajos (snake_case) si tiene varias palabras.
parámetros: variables que recibe la función como entrada (pueden ser cero o más).
return: sirve para devolver un resultado desde la función (es opcional).
'''

def saludar(nombre="mundo"):
    print(f"Hola {nombre}!")

saludar("Jordi")


def suma_dos_enteros(numero1, numero2):
    return numero1 + numero2

print(f"La suma de 2 + 2 es {suma_dos_enteros(2,2)}")
