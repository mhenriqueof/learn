    # Variáveis #
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna = maior = cont = 0
# Cores
we = '\033[1m'
gn = '\033[1;32m'
be = '\033[1;34m'
bk = '\033[1;30m'
cc = '\033[m'
    # Estruturas #
# Colocar na Matriz
for lin in range(0,3):
    for col in range(0,3):
        # Alternar cor
        if cont  % 2 == 0:
            cor = gn
        else:
            cor = be
        cont += 1
        # Matriz
        matriz[lin][col] = int(input(f'{cor}a{lin+1}{col+1}{cc}: '))
        # Soma pares
        if matriz[lin][col] % 2 == 0:
            pares += matriz[lin][col]
        # Soma terceira coluna
        if col == 2:
            coluna += matriz[lin][col]
        # Maior valor segunda linha
        if lin == 1:
            if col == 0:
                maior = matriz[lin][col]
            else:
                if matriz[lin][col] > maior:
                    maior = matriz[lin][col]
print('-' * 50)
# Mostrar a Matriz
for lin in range(0,3):
    for col in range(0,3):
        # Alternar cor
        cont += 1
        if cont  % 2 == 0:
            cor = gn
        else:
            cor = be
        # Matriz
        print(f'[{cor}{matriz[lin][col]:^5}{cc}]',end='')
    print()
print('-' * 50)
    # Encerramento #
print(f'A {we}soma dos valores pares{cc} é {bk}{pares}{cc}.') 
print(f'A {we}soma dos valores da terceira coluna{cc} é {bk}{coluna}{cc}.')
print(f'O {we}maior valor da segunda linha{cc} é {bk}{maior}{cc}.')
