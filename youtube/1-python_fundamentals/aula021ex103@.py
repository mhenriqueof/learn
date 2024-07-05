    # Ficha do jogador #
# Functions
def ficha():
    name = input('Nome do jogador: ').lower().capitalize()
    goals = input('Gols feitos: ')
    if goals == '':
        goals = int(47)
    if name.strip() == '':
        name = 'Joriscleiton'
    return f'O jogador {name} fez {goals} gols.'
    
# Code
print(ficha())
