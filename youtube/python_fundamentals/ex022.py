nome = str(input('Qual é o seu nome completo? '))

nomesep = nome.split()
nomesepa = ' '.join(nomesep)
nomesemespaco = ''.join(nomesep)
nomeletras = nomesemespaco.count('', 0, -1)
nomepletras = nomesep[0].count('', 0, -1)

print(f'Seu nome em maiúscula é {nomesepa.upper()}')
print(f'Seu nome em minúscula é {nomesepa.lower()}')
print(f'Seu nome ao todo tem {nomeletras} letras.')
print(f'Seu primeiro nome {nomesep[0]} possui {nomepletras} letras.')
