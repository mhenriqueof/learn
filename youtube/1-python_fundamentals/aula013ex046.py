# Módulos
import emoji
from time import sleep
# Emojis
diabri = ':sparkler::sparkles:'
bridia = ':sparkler::sparkles:'
firew = ':fireworks::sparkler::firecracker::sparkles:'
# Cores
cc = '\033[m'
# Abertura
print(emoji.emojize(f'\033[30;43m{diabri * 3}  Contagem regressiva para o Ano Novo  {bridia * 3}{cc}', use_aliases=True))
# Repetições
for cont in range(10 , 0, -1):
    print(cont)
    sleep(1)
print(emoji.emojize(f'\033[41m{firew * 2}  Feliz Ano Novo!!  {firew * 2}{cc}', use_aliases=True))
