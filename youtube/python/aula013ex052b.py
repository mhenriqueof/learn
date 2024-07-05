# Módulos
import emoji
r = "\033[m\033[31m"
# Abertura
print(emoji.emojize(':two: :three:  Números primos :three: :two: ', use_aliases=True))
# Perguntas
num = int(input('Digite um número inteiro: '))
count = 0
# Repetições
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;32m', end=' ')
        count += 1
    else:
        print('\033[1;30m', end=' ')
    print(f'{c}\033[m', end=' ')
print(f'\nO número \033[1m{num}\033[m foi dividido \033[1;34m{f"{r}" if count > 2 else ""}{count} vezes\033[m.', end=' ')
if count == 2:
    print(f'Ele \033[32mé primo\033[m.')
else:
    print(f'Ele \033[31mnão é primo\033[m.')
    