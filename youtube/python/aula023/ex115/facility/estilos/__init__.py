# Padrões para o código das cores
def color(col=97):
    return print(f'\033[1;{col}m', end='')


def ccolor():
    return print('\033[m')


def br(msg): # Bolder
    return f'\033[1m{msg}\033[m'


def gn(msg): # Green
    return f'\033[32m{msg}\033[m'


def rd(msg): # Red
    return f'\033[31m{msg}\033[m'


# Padrões para estruturas

def hyphens(msg):
    print('-' * 50)
    print(msg.center(50))
    print('-' * 50, end='')
