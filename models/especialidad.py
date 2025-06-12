class Especialidad:
    dias_validos = {"lunes", "martes", "miércoles", "jueves", "viernes"}

    def __init__(self, tipo, dias):

        #validaciones
        if not tipo:
            raise ValueError("El tipo de especialidad no puede estar vacío.")
        if not dias:
            raise ValueError("El dia no puede estar vacío.")
        
        dias_disponibles = [d.lower() for d in dias]
        for dia in dias_disponibles:
            if dia not in self.dias_validos:
                raise ValueError(f"El dia {dia} no es válido.")
        
        self.__tipo = tipo
        self.__dias = dias_disponibles 


    def obtener_especialidad(self):
        return self.__tipo
        
    
    def verificar_dia(self, dia):
        return dia.lower() in self.__dias
    
    def __str__(self):
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Dias: {dias_str})"
    
    