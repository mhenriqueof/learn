from typing import Type
from db.interface import Repositorio
from db.mongo_repository import MongoRepositorio
from db.mysql_repository import MySqlRepositorio

class Usuario:
    
    def __init__(self, repositorio:Type[Repositorio]):
        self.__repositorio = repositorio
        
    def armazenar_dado(self, dado:any):
        self.__repositorio.inserir(dado)
        
    def remover_dado(self, dado:any):
        self.__repositorio.deletar(dado)
        

usuario = Usuario(MySqlRepositorio())
usuario.armazenar_dado(23)

usuario2 = Usuario(MongoRepositorio())
usuario2.armazenar_dado(6)
