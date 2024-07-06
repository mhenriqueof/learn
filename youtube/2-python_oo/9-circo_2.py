class Circo:    
    
    def apresentar(self, apresentador:any):
        apresentador.apresentar_show()


class Malabarista:
    
    def apresentar_show(self):
        print('Apresentação do Malabarista')

class Palhaco:
    
    def apresentar_show(self):
        print('Apresentação do Palhaco')

class Domador:
    
    def apresentar_show(self):
        print('Apresentação do Domador')
        
    
circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()

circo.apresentar(malabarista)
circo.apresentar(palhaco)
circo.apresentar(Domador())
