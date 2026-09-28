from zoologico import Animal

class caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__("Caballo", nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f"El caballo {self.nombre} galopa elegantemente por el campo.")

    def comunicacion(self):
        print(f"El caballo {self.nombre} relincha fuertemente para llamar a otros.")

    def sueño(self):
        print(f"El caballo {self.nombre} duerme de pie en periodos cortos.")

    def interaccion_social(self):
        print(f"El caballo {self.nombre} interactúa con su manada sumisamente o como líder.")
