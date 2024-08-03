from produtos import Produto
from carrinho import CarrinhoDeCompras

car = CarrinhoDeCompras()
monitor = Produto('Monitor', 1000)
suco = Produto('Uva', 10)

car.adicionar_produto(monitor)
car.adicionar_produto(suco)

car.finalizar_compra()
