# Módulos
import emoji
# Cores
bco = '\033[44m'
bgn = '\033[42m'
brd = '\033[41m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':arrow_backward:  {bco} Menor {cc}:m:  {bgn} Média {cc} :m:  {brd} Maior {cc}:arrow_forward:',use_aliases=True))
# Estruturas
num = ''
soma = quant = 0
lista = []
while num != 0:
    rep = int(input('Número: '))
    if rep == 0:
        break
    lista += [rep]
    soma += rep
    quant += 1
    num = int(input(f'Deseja continuar?\n[0] Não\n[1] Sim\n'))
print(f'Você digitou \033[1m{quant}{cc} números. O {bco} Menor {cc} valor \033[4;34m{min(lista)}{cc}, a {bgn} Média {cc} entres os valores é \033[4;32m{soma / quant:.2f}{cc} e o {brd} Maior {cc} valor é \033[4;31m{max(lista)}{cc}.')
