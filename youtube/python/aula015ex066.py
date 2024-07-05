# Módulos
import emoji
# Cores
rd = '\033[1;31m'
be = '\033[1;34m'
gn = '\033[1;32m'
we = '\033[1m'
cc = '\033[m'
# Abertura
print(emoji.emojize(':heavy_plus_sign: Soma de Números :heavy_plus_sign:',use_aliases=True))
# Estruturas
print(f'Digite [{rd}999{cc}] para {rd}PARAR{cc}')
n = s = c = 0
while True:
    n = int(input(f'{cc}Número:{we} '))
    if n == 999:
        break
    s += n
    c += 1
# Encerramento
print(emoji.emojize(f'O {be}Total de Números{cc} digitados foi {be}{c}{cc} e a {gn}Soma{cc} entre eles é {gn}{s}{cc}. :wink:',use_aliases=True))
