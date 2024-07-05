    # Variáveis #
matriz = [[], [], [], [], [], [], [], [], []]
pares = coluna = maior = 0

    # Estruturas #
# Pergunta
for a in range(0,9):
    ask = int(input(f'{a+1}º valor: '))
    matriz[a] = ask
    
        # Pares
    if ask % 2 == 0:
        pares += ask
        # Terceira coluna
    if a == 2 or a == 5 or a == 8: 
        coluna += ask
        # Maior valor da segunda linha
    if a == 3:
        maior = ask
    elif a == 4:
        if ask > maior:
            maior = ask
    elif a == 5:
        if ask > maior:
            maior = ask        
    
# Matriz
for b in range(0,3):
    # Cor
    if b % 2 == 1:
        cor = '\033[30m'
    else:
        cor = '\033[m'
    if b == 2:
        print(f'[{cor}{matriz[b]:^8}]',end='\n')
        break
    print(f'[{cor}{matriz[b]:^8}]',end='')
for c in range(3,6):
    if c % 2 == 1:
        cor = '\033[30m'
    else:
        cor = '\033[m'
    if c == 5:
        print(f'[{cor}{matriz[c]:^8}]',end='\n')
        break
    print(f'[{cor}{matriz[c]:^8}]',end='')
for d in range(6,9):
    if d % 2 == 1:
        cor = '\033[30m'
    else:
        cor = '\033[m'
    print(f'[{cor}{matriz[d]:^8}]',end='')

# Encerramento
print(f'\nA soma dos valores pares é {pares}.') 
print(f'A soma dos valores da terceira coluna é {coluna}.')
print(f'O maior valor da segunda coluna é {maior}.')
