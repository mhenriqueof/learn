# Módulos
import emoji
# Fechada
print(emoji.emojize(':two:  Soma de números pares :two:', use_aliases=True))
# Perguntas
print('Salut! Quais números você tem em mente?')
s = 0
cont = 0
for rep in range(0, 6):
    num = int(input(''))
    if num % 2 == 0:
        num = num
        cont += 1
    else:
        num = 0
    s += num
if s > 0:
    print(emoji.emojize(f'A soma dos {cont} números pares escolhidos é {s}! :wink:', use_aliases=True))
else:
    print(emoji.emojize('Você não escolheu nenhum número par. :thinking:', use_aliases=True))
