    # Mini-sistema #
# Colors
cc = '\033[m'
we = '\033[47m'
gn = '\033[1;42m'
be = '\033[1;44m'
rd = '\033[1;41m'
# Functions
def title(msg):
    print(gn, end='')
    print('=' * 30)
    print(f'{msg:^30}')
    print('=' * 30)
    print(cc, end='')
    
    
def ask(check):
    inputOk = input(check)
    while not inputOk.isalpha():
        print('ERRO! Digite alguma função!')
        inputOk = input(check)
    inputOk = str(inputOk).strip().lower()
    return inputOk


def ajuda(txt):
    """
    Pertime ao usuário saber informações de uma função.
    """
    from time import sleep
    print(be, end='')
    print(f'Buscando o manual de "{txt}"...', flush=True)
    print(cc, end='')
    print()
    print(we, end='')
    sleep(1.5)
    print('-' * 30)
    help(txt)
    print('-' * 30)
    print(cc, end='')
    print()
    sleep(1)


def end(msg):
    print(rd, end='')
    print('~' * 30)
    print(f'{msg:^30}')
    print('~' * 30)
    print(cc, end='')
    print()


# Code
title('Kalista Helper')
while True:
    inputOk = ask('Digite uma função para saber seus detalhes [Digite "fim" para parar]: ')
    if inputOk in 'fim':
        print(end('Espero ter ajudado!'))
        break
    else:
        ajuda(inputOk)
