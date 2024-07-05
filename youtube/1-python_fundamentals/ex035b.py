print('Digite três número para saber se é possível formar um triângulo com bases nesses valores:')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

dif = n2 - n3
if dif < 0:
    dif = dif * -1
soma = n2 + n3

if n1 > dif and n1 < soma:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo.')
