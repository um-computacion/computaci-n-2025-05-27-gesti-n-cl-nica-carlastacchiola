class HistoriaClinica:
    def __init__(self, paciente):


        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

    def agregar_turno(self, turno):
        self.__turnos.append(turno)

    def obtener_turnos(self):
        return list(self.__turnos) 
    
    def obtener_recetas(self):
        return list(self.__recetas)
    
    def agregar_receta(self, receta):
        self.__recetas.append(receta)
    
    def __str__(self):
        turnos_str = "\n  ".join(str(turno) for turno in self.__turnos)
        recetas_str = "\n  ".join(str(receta) for receta in self.__recetas)

        return (
        f"Historia Clínica del paciente:\n"
        f"  {self.__paciente}\n"
        f"\nTurnos:\n  {turnos_str if turnos_str else 'Sin turnos registrados.'}\n"
        f"\nRecetas:\n  {recetas_str if recetas_str else 'Sin recetas registradas.'}"
    )
