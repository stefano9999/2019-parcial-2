import unittest
from printer import Printer

class TestImpresora(unittest.TestCase):
    def setUp(self):
        self.impresora = Printer()

    def test_estado_inicial(self):
        self.assertFalse(self.impresora.printing)
        self.assertFalse(self.impresora.error_flag)
        self.assertEqual(self.impresora.error_description, "")
        self.assertTrue(self.impresora.printer_available())
        self.assertEqual(self.impresora.queue_printer, [])

    def test_correcta_impresion(self):
        self.assertTrue(self.impresora.printer_available())
        self.impresora.add_print_job(['Hola mundo', 'Hola mundo 2'])
        self.impresora.print_job()
        self.assertFalse(self.impresora.error_flag)
        self.assertTrue(self.impresora.printing)
        self.assertFalse(self.impresora.printer_available())
        self.impresora.reset_printer()
        self.assertTrue(self.impresora.printer_available())
        self.assertFalse(self.impresora.error_flag)

    def test_incorrecta(self):
        self.assertTrue(self.impresora.printer_available())
        self.impresora.print_job()
        self.assertTrue(self.impresora.error_flag)
        self.assertEqual(self.impresora.error_description, "nothing to print")
        self.impresora.reset_printer()
        self.assertTrue(self.impresora.printer_available())
        self.assertFalse(self.impresora.error_flag)

if __name__ == '__main__':
   unittest.main()