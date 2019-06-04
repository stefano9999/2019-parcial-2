class Telefono(object):

    def __init__(self):
        self.credito=0

    def agregar_credito(self,dinero):
        self.credito+=dinero

    def dial(self,numero):
        if len(numero)==3:
            if numero[0]=='8' or numero[0]=='9':
                return (True)

        if len(numero)==7:
            try:
                if self.credito>=30:
                    self.credito-=10
                    return(True)
            except:
                return(False)

        if len(numero)==10:
            if numero[0]=='0' and numero[1]=='0':
                
                try:
                    if self.credito>=100:
                        self.credito-=100
                        return True
                except:
                        return False

                
                




