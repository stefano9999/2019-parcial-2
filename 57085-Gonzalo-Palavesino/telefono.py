class Telefono():
    def __init__(self):
        self.credito = 0
        
    def dial(self, digits):

        cant = len(digits)
        if digits[0] == '9' or digits[0] == '8':
            if cant == 3:
                return True
        elif (cant <= 7) and (self.credito >= 10):
            self.credito -= 10
            return True
        elif digits[0] == '0' and digits[1] == '0':
            if self.credito >= 100:
                self.credito -= 100
                return True

        else:
            return False
        

    def agregar_credito(self, credit):
        self.credito = credit