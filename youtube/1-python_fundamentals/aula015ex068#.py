# Módulos
import emoji
import random
from time import sleep
# Cores
byw = '\033[30;43m'
yw = '\033[1;33m'
co = '\033[1;36m'
gn = '\033[32m'
rd = '\033[31m'
we = '\033[1m'
cc = '\033[m'
# Emojis
hapmojis = [':joy:', ':laughing:', ':smile:', ':blush:', ':stuck_out_tongue_winking_eye:', ':stuck_out_tongue_closed_eyes:', ':hand_over_mouth:']
sadmojis = [':neutral_face:', ':zipper_mouth_face:', ':raised_eyebrow:', ':expressionless:', ':unamused:', ':pensive:']
# Abertura
print(emoji.emojize(f':fist: {byw} Jogo do Par ou Ímpar {cc} :v:',use_aliases=True))
# Estruturas
soma = 0
cont = 0
while True:
    maokalista = random.randint(0,1)
    par = int(input(emoji.emojize(f'Digite [{yw}2{cc}] para escolher {yw}PAR{cc} OU [{yw}3{cc}] para escolher {yw}ÍMPAR{cc}\n',use_aliases=True)))
    if par == 2:
        escolha = 'PAR'
    else:
        escolha = 'ÍMPAR'
    if par == 2 or par == 3:
        while True:
            mao = int(input(emoji.emojize(f'Digite [{co}0{cc}] para escolher {co}ZERO{cc} :fist: OU [{co}1{cc}] para escolher {co}UM{cc} :point_up:\n',use_aliases=True)))
            soma = mao + maokalista
            print(soma)
            if mao == 0 or mao == 1:
                break
            else:
                print(f'{rd}Erro! Você digitou errado!{cc}')
                mao = 0
        if mao == 0:
            emao = ':fist:'
        elif mao == 1:
            emao = ':point_up: '
        if maokalista == 0:
            emaokali = ':fist:'
        elif maokalista == 1:
            emaokali = ':point_up:'
        print(mao, maokalista)
        print(emoji.emojize(f'{we}VOCÊ{cc} escolheu {we}{escolha}{cc} com a mão {emao}{cc} e {we}EU{cc} escolhi {emaokali}',use_aliases=True))
        sleep(1)
        print('Acho que...')
        sleep(1.5)
        if par == 2:
            if soma % 2 == 0:
                print(emoji.emojize(f'Você {gn}ganhou{cc}... {random.choice(sadmojis)}  {we}Quero revanche!{cc}',use_aliases=True))
                cont += 1
                soma = 0
            else:
                print(emoji.emojize(f'Você {rd}perdeu{cc}!! {random.choice(hapmojis)}',use_aliases=True))
                break
        elif par == 3:
            if soma % 2 != 0:
                print(emoji.emojize(f'Você {gn}ganhou{cc}... {random.choice(sadmojis)}  {we}Quero revanche!{cc}',use_aliases=True))
                cont += 1
                soma = 0
            else:
                print(emoji.emojize(f'Você {rd}perdeu{cc}!! {random.choice(hapmojis)}',use_aliases=True))
                break       
    else:
        print(f'{rd}Erro! Você digitou errado!{cc}')
# Encerramento
print(emoji.emojize(f'Você venceu {gn}{cont} {"vez" if cont == 1 else "vezes"}{cc}! {we}Obrigada por jogar comigo!{cc} :wink:',use_aliases=True))
