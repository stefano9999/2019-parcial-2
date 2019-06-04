class Telefono:
    def __init__(self):
        self.credito = 0

    def agregar_credito(self,money):
        self.credito += money

    def dial(self,number):
        if len(number) == 3:        #Gratis
            if number[0] == '9' or number[0] == '8':
                return True
        if len(number) == 7:        #Local
            if self.credito >= 10 :
                self.credito -= 10
                return True
            else:
                return False
        if number[0] == '0' and number[1] == '0':
            if self.credito >= 100:
                self.credito -= 100
                return True
            else:
                return False
