from Conseccionario import Vehiculo

class Camion(Vehiculo):
    def __init__(self, modelo, color, motor, tipo_combustible, capacidad_carga):
        super().__init__("Camión", modelo, color, motor, tipo_combustible)
        self.capacidad_carga = capacidad_carga  # Atributo especial para camiones

    def sistema_de_espejo(self):
        print("El camión ajusta sus espejos dobles laterales y convexos para eliminar puntos ciegos.")

    def tipo_de_seguridad(self):
        print("Seguridad pesada: Sistema de frenado por aire y control de estabilidad de remolque.")
