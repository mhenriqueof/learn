from interface import AveQueVoa, AveQueNaoVoa

class Canario(AveQueVoa):
    
    def comer(self):
        print("Comendo")

    def voar(self):
        print("Voando")

    def gritar(self):
        print('Gritando')

    
class Pinguim(AveQueNaoVoa):
    
    def comer(self):
        print("Comendo")
        self.__acasalar()

    def voar(self):
        None
        
    def gritar(self):
        print("Gritando")
        
    def __acasalar(self):
        print("Acasalando")