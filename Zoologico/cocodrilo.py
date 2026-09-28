from zoologico import Animal

class cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__("Cocodrilo", nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f"El cocodrilo {self.nombre} nada de forma sigilosa bajo el agua.")

    def comunicacion(self):
        print(f"El cocodrilo emite bramidos graves durante la época de apareamiento.")

    def sueño(self):
        print(f"El cocodrilo {self.nombre} entra en un estado de letargo con un ojo abierto.")
