import unittest
from printer import Printer


class TestImpresora(unittest.TestCase):

    def test_printer_False_available(self):
       impresora = Printer()
       impresora.add_print_job('Imprimir')
       impresora.print_job()
       self.assertFalse(impresora.printer_available())
    
    def test_printer_True_available(self):
        impresora = Printer()
        impresora.add_print_job('Imprimir')
        self.assertTrue(impresora.printer_available())

    def test_printer_description(self):
        impresora = Printer()
        impresora.print_job()
        self.assertEqual(impresora.error_description,'nothing to print')
    
    def test_reset_error_description(self):
        impresora = Printer()
        impresora.print_job()
        impresora.reset_printer()
        self.assertEqual(impresora.error_description,'')
    
    def test_reset_printer_1(self):
        impresora = Printer()
        impresora.reset_printer()
        self.assertEqual(impresora.printing, False)
    
    def test_reset_printer_2(self):
        impresora = Printer()
        impresora.reset_printer()
        self.assertFalse(impresora.error_flag)
    
    def test_flag(self):
        impresora = Printer()
        impresora.add_print_job('imprimiendo')
        impresora.add_print_job('imprimiendo1')
        impresora.add_print_job('imprimendo2')
        impresora.add_print_job('imprimiendo3')

        self.assertFalse(impresora.error_flag, False)
    
        

if __name__ == '__main__':
   unittest.main()   