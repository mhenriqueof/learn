nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome letrado!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Que nome comum.')
elif nome in 'Ana Cláudia Jéssica Julia':
    print('Belo nome.')
else:
    print('Seu nome é normal.')
print(f'Tenha um bom dia, {nome}!')
