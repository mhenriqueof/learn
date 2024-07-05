num = [2, 5 ,9 ,1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2,2)
if 5 in num:
    num.remove(5)
else:
    print('erro!')
print(num)
print(f'Esta lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'Valor: {v}')
    
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Posição: {c} | Valor: {v}')
print('pão')

valores = []
for cont in range(0, 5):
    valores.append(int(input('Valor: ')))
for v in valores:
    print(f'Valor: {v}')
    
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(a)
print(b)