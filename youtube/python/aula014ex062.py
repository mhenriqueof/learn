# Módulos
import emoji
# Cores
bbe = '\033[44m'
bk = '\033[30m'
be = '\033[1;34m'
we = '\033[1m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':zero: :five:   {bbe} Progressão Aritmética {cc}  :five: :keycap_ten:',use_aliases=True))
# Perguntas
termo1 = int(input(f'{be}Termo: {cc}'))
razao1 = int(input(f'{we}Razão: {cc}'))
contador = -1
lista = []
# Estruturas
while contador != 9:
    contador += 1
    if contador % 2 == 0:
        fundo = '\033[1;34m'
    else:
        fundo = '\033[1m'
    calc1 = termo1 + (razao1 * contador)
    num = str(f'{fundo}{calc1}{cc}')
    lista += [num]
qntermos = 9
print(f' {bk}|{cc} '.join(lista))
# Estruturas continuar
termo10 = termo1 + (razao1 * (qntermos))
contador2 = -1
ask = ''
while ask != 0:
    ask = int(input(f'Quer continuar a partir do {lista[-1]}?\n[0] Não\n[1] Sim\n'))
    if ask == 1:
        termos = int(input('Mais quantos termos? '))
        while contador2 != termos:
            contador2 += 1
            if contador2 % 2 == 0:
                fundo2 = '\033[1;34m'
            else:
                fundo2 = '\033[1m'
            calc2 = termo10 + (razao1 * contador2)
            num2 = str(f'{fundo2}{calc2}{cc}')
            lista += [num2]
        termo10 = termo10 + (razao1 + (qntermos))
        print(f' {bk}|{cc} '.join(lista))
        