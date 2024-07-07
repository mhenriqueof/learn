class Mae:
    
    def __init__(self, endereco:str) -> None:
        self.endereco = endereco
        self.sobrenome = 'Silva'

    def comer(self) -> str:
        return 'Comendo...'
    
    def estudar(self) -> str:
        return "Estudando..."


class Filha(Mae):
    
    def __init__(self, endereco) -> None:
        super().__init__(endereco)
        
    def brincar(self, brinquedo:str) -> None:
        print(f"Brincando com {brinquedo}")
        

class Neta(Filha):
    
    def __init__(self, endereco) -> None:
        super().__init__(endereco)
    
        
tereza = Mae('Rua da mae')
gislaine = Filha('Rua da filha')
leandra = Neta('Rua')

gislaine.brincar('martelo')

print(tereza.endereco)
print(gislaine.endereco)
print(leandra.endereco)
print(tereza.comer())
print(leandra.estudar())
