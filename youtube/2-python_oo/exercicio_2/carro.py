class Carro:
    
    def __init__(self) -> None:
        self.ligado = False
        self.cor = 'Branco'
        self.modelo = 'Fusion'
        self.velocidade = 0
        self.velocidade_minima = 0
        self.velocidade_maxima = 300
        

    def ligar(self) -> None:
        self.verificar_ligado_e_ligar()
        
    def verificar_ligado_e_ligar(self) -> None:
        if not self.ligado:
            self.liga_carro()
        else:
            print("O carro já está ligado.")
            
    def liga_carro(self) -> None:
        self.ligado = True
        print("O carro foi ligado.")
            
    def desligar(self) -> None:
        self.verificar_desligado_e_desligar()
            
    def verificar_desligado_e_desligar(self) -> None:
        if self.ligado:
            self.desliga_carro()
        else:
            print("O carro já está desligado.")
        
    def desliga_carro(self) -> None:
        self.ligado = False
        print("O carro foi desligado.")
        
    
    def acelerar(self) -> None:
        self.verificar_velocidade_e_acelerar()        
        
    def verificar_velocidade_e_acelerar(self):
        if self.velocidade < self.velocidade_maxima:
            self.acelera_carro()
        else:
            print(f"Velocidade máxima de {self.velocidade_maxima} Km/h já atingida.")
    
    def acelera_carro(self):
        self.velocidade += 100
        print(f'Acelerando 10 Km/h. Velocidade atual: {self.velocidade}')
        
    def desacelerar(self) -> None:
        self.verificar_velocidade_e_desacelerar()        
        
    def verificar_velocidade_e_desacelerar(self):
        if self.velocidade > self.velocidade_minima:
            self.desacelera_carro()
        else:
            print(f"Velocidade mínima de {self.velocidade_minima} Km/h já atingida.")
    
    def desacelera_carro(self):
        self.velocidade -= 10
        print(f'Descelerando 10 Km/h. Velocidade atual: {self.velocidade}')
        

car = Carro()

car.ligar()
car.acelerar()
car.acelerar()
car.acelerar()
car.acelerar()
