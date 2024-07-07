class Carro:
    
    def __init__(self) -> None:
        self.ligado     = False
        self.cor        = 'Branco'
        self.modelo     = 'Fusion'
        self.velocidade = 0
        
        
    def ligar(self):
        self.ligado = True
        print("Ligando carro...")
        
    def desligar(self):
        self.ligado = False
        print("Desligando carro...")
        
    def verificar_ligado(self):
        if not self.ligado:
            self.ligar()
        else:
            print("O carro já está ligado.")
            
    def verificar_desligado(self):
        if self.ligado:
            self.desligar()
        else:
            print("O carro já está desligado.")
        
    def liga(self) -> None:
        self.verificar_ligado()

    def desliga(self) -> None:
        self.verificar_desligado()

    def acelera(self) -> None:
        self.liga()
        print(f'Velocidade atual {self.velocidade} Km/h. Acelerando até 80 Km/h.')
        self.velocidade = 80
        
    def desacelera(self) -> None:
        print(f"Velocidade atual {self.velocidade} Km/h. Desacelerando até parar.")
        self.velocidade = 0
        self.desliga()
        

car = Carro()

car.liga()
car.liga()
car.desliga()
car.desliga()
car.desliga()
