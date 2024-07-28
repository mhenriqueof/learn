from .interface import Repositorio

class MySqlRepositorio(Repositorio):
    
    def inserir(self, dado):
        print(f'Inserindo {dado} no MySQL')

    def deletar(self, dado):
        print(f'Deletando {dado} no MySQL')
        