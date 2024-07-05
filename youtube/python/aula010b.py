n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2

print(f'A sua média foi {m:.1f}.')
if m >= 6.0:
    print('Você não está em recuperação!')
else:
    print('Você está em recuperação.')
print('Estude mais e nunca pare!')

#(print'Você não está em recuperação!' if m >= 6.0 else 'Você está em recuperação.')