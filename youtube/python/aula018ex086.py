    # Variáveis #
matriz = [[], [], [], [], [], [], [], [], []]
linha = coluna = 1

    # Estruturas #
for a in range(0,9):
    matriz[a] = int(input(f'a{linha}{coluna} '))
# Adicionar número da matriz
    if a == 2:
        coluna = 0
    elif a == 5:
        coluna = 0
    if a <= 1:
        coluna += 1
    elif a >= 2 and a < 5:
        coluna += 1
        linha = 2
    else:
        coluna += 1
        linha = 3

    # Encerramento #
for b in range(0,3):
    if b == 2:
        print(f'[{matriz[b]:^8}]',end='\n')
        break
    print(f'[{matriz[b]:^8}]',end='')
for c in range(3,6):
    if c == 5:
        print(f'[{matriz[c]:^8}]',end='\n')
        break
    print(f'[{matriz[c]:^8}]',end='')
for d in range(6,9):
    print(f'[{matriz[d]:^8}]',end='')
    