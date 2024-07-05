import random

print('Digite três números para saber qual é o menor e o maior entre eles: ')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

a = (n1 + n2 + n3) / 2

if n1 >= a:
    print(f'O maior valor é {n1}.')
if n2 >= a:
    print(f'O maior valor é {n2}.')
if n3 >= a:
    print(f'O maior valor é {n3}.')

if n1 <= n2:
    print(f'O menor valor é {n1}.')
if n2 <= n3:
    print(f'O menor valor é {n2}.')
if n3 <= n1:
    print(f'O menor valor é {n3}.')
    