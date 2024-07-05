# Módulos
import emoji
# Abertura
print(emoji.emojize(':two: :three:  Números primos :three: :two: ', use_aliases=True))
# Perguntas
num = int(input('Digite um número inteiro: '))
# Repetições
flag = False
if num > 1:
    for primo in range(2, num):
        if (num % primo) == 0:
            flag = True
            break
if flag:
    print(f'O {num} não é primo.')
else:
    print(f'O {num} é primo.')
