import unittest
from datetime import datetime 
from models.paciente import Paciente

class TestPaciente(unittest.TestCase):

    def test_creacion_valida(self):
        paciente = Paciente("Eva", "Modarelli", "44010203","19/05/2005")
        self.assertEqual(paciente.obtener_dni(), "44010203")
        self.assertEqual(str(paciente), "Eva Modarelli 44010203 19/05/2005")

    def test_creacion_nombre_vacio(self):
        with self.assertRaises(ValueError):
            paciente = Paciente("", "Modarelli", "44010203","19/05/2005")
    
    def test_creacion_dni_vacio(self):
        with self.assertRaises(ValueError):
            paciente = Paciente("Eva", "Modarelli", "","19/05/2005")
    
    def test_fecha_invalida_lanza_error(self):
        with self.assertRaises(ValueError):
            paciente = Paciente("Eva", "Modarelli", "44010203","33/14/2005")

if __name__ == '__main__':
    unittest.main() 


