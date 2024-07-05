# Módulos
import emoji
# Cores
bgy = '\033[30;47m'
be = '\033[1;34m'
gn = '\033[1;32m'
we = '\033[1m'
rd = '\033[31m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':heavy_plus_sign: {bgy} Soma de Números {cc} :heavy_plus_sign:',use_aliases=True))
# Estruturas
num = soma = xnums = 0
print(f'[Digite {rd}999{cc} para {rd}parar{cc}]')
num = int(input(f'{cc}Número:{we} '))
while num != 999:
    soma += num
    xnums += 1
    num = int(input(f'{cc}Número:{we} '))
# Encerramento
print(f'{cc}A {be}quantidade de números{cc} digitados foi {be}{xnums}{cc} e a {gn}soma{cc} entre eles é {gn}{soma}{cc}.')
