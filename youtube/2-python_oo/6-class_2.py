class MinhaClasse:
    
    estatico = 'Henrique' # variável de classe / variável estática / variável global
    
    def __init__(self, estado=True) -> None:
        self.estado = estado
    
    def print_estatico(self) -> None:
        print(self.estatico)
        
    @classmethod
    def mudar_estatico(cls) -> None:
        cls.estatico = 'Oliveira'
        

objeto_1 = MinhaClasse()
objeto_2 = MinhaClasse()

objeto_1.mudar_estatico()

objeto_1.print_estatico()
objeto_2.print_estatico()
