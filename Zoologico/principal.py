from caballo import caballo
from cocodrilo import cocodrilo
from escarabajo import escarabajo
from pato import pato
from pez import pez

# * Código Principal del Zoológico *


spirit = caballo("Spirit", "4 años", "Sabana/Pradera", "Herbívora", "Grande", "Marrón")
print("FICHA DE ANIMAL: CABALLO")
print(f"Nombre: {spirit.nombre} | Edad: {spirit.edad} | Color: {spirit.color}")
spirit.alimentarse()
spirit.moverse()
spirit.interaccion_social()


dandy = cocodrilo("Dandy", "12 años", "Pantano", "Carnívora", "Muy Grande", "Verde Oscuro")
print("FICHA DE ANIMAL: COCODRILO")
print(f"Nombre: {dandy.nombre} | Hábitat: {dandy.habitat}")
dandy.alimentarse()
dandy.moverse()
dandy.sueño()


hercules = escarabajo("Hércules", "6 meses", "Bosque Tropical", "Descomponedora", "Muy Pequeño", "Negro Brillante")
print(" FICHA DE ANIMAL: ESCARABAJO")
print(f"Nombre: {hercules.nombre} | Dieta: {hercules.dieta}")
hercules.instintos()
hercules.moverse()
hercules.sueño()


lucas = pato("Lucas", "1 año", "Estanque", "Omnívora", "Pequeño", "Negro")
print("FICHA DE ANIMAL: PATO")
print(f"Nombre: {lucas.nombre} | Tamaño: {lucas.tamaño}")
lucas.adaptacion()
lucas.comunicacion()
lucas.interaccion_social()


nemo = pez("Nemo", "2 años", "Arrecife de Coral", "Omnívora", "Pequeño", "Naranja y Blanco")
print("FICHA DE ANIMAL: PEZ")
print(f"Nombre: {nemo.nombre} | Hábitat: {nemo.habitat}")
nemo.descanso()
nemo.moverse()
nemo.sueño()
