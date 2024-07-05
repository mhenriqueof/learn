    # Jogador de Futebol #
# Variables
dados = {}
gols = 0
    # Code #
dados['Nome'] = str(input(f'Nome do jogador: ')).lower().capitalize()
dados['Partidas'] = int(input('Partidas jogadas: '))
for a in range(0, dados['Partidas']):
    dados[f'GolsPartida{a+1}'] = int(input(f'Gols na {a+1}ª partida: '))
    # Encerramento #
print('-' * 25)
for b, c in dados.items(): # Nome, Partidas e Gols
    print(f'{b}: {c}')
for d in range(0, dados['Partidas']): # Total Gols
    gols += dados[f'GolsPartida{d+1}']
print(f'Total de gols: {gols}')
