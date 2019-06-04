import unittest
from impresora import Printer


class TestPrinter(unittest.TestCase):
    def setUp(self):
        self.printer=Printer()
    def test_nada_para_imprimir(self):
        self.printer.print_job()
        self.assertTrue(self.printer.error_flag)
        self.assertEqual(self.printer.error_description,'nothing to print')
    def test_impresora_no_disponible(self):
        self.printer.add_print_job("Juan")
        self.printer.add_print_job("Pepe")
        self.printer.add_print_job("Paco")
        self.printer.print_job()
        self.assertFalse(self.printer.printer_available())
    def test_imprime_con_normalidad(self):
        self.assertTrue(self.printer.printer_available())
        self.printer.add_print_job("Estocolmo")
        self.printer.print_job()
        self.assertTrue(self.printer.printing)
        self.printer.reset_printer()
        self.assertTrue(self.printer.printer_available())
        
if __name__ == '__main__':

   unittest.main()