# Módulos
import emoji
# Cores
bbe = '\033[44m'
cc = '\033[m'

# Variáveis
numbers = [[], []]

# Abertura
print(emoji.emojize(f':seven:   {bbe} Sete Valores {cc} :seven:',use_aliases=True))

# Estruturas
for a in range(1,8):
        ask = int(input(f'{a}º número: '))
        if ask % 2 == 0:
            numbers[0].append(ask)
        else:
            numbers[1].append(ask)

# Encerramento
print('-' * 30)
numbers[0].sort()
numbers[1].sort()
print(f'Números pares {numbers[0]}.')
print(f'Números ímpares {numbers[1]}.')
