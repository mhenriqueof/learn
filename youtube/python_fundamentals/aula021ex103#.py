    # Ficha do jogador #
# Functions
def ficha(nome = 'Joriscleiton', gols = 1):
    print(f'O jogador {nome} fez {gols} gols.')
    

# Code
name = str(input('Nome do jogador: '))
goals = str(input('Gols feitos: '))
if goals.isnumeric():
    goals = int(goals)
else: 
    goals = 0
if name.strip() == '':
    ficha(gols = goals)
else:
    ficha(name, goals)
    