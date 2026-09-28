from Carro import Carro
from Camion import Camion
from Furgoneta import Furgoneta

# * Código Principal *

mi_carro = Carro("Mazda 3", "Rojo", "2.0L", "Gasolina", 4, 5)
print("DATOS DEL CARRO")
print(f"Modelo: {mi_carro.modelo} | Pasajeros: {mi_carro.pasajeros}")
mi_carro.arranque()
mi_carro.climatizacion()
mi_carro.tipo_de_seguridad()

mi_camion = Camion("Volvo FH", "Blanco", "13L Diésel", "Apm", "30 Toneladas")
print("DATOS DEL CAMIÓN")
print(f"Modelo: {mi_camion.modelo} | Carga: {mi_camion.capacidad_carga}")
mi_camion.arranque()
mi_camion.sistema_de_espejo()
mi_camion.tipo_de_seguridad()

mi_furgoneta = Furgoneta("Renault Master", "Gris", "2.3 dCi", "Diésel", 12)
print(" DATOS DE LA FURGONETA")
print(f"Modelo: {mi_furgoneta.modelo} | Capacidad Pasajeros: {mi_furgoneta.pasajeros}")
mi_furgoneta.arranque()
mi_furgoneta.climatizacion()
