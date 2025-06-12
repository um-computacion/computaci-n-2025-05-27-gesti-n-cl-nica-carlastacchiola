import unittest
from datetime import datetime
from models.turno import Turno
from models.paciente import Paciente
from models.medico import Medico
from models.especialidad import Especialidad

class TestTurno(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan", "Pérez", "12345678", "12/12/2000")
        especialidad = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        self.medico = Medico("Dr. Juan Pérez", "98765", [especialidad])
        self.fecha_hora = datetime(2025, 12, 12, 12, 0)
        self.turno = Turno(self.paciente, self.medico, self.fecha_hora, "Pediatría")

    def test_obtener_medico(self):
        self.assertEqual(self.turno.obtener_medico(), self.medico)

    def test_obtener_fecha_hora(self):
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_hora)

    def test_str_turno(self):
        result = str(self.turno)
        self.assertIn("Turno(", result)
        self.assertIn("Juan", result)
        self.assertIn("Pediatría", result)
        self.assertIn("2025-12-12 12:00:00", result)

if __name__ == '__main__':
    unittest.main()