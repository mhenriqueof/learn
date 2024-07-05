cont = 1
while cont <= 10:
    print(cont, '...', end='')
    cont += 1
print('fim')

n = cont = 0
while cont <= 2:
    n = int(input('Número: '))
    cont += 1
    
n = s = 0
while True:
    n = int(input('Número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')
