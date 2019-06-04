#Juan I. Martinez, legajo 57018
class Telefono(object):

    def __init__(self):
        self.numero = []
        self.credito = 0
    
    def dial(self, number):
        for num in number:
            self.numero.append(int(num))        
        if len(number) == 3:
            return self.check_gratis(number)
        elif len(number) == 7:
            return self.check_local(number)
        elif self.numero[0] == 0 and self.numero[1] == 0:
            return self.check_internacional(number)
    
    def agregar_credito(self, coins):
        self.credito += coins

    def check_gratis(self, numero):
        if self.numero[0] == 9 or self.numero[0] == 8:
            self.numero =  []
            return True
        else:
            return False


    def check_local(self, numero):
        if self.credito >= 10:
            self.credito -= 10
            self.numero = []
            return True
        else:
            return False
    
    def check_internacional(self, numero):
        if self.credito >= 100:
            self.credito -= 100
            self.numero = []
            return True
        else:
            return False

