# Módulos
import emoji
# Cores
rd = '\033[31m'
gn = '\033[32m'
we = '\033[1m'
ue = '\033[4m'
bbe = '\033[44m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':zero:  {bbe} Vários Números {cc}:nine: :nine:',use_aliases=True))
# Estruturas
counter = 1
lista = []
while True:
    number = int(input(f'{counter}º valor: '))
    lista += [number]
    counter += 1
    while True:
        ask = int(input(f'Deseja continuar? {rd}0 para NÃO{cc} | {gn}1 para SIM{cc} '))
        if ask == 0 or ask == 1:
            break
    if ask == 0:
        break
# Encerramento
lista.sort(reverse=True)
print(f'{ue}Lista{cc} em {we}ordem decrescente{cc}: {we}{lista}{cc}')
print(emoji.emojize(f'{f"Foi contado apenas {we}1 número{cc}" if counter == 2 else f"Foram contados {we}{counter - 1} números{cc}"}{f" e o {gn}número 5 foi encontrado{cc}." if 5 in lista else f", porém o {rd}número 5 não foi encontrado{cc}."}'))
