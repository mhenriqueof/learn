# Módulos
import emoji
# Cores
gn = '\033[1;32m'
ue = '\033[4m'
rd = '\033[1;31m'
we = '\033[1m'
bgy = '\033[1;47m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':capital_abcd: {bgy} Palavras e Vogais {cc} :a:',use_aliases=True))
# Tupla
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO', 'MNB')
# Estruturas
for a in palavras:
    print(f'A palavra {we}{a}{cc} tem as {ue}vogais{cc}:{gn} ',end='')
    cont = 0
    for b in a:
        if b in 'AEIOU':
            print(b.lower(), end=' ')
            cont += 1
    if cont == 0:
        print(f'{rd}não há vogais nesta palavra!')
    cont = 0
    print(cc)
# Encerramento
print(emoji.emojize(f'{we}Espero ter sanado a sua dúvida!{cc} :wink:',use_aliases=True))
