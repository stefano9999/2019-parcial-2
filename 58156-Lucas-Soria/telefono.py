class Telefono:

    def __init__(self):
        self.llamada_ok = False
        self.credito = 0
    
    def agregar_credito(self,credito):
        self.credito += credito
    
    def dial(self, nume):
        if len(nume) == 3:
            if (nume[0] == '9' or nume[0] == '8'):
                return True
            else:
                return False
        
        if len(nume) == 7:
            if self.credito < 10:
                return False
            else:
                self.credito -= 10
                return True
        
        if nume[0:2] == '00':
            if self.credito < 100:
                return False
            else:
                self.credito -= 100
                return True



