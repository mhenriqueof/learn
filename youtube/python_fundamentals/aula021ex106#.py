    # Mini-sistema #
# Modules
from time import sleep
# Colors
col = ('\033[m',
       '\033[47m',
       '\033[1;42m',
       '\033[1;44m',
       '\033[1;41m'
    )
# Functions
def ajuda(com):
    """
    Pertime ao usuário saber informações de uma função.
    """
    title(f'Acessando o manual do comando {com}...', 3)
    print(col[1], end='')
    print('-' * 30)
    help(com)
    print('-' * 30)
    print(col[0], end='')
    print()
    sleep(1)
    
    
def title(msg, cor=0):
    print(col[cor], end='')
    print('=' * 30)
    print(f'{msg:^30}')
    print('=' * 30)
    print(col[0], end='')
    
    
def ask(check):
    inputOk = input(check)
    while not inputOk.isalpha():
        print('ERRO! Digite alguma função!')
        inputOk = input(check)
    inputOk = str(inputOk).strip().lower()
    return inputOk


# Code
title('Kalista Helper', 2)
while True:
    inputOk = ask('Digite uma função para saber seus detalhes [Digite "fim" para parar]: ')
    if inputOk in 'fim':
        title('Espero ter ajudado!', 4)
        break
    else:
        ajuda(inputOk)
