from typing import Type

class Animal:
    
    def comer(self):
        print('Comendo')

    def dormir(self):
        print('Dormindo')

    def andar(self):
        print('Andando')


class Aves(Animal):
    
    def __init__(self):
        super().__init__()
        
    def cantar(self):
        print('Ave cantando')


class Pinguim(Aves):
    
    def __init__(self):
        super().__init__()
        
    def escorregar(self):
        print('Pinguim escorregando')

        
class Pessoa:
    
    def observar(self, animal:Type[Animal]):
        animal.comer()

henrique = Pessoa()
pinguim = Animal()
henrique.observar(pinguim)
