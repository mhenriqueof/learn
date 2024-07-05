    # Sortear e somar #
# Modules
from random import randint as ran
# Functions
def sorteia(pão):
    for a in range(1, 6):
        pão.append(ran(0,15))


def somaPar(pares):
    somapares = 0
    for b in pares:
        if b % 2 == 0:
            somapares += b
    print(f'A soma dos números pares da lista {números} é {somapares}.')


# Code
números = []
sorteia(números)
somaPar(números)
