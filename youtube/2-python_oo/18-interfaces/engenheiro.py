from typing import Type
from interfaces.formas import FormasInterface

class Engenheiro:
    
    def __init__(self, nome:str):
        self.nome = nome
        
    def medir_perimetro(self, terreno:type[FormasInterface]) -> int:
        perimetro = terreno.get_perimetro()
        print(f"{self.nome} mediu o perimetro: {perimetro}")
        
    def medir_area(self, terreno:type[FormasInterface]) -> int:
        area = terreno.get_area()
        print(f"{self.nome} mediu a area: {area} m2")
        