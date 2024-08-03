from produtos import Produto
from typing import Type

class CarrinhoDeCompras:
    
    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto:Type[Produto]):
        self.__produtos.append(produto)
        
    def finalizar_compra(self):
        for produto in self.__produtos:
            produto.informacoes_produto()
            
        self.__produtos = []