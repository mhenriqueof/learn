    # Área de um terreno #
# Functions
def lin(msg): # Mensagem de início
    print('-' * 25)
    print(msg)
    print('-' * 25)
    
    
def medidas(c, l): # Área do terreno
    print(f'O terreno de {c} x {l} tem {c * l}m².')


# Code
lin(f'{"Área de um Terreno":^25}')
medidas(float(input('Largura do terreno (m): ')), 
        float(input('Comprimento do terreno (m): ')))
