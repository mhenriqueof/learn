n = int(input('Número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valor foi {s}.')