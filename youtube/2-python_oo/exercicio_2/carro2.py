class Carro:
    
    def __init__(self) -> None:
        self.ligado     = False
        self.cor        = 'Branco'
        self.modelo     = 'Fusion'
        self.velocidade = 0
        
        
    def ligar(self) -> None:
        self.ligado = True
        print("Ligando carro...")
        
    def desligar(self) -> None:
        self.ligado = False
        print("Desligando carro...")
        
    def verificar_ligado_e_ligar(self) -> None:
        if not self.ligado:
            self.ligar()
        else:
            print("O carro já está ligado.")
            
    def verificar_desligado_e_desligar(self) -> None:
        if self.ligado:
            self.desligar()
        else:
            print("O carro já está desligado.")
        
    def liga_desliga(self, liga:bool) -> None:
        if liga:
            self.verificar_ligado_e_ligar()
        else:
            self.verificar_desligado_e_desligar()


# continuar 
    def acelera(self) -> None:
        self.liga_desliga()
        print(f'Velocidade atual {self.velocidade} Km/h. Acelerando até 80 Km/h.')
        self.velocidade = 80
        
    def desacelera(self) -> None:
        print(f"Velocidade atual {self.velocidade} Km/h. Desacelerando até parar.")
        self.velocidade = 0
        self.liga_desliga()
        

car = Carro()

car.liga_desliga(True)
car.liga_desliga(True)
car.liga_desliga(False)
car.liga_desliga(False)
car.liga_desliga(False)
