# Módulos
import emoji
from math import factorial
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
x = int(input('Número: '))
fat = factorial(x)
print(emoji.emojize(f'{r}{x}:exclamation:{cc}=',use_aliases=True),end='')
while x != 1:
    print(f' {w}{x}{cc} {b}x{cc}',end='')
    x += -1
print(f' {w}1{cc} = {rb} {fat} {cc}')
