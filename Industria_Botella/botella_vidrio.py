from botella import botella
class botella_vidrio(botella):
    def __init__(self,material,capacidad,forma,diseño,tapa,grabados):
        super().__init__(
            "vidrio",
            material,
            capacidad,
            forma,
            diseño,
            tapa,
            grabados
        )

    def cierre_hermetico(self):
           print("la botella tiene cierre hermetico")