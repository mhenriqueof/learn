# Módulos
import emoji
# Cores
byw = '\033[30;43m'
be = '\033[1;34m'
bk = '\033[30m'
yw = '\033[33m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':zero: :one: :one:  {byw} Sequência de Fibonacci {cc} :two: :three: :five:',use_aliases=True))
# Perguntas
seq = int(input('Quantidade da sequência: '))
# Estruturas
num1 = 0
num2 = 1
print(f'{yw}{num1}{cc} {be}|{cc} {bk}{num2}{cc}',end='')
cont = 3
while cont <= seq:
    t3 = num1 + num2
    if cont % 2 == 0:
        cor = bk
    else:
        cor = yw
    print(f' {be}|{cc} {cor}{t3}{cc}',end='')
    cont += 1
    num1 = num2
    num2 = t3
# Encerramento
print(emoji.emojize(f' :no_entry: Esta é a {byw} Sequência de Fibonacci {cc} com \033[32m{seq}{cc} termos!:wink:',use_aliases=True))