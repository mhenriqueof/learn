def aumentar(num):
    valor = int(input(f'Aumentar {num} em quantos %? '))
    return num * (1 + (valor / 100)), valor


def diminuir(num):
    valor = int(input(f'Diminuir {num} em quantos %? '))
    return num * (1 - (valor / 100)), valor


def dobro(num):
    return num * 2


def metade(num):
    return num / 2

