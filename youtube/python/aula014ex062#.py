# Módulos
import emoji
# Cores
bbe = '\033[44m'
bk = '\033[30m'
be = '\033[1;34m'
we = '\033[1m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':zero: :five:   {bbe} Progressão Aritmética {cc}  :five: :keycap_ten:',use_aliases=True))
# Perguntas
termo1 = int(input(f'{be}Termo: {cc}'))
razao1 = int(input(f'{we}Razão: {cc}'))
termo = termo1
contador = 1
total = 0
mais = 10
# Estruturas
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} | ',end='')
        termo += razao1
        contador += 1
    mais = int(input('\nQuanto termos a mais? '))
print(f'Houve {total} termos.')
       