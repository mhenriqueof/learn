# Modules
import moeda
<<<<<<< Updated upstream
import facility
=======
>>>>>>> Stashed changes
# Colors
cc = '\033[m'
we = '\033[1m'
rd = '\033[31m'
gn = '\033[32m'
be = '\033[34m'
cn = '\033[36m'
yw = '\033[33m'
# Code
<<<<<<< Updated upstream
n = int(input(f'{we}Digite um valor{cc}: '))
som = moeda.aumentar(n)
sub = moeda.diminuir(n)
# Closure
facility.hyphens(f'{rd}{n} + {som[1]}{cc} = {gn}{som[0]}{cc}\n{be}{n} - {sub[1]}{cc} = {gn}{sub[0]}{cc}\nO {yw}dobro de {n}{cc} é {gn}{moeda.dobro(n)}{cc}\nA {cn}metade de {n}{cc} é {gn}{moeda.metade(n)}{cc}')
=======
n = int(input(f'Digite um valor: '))
aum = moeda.aumentar(n)
dim = moeda.diminuir(n)
# Closure
print('-' * 50)
print(f'{we}{n}{cc} {rd}aumentado em {aum[1]}%{cc} vale {gn}{aum[0]}{cc}')
print(f'A {be}diminuição em {dim[1]}%{cc} de {we}{n}{cc} é {gn}{dim[0]}{cc}')
print(f'O {yw}dobro{cc} de {we}{n}{cc} é {gn}{moeda.dobro(n)}{cc}')
print(f'{gn}{moeda.metade(n)}{cc} é a {cn}metade{cc} de {we}{n}{cc}')
print('-' * 50)
>>>>>>> Stashed changes
