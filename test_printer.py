import unittest

from printer import Printer

class TestPrinter(unittest.TestCase):
    def setUp(self):
        self.imp = Printer()

    def test_impresion_valida(self):
        self.assertTrue(self.imp.printer_available())
        self.imp.add_print_job('Hola mundo')
        self.imp.print_job()

        self.assertFalse(self.imp.error_flag)
        self.assertTrue(self.imp.printing)

        self.assertFalse(self.imp.printer_available())
        self.imp.reset_printer()
        self.assertTrue(self.imp.printer_available())


    def test_impresion_incorrecta(self):
        self.assertTrue(self.imp.printer_available())

        self.imp.print_job()

        self.assertTrue(self.imp.error_flag)
        self.assertEqual(self.imp.error_description, "nothing to print")

        self.imp.reset_printer()
        self.assertTrue(self.imp.printer_available())

        


if __name__ == '__main__':
   unittest.main()