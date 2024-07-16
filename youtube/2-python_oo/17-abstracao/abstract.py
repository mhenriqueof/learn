from abc import ABC, abstractmethod

class AbstractClass(ABC):
    
    # def __init__(self) -> None:
    #     self.atributo = 'Olá'

    # def metodo(self, elemento:str):
    #     print(elemento)
    
    @abstractmethod
    def metodo_abstrato(self):
        pass
