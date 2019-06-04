class Telefono ():

    def __init__ (self):

        self.credito = 0

    def dial (self, numero):
    
        if len(numero) == 3 and (numero.startswith('8') or numero.startswith('9')):
            return True
        elif numero.startswith('00') and self.credito > 100:
            self.credito -= 100
            return True
        elif len(numero) == 7 and self.credito > 10:
            self.credito -= 10
            return True
        else:
            return False

    def agregar_credito(self, pago):

        self.credito += pago


