class MinhaClasse:
    
    estatico = 'Henrique' # variável de classe / variável estática / variável global
    
    def __init__(self, estado) -> None:
        self.estado = estado
        

objeto_1 = MinhaClasse(True)
objeto_2 = MinhaClasse(False)

MinhaClasse.estatico = 'Oliveira'
objeto_1.estatico = 'Henrique'

print(objeto_1.estatico)
print(objeto_2.estatico)
print(MinhaClasse.estatico)
