from interfaces.formas import FormasInterface

class TerrenoRetangular(FormasInterface):
    
    def __init__(self, largura:int, comprimento:int):
        self.largura = largura
        self.comprimento = comprimento
        
    def get_perimetro(self) -> int:
        perimetro = (self.largura * 2) + (self.comprimento * 2)
        return perimetro
    
    def get_area(self) -> int:
        area = self.largura * self.comprimento
        return area
    