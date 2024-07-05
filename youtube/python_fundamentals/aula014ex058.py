# Módulos
import emoji
import random
from time import sleep
# Cores
w = '\033[1m'
r = '\033[31m'
rd = '\033[1;31m'
g = '\033[32m'
b = '\033[1;34m'
fy = '\033[30;43m'
cc = '\033[m'
# Emojis
hapmojis = [':joy:', ':laughing:', ':smile:', ':blush:', ':stuck_out_tongue_winking_eye:', ':stuck_out_tongue_closed_eyes:', ':hand_over_mouth:']
sadmojis = [':neutral_face:', ':zipper_mouth_face:', ':raised_eyebrow:', ':expressionless:', ':unamused:', ':pensive:']
# Abertura
print(emoji.emojize(f':see_no_evil: {fy} Jogo da Adivinhação {cc} :see_no_evil:',use_aliases=True))
# Kalista
numkali = int(random.randint(0,10))
adivinha = ''
erros = 0
# Estruturas
while numkali != adivinha:
    adivinha = int(input(emoji.emojize('Qual número eu estou pensando? ',use_aliases=True)))
    sleep(.5)
    print('Acho que você...')
    sleep(1.5)
    if adivinha != numkali:
        print(emoji.emojize(f'{r}Errou!!{cc}{random.choice(hapmojis)} É um número {f"{rd}maior{cc}" if numkali > adivinha else f"{b}menor{cc}"}!',use_aliases=True))
    else:
        print('Hum...')
        sleep(1.5)
        print(emoji.emojize(f'{g}Acertou...{cc} {random.choice(sadmojis)}',use_aliases=True))
    erros += 1  
# Despedida
sleep(1)   
print(emoji.emojize(f'Você tentou {w}{erros}{cc} {"vez" if erros == 1 else "vezes"}. {w}Obrigada por jogar comigo!{cc}:grin:',use_aliases=True))
