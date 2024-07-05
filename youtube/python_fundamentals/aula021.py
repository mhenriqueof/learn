def fatorial(num = 1):
    f = 1
    for a in range(num, 0, -1):
        f *= a
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}.')

#

def fatorial(num = 1):
    f = 1
    for a in range(num, 0, -1):
        f *= a
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f1, f2, f3)

#

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
print(par(num))
if par(num):
    print('É par!')
else:
    print('Não é par!')
    