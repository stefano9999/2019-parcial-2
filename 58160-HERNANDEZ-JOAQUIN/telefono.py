class Telefono():
    def __init__(self):
        self.credito=0

    def dial (self, num):
 #Ocupo 'startswith' para el metodo de string , que si empieza con 8 la llamada es gratis 
        if len(num) == 3 and (num.startswith('8')) or (num.startswith('9')): 
            return True

        if num.startswith('00') and self.credito > 100: 
            self.credito -= 100 #le resta el credito ocupado en la llamada
            return True
        
        if len(num) == 7 and  self. credito > 10:
            self.credito -= 10 #le resta el credito ocupado en la llamada
            return True
        else:
            return False

    def agregar_credito (self,pagar):
        self.credito += pagar
