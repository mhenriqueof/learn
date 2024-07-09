class Carro:
    
    def __init__(self) -> None:
        self.ligado = False
        self.cor = 'Branco'
        self.modelo = 'Fusion'
        self.velocidade = 0
        

    def ligar(self) -> None:
        self.verificar_ligado_e_ligar()
        
    def verificar_ligado_e_ligar(self) -> None:
        if not self.ligado:
            self.liga_carro()
        else:
            print("O carro já está ligado.")
            
    def liga_carro(self) -> None:
        self.ligado = True
        print("Ligando carro...")
            
    def desligar(self) -> None:
        self.verificar_desligado_e_desligar()
            
    def verificar_desligado_e_desligar(self) -> None:
        if self.ligado:
            self.desliga_carro()
        else:
            print("O carro já está desligado.")
        
    def desliga_carro(self) -> None:
        self.ligado = False
        print("Desligando carro...")
        
    
# TODO continuar 
    def acelera(self) -> None:
        self.liga_desliga()
        print(f'Velocidade atual {self.velocidade} Km/h. Acelerando até 80 Km/h.')
        self.velocidade = 80
        
    def desacelera(self) -> None:
        print(f"Velocidade atual {self.velocidade} Km/h. Desacelerando até parar.")
        self.velocidade = 0
        self.liga_desliga()
        

car = Carro()

car.ligar()
car.ligar()
car.desligar()
car.desligar()
car.desligar()
car.ligar()
