# Módulos
import emoji
# Cores
be = '\033[1;34m'
we = '\033[1m'
gn = '\033[32m'
rd = '\033[31m'
yw = '\033[33m'
bgn = '\033[42m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':chart: {bgn} Valores Numéricos {cc} :chart:',use_aliases=True))
# Estruturas
print(f'{yw}Digite {rd}0{yw} para parar.{cc}') # Stop
lista = []
while True:
    num = int(input(f'{cc}{we}Número:{gn} '))
    if num == 0:
        print(cc,end='')
        break
    else:
        if num in lista:
            print(cc,end='')     
        else:
            lista.append(num)
lista.sort()
# Encerramento
print(f'{we}Os números em ordem crescente são{cc}: ',end='')
print(be,end='')
print(*lista, sep = f' {cc}{we}|{cc}{be} ',end='')
print(emoji.emojize(f'{cc} :wink:',use_aliases=True))
