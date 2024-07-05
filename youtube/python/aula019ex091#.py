    # 4 Jogadores, 1 Dado #
# Modules
from random import randint
from time import sleep
# Variables
ficha = ()
lances = {'jogador 1': randint(1,6),
          'jogador 2': randint(1,6),
          'jogador 3': randint(1,6),
          'jogador 4': randint(1,6),}
    # Code #
for k, v in lances.items(): # Jogador e Dado
    print(f'O {k} tirou {v} no dado.')
ficha = sorted(lances.items(), key=lambda item: item[1], reverse=True)
    # Encerramento)
print('-' * 50)
sleep(1)
for a, b in enumerate(ficha): # Vencedores
    print(f'O {b[0]} ficou na {a+1}ª posição. Sorteou {b[1]}.')
    sleep(1)
    