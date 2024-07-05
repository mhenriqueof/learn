def aumentar(num, val=0, reais=False):
    if reais == True:
        return f'R$ {num * (1 + (val / 100)):.2f}'
    else:
        return f'{num * (1 + (val / 100)):.2f}'


def reduzir(num, val=0, reais=False):
    if reais == True:
        return f'R$ {num * (1 - (val / 100)):.2f}'
    else:
        return f'{num * (1 - (val / 100)):.2f}'

def dobro(num, reais=False):
    if reais == True:
        return f'R$ {num * 2:.2f}'
    else:
        return num * 2   


def metade(num, reais=False):
    if reais == True:
        return f'R$ {num / 2:.2f}'
    else:
        return num / 2    


def moeda(num):
        return f'R$ {num}'


def resumo(n, aum, dim):
    print('-' * 50)
    print(f'{"Resultados Obtidos":^50}')
    print('-' * 50)
    print(f'{moeda(n)} aumentado em {aum}% vale {aumentar(n, aum, True)}')
    print(f'A redução em {dim}% de {moeda(n)} é {reduzir(n, dim, False)}')
    print(f'O dobro de {moeda(n)} é {dobro(n, True)}')
    print(f'{metade(n, False)} é a metade de {moeda(n)}')
    print('-' * 50)
