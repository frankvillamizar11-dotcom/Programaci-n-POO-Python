from botella_plastica import botella_plastica
from botella_vidrio import botella_vidrio


#* Codigo Principal *

plastico = botella_plastica(
    "plastica",
    "1 litro",
    "cilindrica",
    "transparente",
    "rosca",
    "sin grabados"
)

vidrio = botella_vidrio(
    "vidrio",
    "750 ml",
    "cilindrica",
    "transparente",
    "twist-off",
    "grabado"
)

print(f"botella de plastico:")
print(f"Material: {plastico.material}")
print(f"Capacidad: {plastico.capacidad}")
print(f"Forma: {plastico.forma}")
print(f"Diseño: {plastico.diseño}")
print(f"Tapa: {plastico.tapa}")
print(f"Grabados: {plastico.grabados}")

plastico.reutilizacion()

print(f"botella de Vidrio:")
print(f"Material: {vidrio.material}")
print(f"Capacidad: {vidrio.capacidad}")
print(f"Forma: {vidrio.forma}")
print(f"Diseño: {vidrio.diseño}")
print(f"Tapa: {vidrio.tapa}")
print(f"Grabados: {vidrio.grabados}")

vidrio.cierre_hermetico()