# Módulos
import emoji
# Cores
rb = '\033[1;30;41m'
bk = '\033[1;30m'
b = '\033[34m'
r = '\033[31m'
w = '\033[1m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':exclamation:{rb} Fatorial {cc} :exclamation:',use_aliases=True))
# Estruturas
n = int(input('Número: '))
c = n
f = 1
while c > 0:
    print(c,end='')
    print(" x" if c > 1 else " =",end=' ')
    f *= c
    c -= 1
print(f)