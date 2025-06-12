import unittest
from models.medico import Medico
from models.especialidad import Especialidad

class TestMedico(unittest.TestCase):

    def test_creacion_valida(self):
        especialidad = Especialidad("Cirugía Plástica", ["lunes", "miércoles"])
        medico = Medico("Zoe", "Camus", "12345", [especialidad]) 
        self.assertEqual(medico.obtener_matricula(), "12345")
        self.assertIn("Cirugía Plástica", str(medico))

    def test_agregar_especialidad_y_consulta_por_dia(self):
        medico = Medico("Zoe", "Camus", "12345")
        especialidad = Especialidad("Cirugía Plástica", ["lunes", "miércoles"])
        medico.agregar_especialidad(especialidad)
        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), "Cirugía Plástica")
        self.assertIsNone(medico.obtener_especialidad_para_dia("viernes"))
    
    def test_str(self):
        medico = Medico("Zoe", "Camus", "12345")
        especialidad = Especialidad("Cirugía Plástica", ["lunes", "miércoles"])
        medico.agregar_especialidad(especialidad)
        texto =str(medico)
        self.assertIn("Zoe", texto)
        self.assertIn("Camus", texto)
        self.assertIn("12345", texto)
        self.assertIn("Cirugía Plástica", texto)
        self.assertIn("lunes", texto)
        self.assertIn("miércoles", texto)

if __name__ == '__main__':
    unittest.main()
