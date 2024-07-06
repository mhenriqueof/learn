class MinhaClasse:
    
    def __init__(self, estado) -> None:
        self.estado = estado

    @staticmethod
    def metodo_estatico() -> None:
        print('Estou aqui')
        

objeto = MinhaClasse(True)
objeto.metodo_estatico()
MinhaClasse.metodo_estatico()