from datetime import datetime
from models.especialidad import Especialidad
from models.medico import Medico
from models.paciente import Paciente

class Turno:
    def __init__(self, paciente, medico, fecha_hora, especialidad):
    
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad
    
    def obtener_medico(self):
        return self.__medico
    
    def obtener_fecha_hora(self):
        return self.__fecha_hora
    
    def __str__(self):
        return f"Turno(\n{self.__paciente},\n{self.__medico},\n{self.__fecha_hora},\n{self.__especialidad}\n)"