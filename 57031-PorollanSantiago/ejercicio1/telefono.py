class Telefono:
    def __init__(self):
        self.credito = 0

    def dial(self, numero):
        if len(numero) == 3: 
            return self.llamada_3_digitos(numero)
        elif len(numero) == 7:
            return self.llamada_local(numero)
        elif numero[0] == '0' and numero[1] == '0':
            return self.llamada_internacional(numero)
    def agregar_credito(self, credito):
        self.credito += credito

    def llamada_3_digitos(self, numero):
        if numero[0] == '9' or numero[0] == '8':
            return True
        else:
            return False
    
    def llamada_local(self, numero):
        if self.credito > 10:
            self.credito -= 10
            return True
        else:
            return False       
        
    def llamada_internacional(self, numero):
        if self.credito > 100:
            self.credito -= 100
            return True
        else:
            return False
