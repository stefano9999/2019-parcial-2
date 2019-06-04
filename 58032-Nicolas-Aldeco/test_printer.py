import unittest
from printer import Printer

class TestImpresora(unittest.TestCase):
    def test_inicial(self):
        impresora = Printer()
        #Estado de la maquina
        self.assertFalse(impresora.printing)
        self.assertFalse(impresora.error_flag)
        self.assertEqual(impresora.error_description,'')
        #Nada imprimendo
        self.assertTrue(impresora.printer_available())
        #Nada en la cola
        self.assertEqual(impresora.queue_printer,[])

    def test_impresion_ok_nadie_imprimiendo(self):
        impresora = Printer()
        impresora.add_print_job('HOLA JORGE')
        impresora.print_job()
        #Estado durante la impresion
        self.assertFalse(impresora.printer_available())
        self.assertFalse(impresora.error_flag)
        self.assertEqual(impresora.queue_printer,[])
        #Estado despues de la impresion
        impresora.reset_printer()
        self.assertTrue(impresora.printer_available())
        self.assertFalse(impresora.error_flag)

    def test_muchas_impresiones(self):
        impresora = Printer()
        impresora.add_print_job(['Hola Mabel','123','Perraco'])
        impresora.print_job()
        #Estado durante la impresion
        self.assertFalse(impresora.printer_available())
        self.assertFalse(impresora.error_flag)
        self.assertEqual(impresora.queue_printer,[])
        #Estado despues de la impresion
        impresora.reset_printer()
        self.assertTrue(impresora.printer_available())
        self.assertFalse(impresora.error_flag)

    def test_impresion_nada_para_imprimir(self):
        impresora = Printer()
        impresora.print_job()
        #Error
        self.assertTrue(impresora.error_flag)
        self.assertEqual(impresora.error_description,'nothing to print')
        #Reinicio despues del error
        impresora.reset_printer()
        self.assertFalse(impresora.printing)
        self.assertFalse(impresora.error_flag)


if __name__ == "__main__":
    unittest.main()