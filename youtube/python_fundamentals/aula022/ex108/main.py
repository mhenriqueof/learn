# Modules
import moeda
# Code
n = int(input(f'Digite um valor: R$ '))
aum = moeda.aumentar(n)
dim = moeda.diminuir(n)
# Closure
print('-' * 50)
print(f'{moeda.moeda(n)} aumentado em {aum[1]}% vale {moeda.moeda(aum[0])}')
print(f'A diminuição em {dim[1]}% de {moeda.moeda(n)} é {moeda.moeda(dim[0])}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'{moeda.moeda(moeda.metade(n))} é a metade de {moeda.moeda(n)}')
print('-' * 50)
