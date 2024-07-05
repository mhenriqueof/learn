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
frase = input("Qual a frase? ").upper().replace(" ", "")
# Variáveis
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")