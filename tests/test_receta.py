import unittest
from datetime import datetime
from models.receta import Receta
from models.paciente import Paciente
from models.medico import Medico
from models.especialidad import Especialidad
from models.excepciones import RecetaInvalidaException

class TestReceta(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Eva", "Modarelli", "44010203", "19/05/2005")
        self.especialidad = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        self.medico = Medico("Zoe", "Camus", "12345", [self.especialidad])
        self.medicamentos= ["Paracetamol", "Amoxicilina"]
        self.fecha = datetime(2005, 5, 19, 0, 0)
        

    def test_creacion_valida(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        receta_str =str(receta)
        self.assertIn("Eva", receta_str)
        self.assertIn("Modarelli", receta_str)
        self.assertIn("Paracetamol", receta_str)
        self.assertIn("Amoxicilina", receta_str)
        self.assertIn("Zoe", receta_str)
        self.assertIn("Camus", receta_str)
        self.assertIn("Pediatría", receta_str)

    def test_medicamentos_vacios(self):
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.paciente, self.medico, [])

    def test_medicamentos_no_lista(self):
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.paciente, self.medico, "Paracetamol")


if __name__ == '__main__':
    unittest.main()