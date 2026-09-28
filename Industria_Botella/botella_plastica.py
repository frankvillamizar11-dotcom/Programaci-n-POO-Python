from botella import botella
class botella_plastica(botella):
    def __init__(self,material,capacidad,forma,diseño,tapa,grabados):
        super().__init__(
            "plastico",
            material,
            capacidad,
            forma,
            diseño,
            tapa,
            grabados
        )

    def reutilizacion(self):
        print("la botella de plastico puede reutilizarse")