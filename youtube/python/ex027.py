nome = input('Digite seu nome completo: ')

junta = nome.split()
jupara = ' '.join(junta)
mainome = jupara.title()
pnome = mainome.split()

print('Nome completo:', mainome)
print('Primeiro nome:', pnome[0])
print('Último nome:', pnome[-1])
