import unittest
from printer import Printer


class TestTelefono(unittest.TestCase):

    def setUp(self):
        self.printer = Printer()

    def test_printer_available(self):
        #Tener en cuenta que la impresora no esta imprimiendo
        self.assertTrue(self.printer.printer_available())
   
    def test_printer_not_available(self):        
        self.printer.printing = True
        self.assertFalse(self.printer.printer_available())
    
    def test_printer_adding_to_queue(self):        
        self.printer.add_print_job('Printing example')
        self.assertEqual(self.printer.queue_printer,['Printing example'])
    
    def test_printer_printing_job(self):
        self.printer.queue_printer = ['Printing example']
        self.printer.print_job()
        self.assertTrue(self.printer.printing)
        self.assertEqual(self.printer.queue_printer,[])
    
    def test_printer_nothing_to_print(self):
        #Tener en cuenta que la cola de impresion esta vacia
        self.printer.print_job()
        self.assertTrue(self.printer.error_flag)
        self.assertEqual(self.printer.error_description,'nothing to print')

    def test_printer_reset(self):
        self.printer.reset_printer()
        self.assertFalse(self.printer.printing)
        self.assertFalse(self.printer.error_flag)
        self.assertEqual(self.printer.error_description,'')

if __name__ == '__main__':
    unittest.main()