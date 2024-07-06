class Loja:
    
    tarifa = 1.03
    
    def __init__(self, localizacao:str) -> None:
        self.__localizacao = localizacao
        
    def apresentar_localizacao(self) -> None:
        print(self.__localizacao)
        
    @classmethod
    def vender(cls) -> int:
        return 40 * cls.tarifa
    
    @classmethod
    def alterar_tarifa(cls, nova_tarifa:int) -> None:
        cls.tarifa = nova_tarifa

loja_praia = Loja('Praia')
loja_centro = Loja('Centro')

print(loja_praia.vender())
print(loja_centro.vender())

loja_centro.alterar_tarifa(5.0)

print(loja_praia.vender())
print(loja_centro.vender())
