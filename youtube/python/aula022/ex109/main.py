# Modules
import moeda
# Code
n = int(input(f'Digite um valor: R$ '))
# Closure
print('-' * 50)
print(f'{moeda.moeda(n)} aumentado em 10% vale {moeda.aumentar(n, 10, True)}')
print(f'A redução em 13% de {moeda.moeda(n)} é {moeda.reduzir(n, 13, False)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'{moeda.metade(n)} é a metade de {moeda.moeda(n)}')
print('-' * 50)
