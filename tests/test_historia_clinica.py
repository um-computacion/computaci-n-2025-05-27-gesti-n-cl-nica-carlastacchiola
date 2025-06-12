import unittest
from datetime import datetime
from models.historia_clinica import HistoriaClinica
from models.paciente import Paciente
from models.medico import Medico
from models.especialidad import Especialidad
from models.turno import Turno
from models.receta import Receta

class TestHistoriaClinica(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Eva", "Modarelli", "44010203", "19/05/2005")
        self.especialidad = Especialidad("Cirugía Plástica", ["lunes", "miércoles"])
        self.medico = Medico("Dr. Zoe Camus", "12345", [self.especialidad])
        self.turno = Turno(self.paciente, self.medico, datetime(2025, 12, 12, 12, 0), "Cirugía Plástica")
        self.receta = Receta(self.paciente, self.medico, ["Paracetamol", "Amoxicilina"])
        self.historia = HistoriaClinica(self.paciente)

    def test_agregar_turno(self):
        self.historia.agregar_turno(self.turno)
        self.assertIn(self.turno, self.historia.obtener_turnos())

    
    def test_agregar_receta(self):
        self.historia.agregar_receta(self.receta)
        self.assertIn(self.receta, self.historia.obtener_recetas())
    
    def test_str_historia(self):
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)
        texto =str(self.historia)
        self.assertIn("Eva Modarelli", texto)
        self.assertIn("Cirugía Plástica", texto)
        self.assertIn("Paracetamol", texto)

    
if __name__ == '__main__':
    unittest.main()