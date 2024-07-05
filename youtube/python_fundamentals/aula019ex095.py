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
print(f'Nº | {"NOME":^10} | {"GOLS":^15} | {"TOTAL":<4}')
for k, b in enumerate(jogadores): # Mostrar tabela dos jogadores
    print(f'{k}  | {jogadores[k]["Nome"]:^10} | {str(jogadores[k]["Gols"]):^15} | {sum(jogadores[k]["Gols"])}')
print('-' * 50)
while True: # Performance individual
    player = int(input("Mostrar performance de qual jogador? [Digite o número do jogador] (999 para sair) "))
    if player < len(jogadores):
        print('-' * 50)
        print(f'Performance de {jogadores[player]["Nome"]}:')
        ponto = jogadores[player]["Gols"]
        for c in range(0, len(jogadores[player]["Gols"])):
            print(f'No jogo {c+1}: {ponto[c]} gols.')
        print('-' * 50)
    elif player == 999:
        print('Finalizando o programa...')
        sleep(1)
        break
    else:
        print(f'Jogador {player} não existe na lista!')
        