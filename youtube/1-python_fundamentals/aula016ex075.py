# Módulos
import emoji
# Cores
gn = '\033[32m'
rd = '\033[31m'
bgn = '\033[42m'
we = '\033[1m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':four_leaf_clover: {bgn} Quatro Valores {cc} :four_leaf_clover:',use_aliases=True))
# Números
num = tuple(int(input(f'{"Primeiro" if c == 1 else "Outro"} valor: '))for c in range(1,5))
# Vezes do 9
nove = num.count(9)
if nove == 0:
    print(f'O número {we}9{cc} {rd}não apareceu nenhuma vez{cc}.')
elif nove == 1:
    print(f'O número {we}9{cc} {gn}apareceu uma vez{cc}.')
else:
    print(f'O número {we}9{cc} {gn}apareceu {nove} vezes{cc}.')
# Posição do 3
if 3 in num:
    print(f'O número {we}3{cc} está na posição {gn}{num.index(3) + 1}{cc} da tupla.')
else:
    print(f'O número {we}3{cc} {rd}não aparece{cc} na tupla.')
# Números pares
print(f'Os {we}números pares{cc} são:{gn} ',end='')
cont = 0
for n in num:
    if n % 2 == 0:
        cont += 1
        print(n, end=' ')
    else:
        continue
if cont == 0:
    print(f'{rd}não há número pares{cc}.')
else:
    print(cc)
# Encerramento
