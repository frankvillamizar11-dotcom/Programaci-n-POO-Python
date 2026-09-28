class botella:

    def __init__(self, tipo_material, material, capacidad, forma, diseño, tapa, grabados):
        self.tipo_material = tipo_material
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados

    def contenedor_liquido(self):
        print("la botella almacena liquidos")

    def facilitar_vertido(self):
        print("la botella facilita el vertido del liquido")

    def cierre_hermetico(self):
        print("la botella tiene cierre hermetico")

    def transporte(self):
        print("la botella puede transportarse ")

    def manejo(self):
        print("la botella es facil de manejar ")

    def compatibilidad_bebidas(self):
        print("la botella aguanta Frio y Calor")

    def reulitizacion(self):
        print("la botella puede ser reutilizada")

    def Transparencia(self):
        print("la botella es transparente")
