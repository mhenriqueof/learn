from abc import ABC, abstractmethod

class AveQueVoa(ABC):
    
    @abstractmethod
    def comer(self):
        raise "Should implement"

    @abstractmethod
    def voar(self):
        raise "Should implement"
    
    @abstractmethod
    def gritar(self):
        raise "Should implement"
        
        
class AveQueNaoVoa(ABC):
    
    @abstractmethod
    def comer(self):
        raise "Should implement"

    @abstractmethod
    def gritar(self):
        raise "Should implement"
