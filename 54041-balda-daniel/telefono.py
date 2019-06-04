class Telefono(object):
    def __init__(self):
        self.credito = 0

    def agregar_credito(self, credito):
        self.credito = credito

    def descontar_credito(self, numero):
            self.credito -= numero

    def dial(self, numero):
        self.numero = numero
        if len(numero) == 3 and (numero[0] == '9' or numero[0] == '8'):
            return True
        if len(numero) == 7 and self.credito >= 10:
            self.descontar_credito(10)
            return True
        if len(numero) >= 7 and numero[0:1] == '0' and self.credito >= 100:
            self.descontar_credito(100)
            return True
        return False