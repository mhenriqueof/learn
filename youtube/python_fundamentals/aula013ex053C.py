# Módulos
import emoji
# Cores
r = '\033[1;31m'
g = '\033[1;32m'
w = '\033[1;97m'
cc = '\033[m'
# Abertura
print(emoji.emojize(':repeat_one: Detector de \033[4mPalíndromos\033[m :repeat_one:', use_aliases=True))
# Perguntas
frase = str(input('Digite a frase: ')).strip().upper()
# Variáveis
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
# Condições
print(f'O inverso de {w}{junto}{cc} é {w}{inverso}{cc}.', end=' ')
if junto == inverso:
    print(f'A frase {g}é um palíndromo{cc}.')
else:
    print(f'A frase {r}não é um palíndromo{cc}.')
