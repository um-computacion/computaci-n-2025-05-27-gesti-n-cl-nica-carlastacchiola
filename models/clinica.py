from datetime import datetime
from models.paciente import Paciente
from models.receta import Receta
from models.turno import Turno
from models.historia_clinica import HistoriaClinica
from models.especialidad import Especialidad
from models.medico import Medico
from models.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException,
    DiaInvalidoException

)
class Clinica:
    def __init__(self):
        self.__pacientes = {}
        self.__medicos = {}
        self.__turnos = []
        self.__historias_clinicas = {}

    # ----- REGISTRO -----
    def agregar_paciente(self, paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise ValueError("Paciente ya registrado.")
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise ValueError("Médico ya registrado.")
        self.__medicos[matricula] = medico

    def agendar_turno(self, dni, matricula, especialidad, fecha_hora):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        if dia_semana not in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
            raise DiaInvalidoException(dia_semana)

        medico = self.__medicos[matricula]
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)

        paciente = self.__pacientes[dni]
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni, matricula, medicamentos):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)

    # ----- ACCESO A INFORMACIÓN -----
    def obtener_pacientes(self):
        return list(self.__pacientes.values())

    def obtener_medicos(self):
        return list(self.__medicos.values())

    def obtener_medico_por_matricula(self, matricula):
        return self.__medicos.get(matricula)

    def obtener_turnos(self):
        return list(self.__turnos)

    def obtener_historia_clinica_por_dni(self, dni):
        return self.__historias_clinicas.get(dni)

    # ----- VALIDACIONES Y UTILIDADES -----
    def validar_existencia_paciente(self, dni):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(dni)

    def validar_existencia_medico(self, matricula):
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException(matricula)

    def validar_turno_no_duplicado(self, matricula, fecha_hora):
        for turno in self.__turnos:
            if turno.obtener_medico().obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException(turno.obtener_medico().obtener_nombre(), matricula, fecha_hora)
            
    def obtener_dia_semana_en_espanol(self, fecha_hora):
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        return dias[fecha_hora.weekday()]

    def obtener_especialidad_disponible(self, medico, dia_semana):
        return medico.obtener_especialidad_para_dia(dia_semana)

    def validar_especialidad_en_dia(self, medico, especialidad_solicitada, dia_semana):
        especialidades_en_dia = [
        e.obtener_especialidad()
        for e in medico.obtener_especialidades()
        if e.verificar_dia(dia_semana)
        ]
        if especialidad_solicitada not in especialidades_en_dia:
            raise MedicoNoDisponibleException(
            medico.obtener_nombre(),
            medico.obtener_matricula(),
            especialidad_solicitada,
            dia_semana
        )

    
    def validar_receta(self, medicamentos):
        if not medicamentos:
            raise RecetaInvalidaException()
