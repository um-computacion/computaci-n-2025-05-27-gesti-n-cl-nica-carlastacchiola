import unittest
from datetime import datetime
from models.clinica import Clinica
from models.paciente import Paciente
from models.medico import Medico
from models.turno import Turno
from models.receta import Receta
from models.especialidad import Especialidad
from models.historia_clinica import HistoriaClinica
from models.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException, 
    DiaInvalidoException
)

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()

        self.paciente = Paciente("Eva", "Modarelli", "44010203", "19/05/2005")
        self.especialidad = Especialidad("Cirugía Plástica", ["lunes", "miércoles"])
        self.medico = Medico("Zoe", "Camus", "12345", [self.especialidad])

        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agregar_paciente_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(self.paciente)

    def test_agregar_medico_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(self.medico)

    def test_agendar_turno_valido(self):
        fecha = datetime(2025, 12, 10, 10, 0)  # miércoles
        self.clinica.agendar_turno("44010203", "12345", "Cirugía Plástica", fecha)  
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)

    def test_agendar_turno_en_dia_invalido(self):
        fecha_domingo = datetime(2025, 12, 7, 10, 0)  # domingo
        with self.assertRaises(DiaInvalidoException):
            self.clinica.agendar_turno("44010203", "12345", "Cirugía Plástica", fecha_domingo)

    def test_emitir_receta(self):
        medicamentos = ["Paracetamol", "Amoxicilina"]
        self.clinica.emitir_receta("44010203", "12345", medicamentos)

        historia = self.clinica.obtener_historia_clinica_por_dni("44010203")
        recetas = historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertIn("Paracetamol", str(recetas[0]))

if __name__ == '__main__':
    unittest.main()
