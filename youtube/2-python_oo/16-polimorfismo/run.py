from typing import Dict
from models import Insersor, Repositorio

class RepositorioFake(Repositorio):

    def __init__(self) -> None:
        super().__init__()
        
    def select(self, nome:str) -> Dict:
        return None

repo = RepositorioFake()
insersor = Insersor(repo)

data = insersor.inserir_dado('Henrique', 23)
data2 = insersor.inserir_dado('Henrique', 23)
print(data)
