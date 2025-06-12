from datetime import datetime
from models.excepciones import RecetaInvalidaException

class Receta:
    def __init__(self, paciente, medico, medicamentos):
        if not medicamentos or not isinstance(medicamentos, list):
            raise RecetaInvalidaException()
        
        self.__paciente = paciente 
        self.__medico = medico 
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self):
        medicamentos_str = ", ".join(self.__medicamentos)
        return (
            f"Receta(\n"
            f"{self.__paciente},\n"
            f"{self.__medico},\n"
            f"[{self.__medicamentos}],\n"
            f"{self.__fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f")"
        )

