class PessoaA:
    
    def se_apresentar(self):
        print('Ola, sou a A')
        
class PessoaB(PessoaA):
    
    def __init__(self) -> None:
        super().__init__()

    def se_apresentar(self):
        print('Alterando metodo.')
        
class PessoaC(PessoaB):
    
    def __init__(self) -> None:
        super().__init__()
        
pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2= PessoaB()
pessoa2.se_apresentar()

pessoa3 = PessoaC()
pessoa3.se_apresentar()
