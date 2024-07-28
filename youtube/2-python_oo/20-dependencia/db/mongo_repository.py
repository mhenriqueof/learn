from .interface import Repositorio

class MongoRepositorio(Repositorio):
    
    def inserir(self, dado):
        print(f'Inserindo {dado} no Mongo')

    def deletar(self, dado):
        print(f'Deletando {dado} no Mongo')
        