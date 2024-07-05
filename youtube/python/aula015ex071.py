# Módulos
import emoji
from time import sleep
# Cores
bgn = '\033[42m'
we = '\033[1m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':bank: :money_with_wings: {bgn} Caixa Eletrônico {cc} :money_with_wings: :bank:',use_aliases=True))
# Estruturas
nota50 = nota20 = nota10 = nota1 = dinheiro = 0
dinheiro = int(input('Valor a ser sacado: R$ \033[4m'))
sleep(.5)
while True:
    # 50
    if dinheiro >= 50:
        while dinheiro >= 50:
            dinheiro -= 50
            nota50 += 1
    elif dinheiro >= 20:
        while dinheiro >= 20:
            dinheiro -= 20
            nota20 += 1
    elif dinheiro >= 10:
        while dinheiro >= 10:
            dinheiro -= 10
            nota10 += 1
    elif dinheiro > 0:
        dinheiro -= 1
        nota1 += 1
    if dinheiro == 0:
        break
# Condições
if nota50 > 0:
    print(f'{cc}{we}{nota50}{cc} {"cédula" if nota50 == 1 else "cédulas"} de \033[1;32mR$ 50{cc}')
if nota20 > 0:
    print(f'{cc}{we}{nota20}{cc} {"cédula" if nota20 == 1 else "cédulas"} de \033[1;35mR$ 20{cc}')
if nota10 > 0:
    print(f'{cc}{we}{nota10}{cc} {"cédula" if nota10 == 1 else "cédulas"} de \033[1;33mR$ 10{cc}')
if nota1  > 0:
    print(f'{cc}{we}{nota1}{cc} {"cédula" if nota1 == 1 else "cédulas"} de \033[1;34mR$ 1{cc}')
sleep(2)
# Encerramento
print(emoji.emojize(f'{we}O {cc}{bgn} Caixa Eletrônico {cc} {we}agredece por sua atividade!{cc}:wink:',use_aliases=True))
