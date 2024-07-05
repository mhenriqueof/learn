for c in range(1, 10):
    print(c)

c = 1
while c < 10:
    print(c)
    c += 1

n = 1
while n != 0:
    n = int(input('Valor: '))
    
r = 's'
while r == 's':
    n = int(input('Valor: '))
    r = str(input('Continuar? [S/N]')).lower()
    
n = 1
par = impar = 0
while n != 0:
    n = int(input('Valor: '))
    if n != 0:    
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} número pares e {impar} número ímpares!')