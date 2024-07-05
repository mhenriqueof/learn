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
n = int(input('Fatorial do número: '))
a = 0
f = 1
for a in range(n, 0, -1):
    print(a, end='')
    print(" x " if a > 1 else " = ",end='')
    f *= n
    n -= 1
print(f)