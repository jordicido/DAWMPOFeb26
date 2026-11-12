'''
Clase alumnos con atributos basicos y un atributo notas (lista de enteros), que tenga un inicializador, y un metodo que permita añadir notas enteras entre 0 y 10 
'''
class Alumno:
    def __init__(self, nombre, ciclo, curso):
        self.nombre = nombre
        self.ciclo = ciclo
        self.curso = curso
        self.notas = list()

    def anadir_nota(self, notas):
        for nota in notas:
            if nota < 0 or nota > 10:
                raise ValueError("Todas las notas deben ser entre 0 y 10")

        self.notas.append(notas)

