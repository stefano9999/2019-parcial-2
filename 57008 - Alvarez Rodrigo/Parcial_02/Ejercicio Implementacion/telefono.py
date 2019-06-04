class Telefono():
    def __init__(self):
        self.credito = 0

    def dial(self, digitos):
        if len(digitos) == 3 and digitos[0] == '9' or digitos[1] == '8':
                return True
        if len(digitos) == 7:
            if self.credito < 10:
                return False
            if self.credito > 10:
                self.credito -= 10
                return True
        if len(digitos) == 10 and digitos[0] == '0' and digitos[1] == '0':
            if self.credito < 100:
                return False
            if self.credito > 100:
                self.credito -= 100
                return True

    def agregar_credito(self, dinero):
        self.credito += dinero