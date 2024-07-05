# Módulos
import emoji
# Cores
bbe = '\033[44m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':five:  {bbe} Valores {cc}:five:',use_aliases=True))
# Estruturas
lista = []
for f in range(0,5):
    num = int(input('Número: '))
    if f == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Número adicionado na posição {lista.index(num)}.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Número adicionado na posição {lista.index(num)}.')
                break
            pos += 1
print(emoji.emojize(f'A lista em ordem é {lista}. :wink:',use_aliases=True))
print()