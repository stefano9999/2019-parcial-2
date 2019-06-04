class Telefono():

    def __init__(self):
        self.credito = 0
    
    def agregar_credito(self,plata):
        self.credito += plata
    
    def dial(self,numero):
        if len(numero) == 3:
            if numero[0] == '8' or numero[0] == '9':
                return True
        if len(numero) == 7:
            if self.credito < 10:
                return False
            if self.credito >= 10:
                self.credito -= 10
                return True
        if len(numero) == 10 and numero[0] == '0' and numero[1] == '0':
            if self.credito < 100:
                return False
            if self.credito >= 100:
                self.credito -= 100
                return True

