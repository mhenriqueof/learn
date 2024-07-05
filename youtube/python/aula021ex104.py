    # Validação valor numérico #
# Colors
cc = '\033[m'
we = '\033[31m'
# Functions
def leiaInt(num):
    while True:
        n = str(input(num))
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print(f'{we}"{n}" não é um número!{cc}')


# Code
n = leiaInt('Número: ')
print(f'Você digitou o número {n}.')
