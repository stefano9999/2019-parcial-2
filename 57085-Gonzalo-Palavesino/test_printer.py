import unittest
from printer import Printer

class TestPrinter(unittest.TestCase):
    def test_ready_to_print(self):
        epson = Printer()
        printer_state = epson.printer_available()
        self.assertTrue(printer_state)

    def test_NOT_ready_to_print(self):
        epson = Printer()
        epson.add_print_job('Impresion 1')
        epson.print_job()
        printer_state = epson.printer_available()
        self.assertFalse(printer_state)

    def test_something_to_print(self):
        epson = Printer()
        epson.add_print_job('Impresion 2')
        epson.print_job()
        epson.reset_printer()
        flag = epson.error_flag
        description = epson.error_description
        printer_state = epson.printing
        self.assertFalse(flag)
        self.assertFalse(printer_state)
        self.assertEqual(description, '')

    def test_nothing_to_print(self):
        epson = Printer()
        epson.print_job()
        flag = epson.error_flag
        description = epson.error_description
        self.assertTrue(flag)
        self.assertEqual(description, 'nothing to print')

    def test_NOT_reseted_after_print(self):
        epson = Printer()
        epson.add_print_job('Impresion 3')
        epson.print_job()
        flag = epson.error_flag
        description = epson.error_description
        printer_state = epson.printing
        self.assertFalse(flag)
        self.assertTrue(printer_state)
        self.assertEqual(description, '')

    





if __name__ == '__main__':
  unittest.main()