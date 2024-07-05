# Módulos
import emoji
from time import sleep
# Cores
fundo = '\033[7m'
bk = '\033[1;30m'
b = '\033[1;34m'
g = '\033[1;32m'
c = '\033[1;36m'
r = '\033[1;31m'
w = '\033[1;97m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':heavy_plus_sign: {fundo}Operações com 2 valores{cc} :heavy_multiplication_x:',use_aliases=True))
# Perguntas
x = float(input('x: '))
y = float(input('y: '))
xy = [x, y]
print(xy)
menu = ''
# Estruturas
while menu != 5:
    menu = int(input(emoji.emojize(f'O que você deseja fazer com os valores {w}{x}{cc} e {w}{y}{cc}?\n{c}[1] Somar :heavy_plus_sign:{cc}\n{b}[2] Multiplicar :heavy_multiplication_x:{cc}\n{r}[3] Maior :arrow_forward:{cc}\n{g}[4] Outros valores :grey_question:{cc}\n{bk}[5] Sair :door:{cc}\n',use_aliases=True)))
    sleep(.5)
    if menu == 1:
        print(f'A {c}Soma{cc} entre eles é {w}{x + y}{cc}.')
    elif menu == 2:
        print(f'A {b}Multiplicação{cc} entre eles é {w}{x * y}{cc}.')
    elif menu == 3:
        print(f'O {r}maior{cc} número é {w}{max(xy)}{cc}.')
    elif menu == 4:
        x = float(input(f'{g}x:{cc} '))
        y = float(input(f'{g}y:{cc} '))
    elif menu == 5:
        print(emoji.emojize(f'{bk}Volte sempre!{cc}:grin:',use_aliases=True))
    else:
        print('Opção inválida!')
    sleep(3)
    