from abstract import AbstractClass

class Filha(AbstractClass):
    
    def apresentar_metodo(self):
        print(self.atributo)
        
    def metodo_abstrato(self):
        print('Abstração')

        
filha = Filha()
filha.apresentar_metodo()
filha.metodo('Pão')
filha.metodo_abstrato()

# abstractClass = AbstractClass()
# abstractClass.metodo('Céu')
