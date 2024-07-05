print('Digite três número para saber se é possível formar um triângulo com bases nesses valores:')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

a = n2 - n3 + n1
b = n3 - n1 
c = n3 - n1

x = n2 + n3 - n1
y = n2 + n3
z = n3 + n1

if n1 >= a:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
if n1 <= x:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
