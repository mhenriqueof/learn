    # Jogador de Futebol #
# Modules
from time import sleep
# Variables
jogadores = list()
dados = {}
gols = []
# Code
while True: # Perguntar dados
    dados.clear()
    gols.clear()
    dados['Nome'] = str(input(f'Nome do jogador: ')).lower().capitalize()
    partidas = int(input('Partidas jogadas: '))
    for a in range(0, partidas):
         gol = int(input(f'Gols na {a+1}ª partida: '))
         gols += [gol]
         dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    # Finalizar dados
    jogadores.append(dados.copy())
    while True: # Continuar?
        ask = str(input(f'Deseja adicionar mais jogadores? SIM ou NÃO ')).lower()
        if ask[0] in 'sn':
            break
        print('Digite SIM ou NÃO')
    if ask[0] in 'n':
        break
# Encerramento
print('-' * 50)
print('Nº ', end='')
for i in dados.keys():
    print(f'{i:^15}', end='')
print()
for k, b in enumerate(jogadores): # Mostrar tabela dos jogadores
    print(f'{k} ', end='')
    for d in b.values():
        print(f'{str(d):^15}', end='')
    print()
print('-' * 50)
while True: # Performance individual
    player = int(input("Mostrar performance de qual jogador? [Digite o número do jogador] (999 para sair) "))
    if player < len(jogadores):
        print('-' * 50)
        print(f'Performance de {jogadores[player]["Nome"]}:')
        ponto = jogadores[player]["Gols"]
        for f, c in enumerate(jogadores[player]["Gols"]):
            print(f'No jogo {f+1}: {c} gols.')
        print('-' * 50)
    elif player == 999:
        print('Finalizando o programa...')
        sleep(1)
        break
    else:
        print(f'Jogador {player} não existe na lista!')
        