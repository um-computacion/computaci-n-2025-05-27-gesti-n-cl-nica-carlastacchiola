import unittest
from models.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):

    def test_creacion_valida(self):
        especialidad = Especialidad("Cirugía Plástica", ["lunes", "miércoles"])
        self.assertEqual(especialidad.obtener_especialidad(), "Cirugía Plástica")
        self.assertEqual(str(especialidad), "Cirugía Plástica (Dias: lunes, miércoles)")

    def test_verificar_dia_true_false(self):
        especialidad = Especialidad("Neurología", ["martes", "jueves"])
        self.assertTrue(especialidad.verificar_dia("MARTES"))
        self.assertFalse(especialidad.verificar_dia("viernes"))

    def test_dias_invalidos_lanzan_error(self):
        with self.assertRaises(ValueError):
            especialidad = Especialidad("Odontología", ["lunes", "sábados"])

    def test_dias_y_tipo_vacios_lanzan_error(self):
        with self.assertRaises(ValueError):
            especialidad = Especialidad("", ["lunes", "miércoles"])
        with self.assertRaises(ValueError):
            especialidad = Especialidad("Cirugía Plástica", [])

if __name__ == '__main__':
    unittest.main()