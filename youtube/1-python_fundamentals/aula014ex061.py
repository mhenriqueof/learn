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
termo = int(input(f'{be}Termo: {cc}'))
razao = int(input(f'{we}Razão: {cc}'))
dez = -1
lista = []
# Estruturas
while dez != 9:
    dez += 1
    if dez % 2 == 0:
        fundo = '\033[1;34m'
    else:
        fundo = '\033[1m'
    nums = termo + (razao * dez)
    n = str(f'{fundo}{nums}{cc}')
    lista += [n]
print(f' {bk}|{cc} '.join(lista))
