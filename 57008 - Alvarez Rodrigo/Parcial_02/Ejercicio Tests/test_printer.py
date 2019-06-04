import unittest
from printer import Printer

class TestPrinter(unittest.TestCase):
    def test_lista_para_imprimir(self):
        imprem = Printer()
        printer_state = imprem.printer_available()
        self.assertTrue(printer_state)

    def test_NO_lista_para_imprimir(self):
        imprem = Printer()
        imprem.add_print_job('Impresion 1')
        imprem.print_job()
        printer_state = imprem.printer_available()
        self.assertFalse(printer_state)

    def test_algo_para_imprimir(self):
        imprem = Printer()
        imprem.add_print_job('Impresion 2')
        imprem.print_job()
        imprem.reset_printer()
        flag = imprem.error_flag
        description = imprem.error_description
        printer_state = imprem.printing
        self.assertFalse(flag)
        self.assertFalse(printer_state)
        self.assertEqual(description, '')

    def test_nada_para_imprimir(self):
        imprem = Printer()
        imprem.print_job()
        flag = imprem.error_flag
        description = imprem.error_description
        self.assertTrue(flag)
        self.assertEqual(description, 'nothing to print')

    def test_NO_reseteada_despues_de_imprimir(self):
        imprem = Printer()
        imprem.add_print_job('Impresion 3')
        imprem.print_job()
        flag = imprem.error_flag
        description = imprem.error_description
        printer_state = imprem.printing
        self.assertFalse(flag)
        self.assertTrue(printer_state)
        self.assertEqual(description, '')

if __name__ == '__main__':
    unittest.main()