class PessoaA:
    
    def se_apresentar(self):
        print('Ola, sou a A')
        
class PessoaB(PessoaA):
    
    def __init__(self) -> None:
        super().__init__()

    def se_apresentar(self):
        print('Alterando metodo.')
        
pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2= PessoaB()
pessoa2.se_apresentar()

pessoa.se_apresentar()
