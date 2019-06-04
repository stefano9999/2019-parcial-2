from printer import Printer
import unittest

class Test_printer(unittest.TestCase):
    def setUp(self):
        self.printer = Printer()
        self.print_jobs = ['print job 1', 'print job 2',
            'print job3', 'print job 4', 'print job 5']
    
    def test_print_ok(self):
        # llenar impresora
        for value in self.print_jobs:
            self.printer.add_print_job(value)
        self.assertTrue(self.printer.queue_printer)

        #imprimir
        available = self.printer.printer_available()
        self.assertTrue(available)
        if available:
            self.printer.print_job()
        self.assertTrue(self.printer.printing)
        self.assertEqual(len(self.printer.queue_printer), len(self.print_jobs) -1)

        # resetear la impresora
        self.printer.reset_printer()
        self.assertFalse(self.printer.printing)
        
    def test_print_not_available(self):
        # llenar impresora
        for value in self.print_jobs:
            self.printer.add_print_job(value)
        self.assertTrue(self.printer.queue_printer)
        self.assertEqual(len(self.printer.queue_printer), len(self.print_jobs))

        # imprimir
        available = self.printer.printer_available()
        self.assertTrue(available)
        if available:
            self.printer.print_job()
        self.assertTrue(self.printer.printing)
        self.assertEqual(len(self.printer.queue_printer), len(self.print_jobs) - 1)

        # tratar de imprimir con la impresora en uso
        available = self.printer.printer_available()
        self.assertFalse(available)
        if available:
            self.printer.print_job()
        self.assertEqual(len(self.printer.queue_printer), len(self.print_jobs) - 1)
        
        # resetear la impresora
        self.printer.reset_printer()
        self.assertFalse(self.printer.printing)
    
    def test_nothing_to_print(self):
        self.assertFalse(self.printer.queue_printer)

        #imprimir
        available = self.printer.printer_available()
        self.assertTrue(available)
        if available:
            self.printer.print_job()
        self.assertFalse(self.printer.printing)
        self.assertFalse(self.printer.queue_printer)
        self.assertFalse(self.printer.printing)
        self.assertEqual(self.printer.error_description, "nothing to print")

    def test_print_2(self):
        # llenar impresora
        for value in self.print_jobs:
            self.printer.add_print_job(value)
        self.assertTrue(self.printer.queue_printer)

        #imprimir
        available = self.printer.printer_available()
        self.assertTrue(available)
        self.assertEqual(len(self.printer.queue_printer), len(self.print_jobs))
        if available:
            self.printer.print_job()
        self.assertTrue(self.printer.printing)
        self.assertEqual(len(self.printer.queue_printer), len(self.print_jobs) - 1)

        # resetear la impresora
        self.printer.reset_printer()
        self.assertFalse(self.printer.printing)

        #imprimir
        available = self.printer.printer_available()
        self.assertTrue(available)
        self.assertEqual(len(self.printer.queue_printer), len(self.print_jobs) - 1)
        if available:
            self.printer.print_job()
        self.assertTrue(self.printer.printing)
        self.assertEqual(len(self.printer.queue_printer), len(self.print_jobs) - 2)

        # resetear la impresora
        self.printer.reset_printer()
        self.assertFalse(self.printer.printing)

if __name__ == '__main__':
    unittest.main()