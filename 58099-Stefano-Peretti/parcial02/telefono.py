
class Telefono():
    def __init__(self):
        self.credito = "0"
    def agregar_credito(self,cantidad):
        self.credito += cantidad

    def dial(self, numero):
        if len(numero) == 3:
            if numero [0] == 8 or numero[0] == 9:
                return True
        else:
            return False
    def llamada_local(self, credito):
        credito =-20
    def llamda_internacional(self,credito):
        credito =-120
    