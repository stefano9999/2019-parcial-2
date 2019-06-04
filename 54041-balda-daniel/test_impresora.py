import unittest
from impresora import Printer

class TestPrinter(unittest.TestCase):
    def setUp(self):
        self.printer = Printer()

    def test_printer_ok(self):
        self.assertTrue(self.printer.printer_available)
        self.printer.add_print_job('Test de Impresion')
        self.printer.add_print_job('Hola')
        self.printer.add_print_job('12345678')
        self.assertTrue(self.printer.print_job)

    def test_printer_nothing_print(self):
        self.printer.print_job()
        self.assertTrue(self.printer.error_flag)
        self.assertEqual(self.printer.error_description,"nothing to print")
        self.assertFalse(self.printer.printing)

    def test_printer_not_available(self):
        self.printer.add_print_job('Test de Impresion')
        self.printer.add_print_job('Hola')
        self.printer.add_print_job('12345678')
        self.printer.print_job()
        self.assertFalse(self.printer.printer_available())

    def test_print_queue(self):
        self.printer.add_print_job('Hola')
        self.assertTrue(self.printer.printer_available())
        self.printer.add_print_job('12345678')
        self.printer.add_print_job('asdasdasd')
        self.printer.add_print_job('qwerty')
        self.printer.print_job()
        self.assertFalse(self.printer.printer_available())
if __name__ == '__main__':
   unittest.main()