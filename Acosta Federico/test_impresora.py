import unittest
from impresora import Printer


class TestPrinter(unittest.TestCase):

    def test_estado_inicial_impresora(self):
        impresion = Printer()
        self.assertTrue(impresion.printer_available())
        self.assertFalse(impresion.error_flag)
        self.assertEqual(impresion.error_description, "")

    def test_impresion_ok_simple(self):
        # Impresion ok de 1 item
        # Testeo 
        impresion = Printer()
        impresion.add_print_job("Python")
        impresion.print_job()
        # Termina la impresion
        impresion.reset_printer()
        self.assertTrue(impresion.printer_available())


    def test_impresion_ok_multiple(self):
        # Impresion ok de varios items
        # Testeo General
        impresion = Printer()
        impresion.add_print_job("Hey")
        impresion.add_print_job("Vsauce")
        impresion.add_print_job("Michael")
        impresion.add_print_job("here")
        impresion.print_job()
        impresion.print_job()
        impresion.print_job()
        impresion.print_job()
        # Termina la impresion
        impresion.reset_printer()
        self.assertTrue(impresion.printer_available())

    def test_printer_unavailable(self):
        impresion = Printer()
        impresion.add_print_job("Python")
        impresion.print_job()
        self.assertFalse(impresion.printer_available())

    def test_error_empty_queue(self):
        # Cola vacia
        # Testeo de Error de cola
        impresion = Printer()
        impresion.print_job()
        self.assertTrue(impresion.error_flag)
        self.assertEqual(impresion.error_description, "nothing to print")

    def test_reseteo(self):
        # Test de reset_printer
        impresion = Printer()
        # Genero error para modificar error_flag y error_description
        impresion.print_job()
        impresion.add_print_job("Python")
        impresion.add_print_job("Python2")
        impresion.add_print_job("Python3")
        impresion.print_job()
        impresion.reset_printer()
        self.assertTrue(impresion.printer_available())
        self.assertFalse(impresion.error_flag)
        self.assertEqual(impresion.error_description, "")
    

if __name__ == '__main__':
    unittest.main()