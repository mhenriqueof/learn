from math import trunc as inteiro
num = float(input('Digite um número decimal: '))
cc = '\033[m'

print(f'O número \033[1;30m{num}{cc} tem sua parte inteira como \033[97m{inteiro(num)}{cc}.')
