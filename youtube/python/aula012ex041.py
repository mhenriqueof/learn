# Módulos
import emoji
from datetime import date
year = date.today().year
from time import sleep
# Cores
c = '\033[1;36m'
b = '\033[1;34m'
g = '\033[1;32m'
y = '\033[1;33m'
r = '\033[1;31m'
cc = '\033[m'
# Fachada
print(emoji.emojize(':swimmer: \033[44mConfederação Nacional de Natação\033[m :swimmer:', use_aliases=True))
# Perguntas
sleep(.5)
nasci = int(input('Qual é o ano do seu nascimento?\n'))
# Condições
idade = year - nasci
if idade <= 9:
    print(f'Sua categoria é {c}MIRIM{cc}.')
elif idade <= 14:
    print(f'Sua categoria é {b}INFANTIL{cc}.')
elif idade <= 19:
    print(f'Sua categoria é {g}JUNIOR{cc}.')
elif idade <= 20:
    print(f'Sua categoria é {y}SÊNIOR{cc}.')
elif idade >= 25:
    print(f'Sua categoria é {r}MASTER{cc}.')
else:
    print('Por favor, digite um ano válido.')
print(f'A sua idade é de {idade}.')
print(emoji.emojize('Acesse o \033[1msite\033[m da \033[44mConfederação Nacional de Natação\033[m para mais :question:informações:question:.', use_aliases=True))
