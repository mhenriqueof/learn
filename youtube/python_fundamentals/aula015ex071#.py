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
total = dinheiro
ced = 50
totced = 0
while True:
    if total >= ced:
        total -=ced
        totced += 1
    else:
        if totced > 0:
            print(f'{cc}{we}{totced}{cc} {"cédula" if nota50 == 1 else "cédulas"} de \033[1;32mR$ {ced}{cc}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
sleep(2)
# Encerramento
print(emoji.emojize(f'{we}O {cc}{bgn} Caixa Eletrônico {cc} {we}agredece por sua atividade!{cc}:wink:',use_aliases=True))
