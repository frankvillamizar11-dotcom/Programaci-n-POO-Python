from Conseccionario import Vehiculo
class Furgoneta(Vehiculo):
    def __init__(self, modelo, color, motor, tipo_combustible, pasajeros):
        super().__init__("Furgoneta", modelo, color, motor, tipo_combustible)
        self.pasajeros = pasajeros

    def climatizacion(self):
        print("La furgoneta activa la climatización extendida para los pasajeros traseros.")

    def sistema_de_ventanas(self):
        print("Las ventanas delanteras son eléctricas; las traseras son fijas.")
