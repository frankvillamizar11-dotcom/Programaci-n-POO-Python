class Vehiculo:
    def __init__(self, tipo_vehiculo, modelo, color, motor, tipo_combustible):
        self.tipo_vehiculo = tipo_vehiculo
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.tipo_combustible = tipo_combustible

    def arranque(self):
        print(f"El {self.tipo_vehiculo} ha encendido el motor.")

    def apagado(self):
        print(f"El {self.tipo_vehiculo} se ha apagado.")

    def aceleracion_y_frenado(self):
        print(f"El {self.tipo_vehiculo} acelera suavemente y prueba sus frenos.")

    def sistema_de_direccion(self):
        print(f"El {self.tipo_vehiculo} utiliza dirección asistida.")

    def luces(self):
        print(f"Las luces del {self.tipo_vehiculo} están encendidas.")
