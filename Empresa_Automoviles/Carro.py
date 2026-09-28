from Conseccionario import Vehiculo
class Carro(Vehiculo):
    def __init__(self, modelo, color, motor, tipo_combustible, n_puertas, pasajeros):
        super().__init__("Carro", modelo, color, motor, tipo_combustible)
        self.n_puertas = n_puertas
        self.pasajeros = pasajeros

    def climatizacion(self):
        print("El carro activa el aire acondicionado digital de doble zona.")

    def sistema_de_ventanas(self):
        print("Las 4 ventanas eléctricas del carro suben automáticamente.")

    def tipo_de_seguridad(self):
        print("Seguridad activa: Cuenta con 6 Airbags y frenos ABS.")
