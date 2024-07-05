    # Cadastro de Pessoas #
# Colors
rd = '\033[31m'
be = '\033[34m'
bk = '\033[1;30m'
we = '\033[1;37m'
pk = '\033[35m'
gn = '\033[32m'
cc = '\033[m'
# Variables
fichas = []
dados = {}
cont = 1
media = 0
# Code
while True:
    while True: # Dados da pessoa
        dados['Nome'] = str(input(f'Nome da {cont}ª pessoa: ')).lower().capitalize()
        while True: # Digitar corretamente o sexo
            sexo = str(input(f'Sexo: ')).lower()
            if sexo[0] in 'm':
                dados['Sexo'] = 'Masculino'
                break
            elif sexo[0] in 'f':
                dados['Sexo'] = 'Feminino'
                break
            else:
                print(f'Digite {be}M{cc} para {be}Masculino{cc} ou {pk}F{cc} para {pk}Feminino{cc}!')
        dados['Idade'] = int(input(f'Idade: '))
        print('-' * 100)
        for k,v in dados.items(): # Mostrar os dados
            print(f'{bk}{k}{cc}: {we}{v}{cc}',end=' | ')
        while True: # Verificar se os dados estão corretos
            right = str(input(f'As informações estão corretas? {gn}S{cc} para {gn}Sim{cc} ou {rd}N{cc} para {rd}Não{cc} '))
            if right[0] in 'sn':
                break
        if right[0] in 's':
            break
    # Finalizar a coleta dos dados
    media += dados['Idade']
    print(media)
    fichas.append(dados.copy())
    cont += 1
    ask = str(input(f'Deseja adicionar mais pessoas? {gn}S{cc} para {gn}Sim{cc} ou {rd}N{cc} para {rd}Não{cc} '))
    if ask[0] in 'n':
        break
    if ask[0] in 's':
        print('-' * 100)
# Encerramento
print('-' * 100)
print(f'A) Foram {we}cadastradas {len(fichas)} pessoas{cc}.')
print(f'B) A {we}média de idade é {media / len(fichas):.2f} anos{cc}.')
print('-' * 100)
print(f'C) Lista com {we}nomes das mulheres{cc}: ',end='')
for b in fichas:
    if b['Sexo'] in 'Feminino':
        print(b['Nome'],end=' ')
print()
print('-' * 100)
print(f'D) Pessoas {we}acima da média de idade{cc}: ')
for c in fichas:
    if c['Idade'] >= media / len(fichas):
        print(f'{we}{c["Nome"]}{cc} com {we}{c["Idade"]} anos{cc}.')
        