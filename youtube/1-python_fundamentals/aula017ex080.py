# Módulos
import emoji
# Cores
bbe = '\033[44m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':five:  {bbe} Valores {cc}:five:',use_aliases=True))
# Estruturas
lista = []
menor = maior = ultimo = 0
for f in range(0,5):
    num = int(input('Número: '))
    if f == 0:
        menor = num
        maior = num
        lista.append(num)
    if f > 0:
        if num >= maior:
            lista.append(num)
            maior = num
        elif num <= menor:
            menor = num
            lista.insert(0, num)
        else:
            if num >= ultimo:
                lista.insert(4, num)
            elif num <= ultimo:
                lista.insert(1, num)
    ultimo = num
print(lista)
#
#
#