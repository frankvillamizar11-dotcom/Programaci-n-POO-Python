from zoologico import Animal

class pez(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__("Pez", nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f"El pez nada moviendo ágilmente sus aletas y su cola.")

    def sueño(self):
        print(f"El pez descansa inmóvil flotando en el agua con los ojos abiertos.")
