import unittest
from printer import Printer

class TestPrinter(unittest.TestCase):

    def test_agregar(self):        
        impresora = Printer()
        impresora.add_print_job('Hola')
        self.assertEqual(impresora.queue_printer[0], 'Hola')

    def test_something_to_print (self):
        impresora = Printer()
        impresora.add_print_job('Algo para imprimir')
        impresora.print_job()
        self.assertTrue(impresora.printing)
        self.assertFalse(impresora.error_flag)

    def test_nothing_to_print (self):
        impresora = Printer()
        
        impresora.print_job()
        self.assertFalse(impresora.printing)
        self.assertTrue(impresora.error_flag)


    def test_available(self):
        impresora = Printer() #cuando prende esta disponible
        self.assertTrue(impresora.printer_available())

    def test_no_available(self):
        impresora = Printer() 

        impresora.add_print_job('Algo para imprimir') #suponemos que esta imprimiendo algo
        impresora.print_job()

        self.assertFalse(impresora.printer_available())

    def test_reset(self):

        impresora = Printer() 

        impresora.add_print_job('Algo para imprimir') 
        impresora.print_job() #cambiamos los valores iniciales

        impresora.reset_printer() #volvemos a los valores iniciales

        self.assertFalse(impresora.error_flag)
        self.assertFalse(impresora.printing)
        self.assertEqual(impresora.error_description,'')




    
    


if __name__ == '__main__':
  unittest.main()