from models.especialidad import Especialidad

class Medico: 
    def __init__(self, nombre, apellido, matricula, especialidades = None):

        #validaciones
        if not nombre or not matricula:
            raise ValueError("Nombre y Matricula no pueden estar vacíos.")
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__matricula = matricula
        self.__especialidades = especialidades if especialidades else []

    def __str__(self):
        especialidades_str = ", ".join(str(e) for e in self.__especialidades)
        return f"{self.__nombre}, {self.__apellido}, {self.__matricula}, [{especialidades_str}]"
    
    def agregar_especialidad(self, especialidad):
        self.__especialidades.append(especialidad)

    def obtener_matricula(self):
        return self.__matricula
    
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_apellido(self):
        return self.__apellido
    
    def obtener_especialidad_para_dia(self, dia):
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
        return None
    
    def obtener_especialidades(self):
        return self.__especialidades