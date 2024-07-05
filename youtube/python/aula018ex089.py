    # Boletim com listas compostas #
# Variables
dados = []
boletim = []
ask = ''
c = 1
    # Code #
# Dados do aluno
while True: # Nome e nota
    name = str(input(f'Nome do {c}º estudante: ')).capitalize()
    boletim.append(name)
    c += 1
    for a in range(1,3):
        while True: # Verificar se a nota está em Int e colocar no boletim
            ok = True
            try:
                grade = float(input(f'{a}ª nota: '))
            except ValueError:
                ok = False
                print('Por favor, digite números.')
            if ok == True:
                boletim.append(grade)
                break
    dados.append(boletim[:])
    boletim.clear()
    while True: # Verificar se deseja continuar
        ask = str(input(f'Deseja continuar? SIM ou NÃO ')).lower()
        if ask[0] in 'sn':
            break
    if ask[0] in 'n':
        break
    # Encerramento #
# Tabela com os dados
print('-' * 25)
print(f'{"Nº"} | {"NOME":^10} | {"MÉDIA"}')
print()
for a, dado in enumerate(dados):
    print(f'{a}  | {dado[0]:^10} | {(dado[1] + dado[2])/2:>5.1f}')
print('-' * 25)
# Boletim individual
while True:
    who = int(input('Mostrar notas de qual aluno? (Digite o número do aluno) *999 para sair* '))
    if who == 999:
        break
    if who >= len(dados):
        continue
    else:
        print('-' * 25)
        print(f'Nome: {dados[who][0]}\nNotas: {dados[who][1]} e {dados[who][2]}')
        print('-' * 25)
print('\nColégio Estudual Henrique Joronfino')
