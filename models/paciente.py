from datetime import datetime

class Paciente:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento):
        
    #validaciones 
    #ningun dato esté vacío y fecha tenga formato válido
    ###############################################################
        if not nombre or not apellido or not dni: 
            raise ValueError("nombre, apellido y DNI no pueden estar vacíos")

        try:
            datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError: 
            raise ValueError("La fecha de nacimiento debe tener el formato dd/mm/aaaa")
        
    ###############################################################

        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento


    #acceso a informacion obtener dni 
    def obtener_dni(self):
        return self.__dni
    
    #representación 
    def __str__(self):
        return f"{self.__nombre} {self.__apellido} {self.__dni} {self.__fecha_nacimiento}"
    

    
