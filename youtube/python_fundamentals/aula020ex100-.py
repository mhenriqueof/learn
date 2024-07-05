    # Sortear e somar #
# Modules
from random import randint as ran
# Functions
def sorteia():
    for a in range(1, 6):
        r = ran(0,15)
        print(f'O {a}º número sorteado é o {r}.')
        números.append(r)


def somaPar():
    for b in números:
        if b % 2 == 0:
            pares.append(b)    


# Code
pares = []
números = []
sorteia()
somaPar()
# Encerramento
print(f'A soma dos números pares da lista {números} é {sum(pares)}.')
