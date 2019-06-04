import unittest

from printer import Printer

class TestPrinter(unittest.TestCase):

    def test_printer_1(self):
       
        impresora = Printer()
        impresora.add_print_job('Imprimir esto')
        impresora.print_job()
        self.assertFalse(impresora.printer_available()) 

    def test_printer_2(self):
       
        impresora = Printer()
        impresora.add_print_job('Imprimir esto')
        impresora.print_job()
        impresora.reset_printer()
        self.assertTrue(impresora.printer_available()) 

    def test_printer_3(self):
       
        impresora = Printer()
        impresora.print_job()
        self.assertEqual(impresora.error_description, 'nothing to print')

    def test_printer_4(self):
       
        impresora = Printer()
        impresora.print_job()
        self.assertTrue(impresora.error_flag)

    
    def test_printer_5(self):
       
        impresora = Printer()
        impresora.print_job()
        impresora.reset_printer()
        self.assertEqual(impresora.error_description, '')

    def test_printer_6(self):
       
        impresora = Printer()
        impresora.print_job()
        impresora.reset_printer()
        self.assertFalse(impresora.error_flag)

    def test_printer_7(self):
       
        impresora = Printer()
        impresora.add_print_job('Hola')
        impresora.add_print_job('imprimir')
        impresora.add_print_job('imprimir este string')
        impresora.add_print_job('123456')
        impresora.add_print_job('holaholahola')
        impresora.print_job()
        impresora.reset_printer()
        impresora.print_job()
        impresora.reset_printer()
        impresora.print_job()
        impresora.reset_printer()
        
        self.assertFalse(impresora.error_flag)

    def test_printer_8(self):
       
        impresora = Printer()
        impresora.add_print_job('Hola')
        impresora.add_print_job('imprimir')
        impresora.add_print_job('imprimir este string')
        impresora.add_print_job('123456')
        impresora.add_print_job('holaholahola')
        impresora.print_job()
        impresora.reset_printer()
        impresora.print_job()
        impresora.reset_printer()
        
        self.assertEqual(impresora.error_description, '')

    def test_printer_9(self):
       
        impresora = Printer()
        impresora.add_print_job('Hola')
        impresora.add_print_job('imprimir')
        impresora.add_print_job('imprimir este string')
        impresora.add_print_job('123456')
        impresora.add_print_job('holaholahola')
        impresora.print_job()
        impresora.reset_printer()
        impresora.print_job()
        
        self.assertTrue(impresora.printing)

    def test_printer_10(self):
       
        impresora = Printer()
        impresora.add_print_job('Hola')
        impresora.add_print_job('imprimir')
        impresora.add_print_job('imprimir este string')
        impresora.add_print_job('123456')
        impresora.add_print_job('holaholahola')
        impresora.print_job()
        impresora.reset_printer()
        impresora.print_job()
        impresora.reset_printer()
        impresora.print_job()
        impresora.reset_printer()
        
        self.assertFalse(impresora.printing)
    


if __name__ == '__main__':
   unittest.main()