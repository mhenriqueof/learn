nome = input('Digite seu nome completo: ').strip()

lnome = nome.lower()
a = 'silva' in lnome

print(f'Seu nome possui Silva? {a}')
