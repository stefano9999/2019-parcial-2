import unittest
from telefono import Telefono


class TestTelefono(unittest.TestCase):

   def test_llamada_gratis(self):
       # si la llamada es de 3 digitos,
       # la llamada es gratis, debe empezar con 9 u 8
       fono = Telefono()
       llamada_ok = fono.dial('911')
       self.assertTrue(llamada_ok)

   def test_llamada_gratis_error(self):
       # si la llamada es de 3 digitos,
       # la llamada es gratis, debe empezar con 9 u 8
       fono = Telefono()
       llamada_ok = fono.dial('111')
       self.assertFalse(llamada_ok)

   def test_llamada_local_error(self):
       # si la llamada es de 7 digitos, es local
       # debe tener credito mayor a 10
       fono = Telefono()
       llamada_ok = fono.dial('4234729')
       # no hay credito
       self.assertFalse(llamada_ok)

   def test_llamada_local_ok(self):
       # si la llamada es de 7 digitos, es local
       # debe tener credito mayor a 10
       fono = Telefono()
       fono.agregar_credito(30)
       llamada_ok = fono.dial('4234729')
       # hay credito
       self.assertTrue(llamada_ok)
       self.assertEqual(fono.credito, 20)

   def test_llamada_internacional_error(self):
       # si la llamada comienza con 00, es internacional
       # debe tener credito mayor a 100
       fono = Telefono()
       fono.agregar_credito(30)
       llamada_ok = fono.dial('0014234729')
       # no hay credito
       self.assertFalse(llamada_ok)

   def test_llamada_intenacional_ok(self):
       # si la llamada comienza con 00, es internacional
       # debe tener credito mayor a 100
       fono = Telefono()
       fono.agregar_credito(120)
       llamada_ok = fono.dial('0014234729')
       # hay credito
       self.assertTrue(llamada_ok)
       self.assertEqual(fono.credito, 20)


if __name__ == '__main__':
   unittest.main()