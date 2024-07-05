    # Palpites Mega Sena #
jogos = []
numbers = []
cont = 0
# Módulos
from random import randint
    # Estruturas #
# Quantos jogos?
ask = int(input(f'Quantos jogos desejados? '))
# Gerar palpites
for quantidade in range(0,ask):
    while True:
        num = randint(1,60)
        if num not in numbers:
            numbers.append(num)
            cont +=1
        if cont == 6:
            cont = 0
            break
    numbers.sort()
    jogos.append(numbers[:])
    numbers.clear()
print('-' * 35)
    # Encerramento #
for a in range(0,ask):
    print(f'{a+1}º jogo: {jogos[a]}')
