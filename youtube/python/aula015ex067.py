# Módulos
import emoji
# Cores
bbg = '\033[1;30;44m'
rd = '\033[1;31m'
be = '\033[1;34m'
bk = '\033[30m'
gn = '\033[1;32m'
we = '\033[1m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':heavy_multiplication_x:   {bbg} Tabuada {cc} :heavy_multiplication_x:',use_aliases=True))
# Estruturas
print(f'Digite um {rd}NÚMERO NEGATIVO{cc} para {rd}PARAR{cc}')
cont = n = s = 0
while True:
    n = int(input(f'Você quer saber a {we}tabuada de qual número?{cc} '))
    if n < 0:
        break
    while cont != 10:
        cont += 1
        s = cont * n
        print(f'{be}{n}{cc} {bk}x{cc}{" " if cont == 10 else "  "}{be}{cont}{cc} {bk}={cc} {gn}{s}{cc}')
    cont = 0
# Encerramento
print(emoji.emojize(f'\033[4mVolte sempre!{cc}:grinning:',use_aliases=True))
