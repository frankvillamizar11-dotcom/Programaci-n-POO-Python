class Animal:
    def __init__(self, especie, nombre, edad, habitat, dieta, tamaño, color):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    def alimentarse(self):
        print(f"El {self.especie} ({self.nombre}) está comiendo su ración basada en una dieta {self.dieta}.")

    def reproducirse(self):
        print(f"El {self.especie} sigue sus ciclos naturales de reproducción.")

    def adaptacion(self):
        print(f"El {self.especie} se adapta perfectamente a su hábitat de tipo {self.habitat}.")

    def instintos(self):
        print(f"El {self.especie} actúa de acuerdo a sus instintos de supervivencia.")

    def descanso(self):
        print(f"El {self.especie} reposa en un lugar seguro para recuperar energías.")
