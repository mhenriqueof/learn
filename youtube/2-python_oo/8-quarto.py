
from typing import Type

class Interruptor:
    
    def __init__(self, comodo:str) -> None:
        self.__comodo = comodo
        
    def acender(self):
        print(f'Acendendo {self.__comodo}')

    def apagar(self):
        print(f'Apagando {self.__comodo}')
        
        
class Pessoa:
    
    def acender_luz(self, interruptor:Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor:Type[Interruptor]):
        interruptor.apagar()
        
    def dormir(self):
        print("Mimindo zZzZzz")
        

henrique = Pessoa()
interruptor_quarto = Interruptor('quarto')
interruptor_cozinha = Interruptor('cozinha')

interruptor_quarto.acender()
henrique.acender_luz(interruptor_cozinha)
henrique.apagar_luz(interruptor_quarto)
henrique.dormir()
