from zoologico import Animal

class pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__("Pato", nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f"El pato {self.nombre} camina por la orilla y nada de forma fluida.")

    def comunicacion(self):
        print(f"El pato {self.nombre} grazna ('cuac') repetidamente.")

    def sueño(self):
        print(f"El pato duerme en la orilla junto a sus compañeros.")

    def interaccion_social(self):
        print(f"El pato {self.nombre} comparte el estanque de forma amigable en grupo.")
