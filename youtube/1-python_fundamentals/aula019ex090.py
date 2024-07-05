    # Escola Henrique Madre Tereza #
# Variables
fichas = []
dados = {}
cont = 1
# Colors
we = '\033[1m'
gn = '\033[32m'
be = '\033[34m'
yw = '\033[33m'
rd = '\033[31m'
cn = '\033[36m'
cc = '\033[m'
    # Code #
while True: # Nome e Média
    dados['Nome'] = str(input(f'Nome do {cont}º aluno: ')).capitalize()
    dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
    if dados['Média'] >= 7:
        dados['Situação'] = 'Aprovado'
    elif dados['Média'] < 5:
        dados['Situação'] = 'Reprovado'
    elif dados['Média'] >= 5:
        dados['Situação'] = 'Recuperação'
    fichas.append(dados.copy())
    cont += 1
    while True: # Continuar?
        ask = str(input(f'Deseja adicionar mais alunos? SIM ou NÃO ')).lower()
        if ask[0] in 'sn':
            break
    if ask[0] in 'n':
        break
    # Encerramento #
c = 0
co = 0
print('-' * 25)
for a in fichas:
    c = 0
    for k, v in a.items():
        # Cores
        if c == 0:
            if co % 2 == 0:
                cor = be
            else:
                cor = cn
            co += 1
        elif c == 1:
            if v < 5:
                cor = rd
            elif v >= 7:
                cor = gn
            elif v >= 5:
                cor = yw
        c += 1
        # Ficha
        print(f'{we}{k}{cc}: {cor}{v:^12}{cc}',end=' ')
    print()
print('-' * 25)
