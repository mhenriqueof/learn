# Módulos
import emoji
import random
# Cores
bbe = '\033[44m'
be = '\033[1;34m'
ue = '\033[4m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':repeat: {bbe} Números Aleatórios {cc} :repeat:',use_aliases=True))
# Números
numeros = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
print(numeros)
# Maior e menor
print(f'O {ue}menor{cc} valor é o {be}{min(numeros)}{cc} e o {ue}maior{cc} é o {be}{max(numeros)}{cc}.')
