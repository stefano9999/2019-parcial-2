#Juan I. Martinez, legajo 57018
import unittest 
from printer import Printer

class TestPrinter(unittest.TestCase):
    def test_check_available(self):
        impresora = Printer()
        self.assertTrue(impresora.printer_available)
    
    def test_print(self):
        impresora = Printer()
        impresora.add_print_job(123)  
        impresora.print_job()
        estado = impresora.printer_available()  
        self.assertFalse(estado)    
    
    def test_print_job_empty(self):
        impresora = Printer()
        impresora.print_job()
        prueba = impresora.error_flag
        self.assertTrue(prueba)
        self.assertEqual(impresora.error_description, "nothing to print")

    def test_reset_printer(self):
        impresora = Printer()
        impresora.reset_printer()
        estado = impresora.printing
        self.assertFalse(estado)
        

if __name__ == '__main__':
    unittest.main()