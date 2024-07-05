def aumentar(num=0, taxa=0, reais=False):
    valor = num * (1 + (taxa / 100))
    return valor if reais is False else moeda(valor)


def reduzir(num, taxa=0, reais=False):
    valor = num * (1 - (taxa / 100))
    return valor if reais is False else moeda(valor)


def dobro(num, reais=False):
    valor = num * 2
    return valor if reais is False else moeda(valor)


def metade(num, reais=False):
    valor = num / 2
    return valor if reais is False else moeda(valor)


def moeda(num):
    return f'R$ {num:.2f}'.replace('.',',')
