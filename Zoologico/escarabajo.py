from zoologico import Animal

class escarabajo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__("Escarabajo", nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f"El escarabajo camina sobre la tierra y abre sus alas para volar distancias cortas.")

    def sueño(self):
        print(f"El escarabajo se esconde bajo las hojas para pasar las horas de frío de la noche.")
