

class Telefono :

    def __init__ (self) :
        self.credito = 0

    def agregar_credito(self,credito):
        self.credito += credito

    def quitar_credito(self,restar):
        self.credito -=restar


    def llamada_gratis(self,numero):
        self.numero = int(numero)

        if self.numero <1000 and self.numero >799:  #para que empize con 8 o 9 debe estar entre estos numeros
            
            return True
        else:
            return False


    def llamada_local(self):
        
        if self.credito < 10 :
            return False
        else:
            self.quitar_credito(10)
            return True

    def llamada_internacional(self):
        if self.credito < 100 :
            return False
        else:
            self.quitar_credito(100)
            return True




    def dial(self,numero):
        
        if numero[0:2] == '00':
            self.llamada = self.llamada_internacional()
            return self.llamada


        if len (numero) == 3:
           self.llamada = self.llamada_gratis(numero)
           return self.llamada

        if len (numero) == 7:
            self.llamada = self.llamada_local()
            return self.llamada

        else:
            print('Numero no valido')
            return False

        



