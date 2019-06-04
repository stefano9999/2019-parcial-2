import unittest
from printer import Printer


class TestPrinter(unittest.TestCase):
    def setUp(self):
        self.epson=Printer()

    def test_inicial_lista(self):
      
        self.assertFalse(self.epson.printing)
        self.assertFalse(self.epson.error_flag)
        self.assertEqual(self.epson.error_description,'')
        self.assertTrue(self.epson.printer_available())
        self.assertEqual(self.epson.queue_printer,[])

    def test_Error(self):
        self.assertTrue(self.epson.printer_available())
        self.epson.print_job()
        self.assertTrue(self.epson.error_flag)
        self.assertEqual(self.epson.error_description, "nothing to print")
        self.epson.reset_printer()
        self.assertTrue(self.epson.printer_available())
        self.assertFalse(self.epson.error_flag)

    def test_impresion_valida(self):
        self.assertTrue(self.epson.printer_available())
        self.epson.add_print_job(['Numeros', 'excel'])
        self.epson.print_job()
        self.assertFalse(self.epson.error_flag)
        self.assertTrue(self.epson.printing)
        self.assertFalse(self.epson.printer_available())
        self.epson.reset_printer()
        self.assertTrue(self.epson.printer_available())
        self.assertFalse(self.epson.error_flag)

if __name__ == "__main__":
    unittest.main()