
class PacienteNoEncontradoException(Exception):
    def __init__(self, dni):
        super().__init__(f"No se encontró un paciente con el DNI: {dni}")

class MedicoNoEncontradoException(Exception):
    def __init__(self, matricula):
        super().__init__(f"No se encontró un médico con la matricula: {matricula}")

class MedicoNoDisponibleException(Exception):
    def __init__(self, nombre, matricula, especialidad, dia):
        super().__init__(f"El médico {nombre} con matricula {matricula} no está disponible para la especialidad '{especialidad}' el día {dia}")

class TurnoOcupadoException(Exception):
    def __init__(self, nombre, matricula, fecha_hora):
        super().__init__(f"El médico {nombre} con matricula {matricula} ya tiene un turno asignado en: {fecha_hora.strftime('%Y-%m-%d %H:%M')}")

class RecetaInvalidaException(Exception):
    def __init__(self):
        super().__init__("La receta debe tener al menos un medicamento válido (lista de strings)")

class DiaInvalidoException(Exception):
    def __init__(self, dia):
        super().__init__(f"No se pueden agendar turno el día {dia}. Solo se pueden agendar turnos de lunes a viernes.")

        


