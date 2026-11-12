class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.km = 0

    def anadir_km(self, num_km):
        if num_km < 0:
            raise ValueError("El km no puede ser negativo")
        self.km = num_km

    def tocar_bocina(self):
        print("meec meeec")


coche = Vehiculo("Toyota", "Yaris")
moto = Vehiculo("Aprillia", "Racing")
numero = 6

try:
    coche.anadir_km(-1000)
except ValueError as error:
    print(f"Error: {error}")

print(coche.km)

lista_vehiculos = [Vehiculo("Toyota", "Yaris"), Vehiculo("Aprillia", "Racing"), Vehiculo("Opel", "Corsa")]

for vehiculo in lista_vehiculos:
    print(f"Vehiculo: {vehiculo.marca} {vehiculo.modelo}")