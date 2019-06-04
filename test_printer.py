import unittest
from printer import Printer

class TestPrinter(unittest.TestCase):

    def test_estado_inicial(self):
       impresora = Printer()
       impresion_ok = impresora.printer_available()
       self.asserFalse(impresion_ok)

if __name__ == '__main__':
   unittest.main()