# Módulos
import emoji
import random
from time import sleep
# Cores
under = '\033[4m'
cc = '\033[m'
# Fachada
print(emoji.emojize(':fist::raised_hand_with_fingers_splayed: :v: Jogo do Jokenpô :v: :raised_hand_with_fingers_splayed: :fist:', use_aliases=True))
# Pergunta da mão
mao = int(input(emoji.emojize(f'Digite\n1 para {under}Pedra{cc} :fist:\n2 para {under}Papel :raised_hand_with_fingers_splayed:{cc}\n3 para {under}Tesoura{cc} :v:\n', use_aliases=True)))
# Escolha da Kalista
lista = ['1', '2', '3']
random.shuffle(lista)
escolha = random.choice(lista)
# Condições escolha (mostrar emoji)
usu = int(mao)
kali = int(escolha)
if usu == 1:
    usuario = emoji.emojize(':fist:', use_aliases=True)
elif usu == 2:
    usuario = emoji.emojize(':raised_hand_with_fingers_splayed: ', use_aliases=True)
else:
    usuario = emoji.emojize(':v:', use_aliases=True)
if kali == 1:
    computador = emoji.emojize(':fist:', use_aliases=True)
elif kali == 2:
    computador = emoji.emojize(':raised_hand_with_fingers_splayed:', use_aliases=True)
else:
    computador = emoji.emojize(':v:', use_aliases=True)
# Resultado
sleep(.5)
print('JO')
sleep(.5)
print('KEN')
sleep(.5)
print('PÔ')
sleep(.5)
print(f'Você escolheu {usuario} e eu escolhi {computador}')
sleep(1)
print('Parece que...')
sleep(2)
# Condições
if usu == kali:
    print(emoji.emojize('Empatou. :raised_eyebrow:', use_aliases=True))
elif usu == 1 and kali == 3:
    print(emoji.emojize('Hum... você ganhou... :unamused:', use_aliases=True))
elif usu == 1 and kali == 2:
    print(emoji.emojize('Uhu! Eu ganhei! :grin:', use_aliases=True))
elif usu == 2 and kali == 1:
    print(emoji.emojize('Hum... você ganhou... :unamused:', use_aliases=True))
elif usu == 2 and kali == 3:
    print(emoji.emojize('Uhu! Eu ganhei! :grin:', use_aliases=True))
elif usu == 3 and kali == 1:
    print(emoji.emojize('Uhu! Eu ganhei! :grin:', use_aliases=True))
elif usu == 3 and kali == 2:
    print(emoji.emojize('Hum... você ganhou... :unamused:', use_aliases=True))
sleep(1)
# Despedida da Kalista
print(emoji.emojize(f'Obrigada por jogar comigo!:blush:', use_aliases=True))
