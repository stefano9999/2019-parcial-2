class Telefono(object):
    def __init__(self):
        self.credito=0
    
    def agregar_credito(self,credito_agregado):
        self.credito=credito_agregado
    
    def quitar_credito(self,quitar):
        self.credito-=quitar
    
    def dial(self,numero):
        if len(numero)==3 and (numero[0]=='8') or (numero[0]=='9'):    
            return True
        if len(numero)==7 and self.credito>10:    
            self.quitar_credito(10)
            return True
        if len(numero)==10 and (numero[0:1]=='0') and self.credito>100:
            self.quitar_credito(100)
            return True
        return False

        
        

        
