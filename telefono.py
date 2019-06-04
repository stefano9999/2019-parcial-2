class Telefono():
    
    def __init__(self):
        self.credito = 0

    def dial(self, numero):
        if len(numero) == 3:
            if numero[0] == '8' or numero[0] == '9':
                llamada_ok = True
                return llamada_ok
            else:
                llamada_ok = False
                return llamada_ok

        if len(numero) == 7:
            if self.credito > 10:
                llamada_ok = True
                self.credito -= 10
                return llamada_ok
            else:
                llamada_ok = False
                return llamada_ok

        if numero[0] == '0' and numero[1] == '0':
            if self.credito > 100:
                llamada_ok = True
                self.credito -= 100
                return llamada_ok
            else:
                llamada_ok = False
                return llamada_ok

    def agregar_credito(self, cred):
        self.credito += cred
