    # Validação valor numérico #
# Colors
cc = '\033[m'
we = '\033[31m'
# Functions
def leiaInt(check):
    n = input(check)
    while not n.isnumeric():
        print(f'{we}"{n}" não é um número!{cc}')
        n = input(check)    
    n = int(n)
    return n


# Code
n = leiaInt('Número: ')
print(f'Você digitou o número {n}.')
