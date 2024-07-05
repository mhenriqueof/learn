# Módulos
import emoji
# Cores
yw = '\033[30;43m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':zero: :one: :one:  {yw} Sequência de Fibonacci {cc} :two: :three: :five:',use_aliases=True))
# Perguntas
num1 = int(input('Número: '))
seq = int(input('Quantidade da sequência: '))
# Estruturas
contador = seq
num2 = 0
while contador != -1:
    print(num1 + num2)
    num1 = num1 + num2
    num2 += 1
    contador += -1