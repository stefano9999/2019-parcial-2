


class Telefono():
    def __init__(self):
        self.credito = 0

    def agregar_credito(self, credito):
        self.credito += credito

    def dial(self, num):
        if num[0] == "0" and num[1] == "0":
            llamada = self.internacional(num)
            return llamada 
        elif len(num) == 3:
            llamada = self.gratis(num)
            return llamada
        elif len(num) == 7:
            llamada = self.local(num)
            return llamada
        

    def gratis(self, num):
        if num[0] == "9" or num[0] == "8":
            return True
        else:
            return False

    def local(self, num):
        if self.credito >= 10:
            self.credito -= 10
            return True
        else:
            return False

    def internacional(self, num):
        if self.credito >= 100:
            self.credito -= 100
            return True
        else:
            return False
