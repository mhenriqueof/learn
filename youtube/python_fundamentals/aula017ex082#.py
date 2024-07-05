# Módulos
import emoji
# Cores
be = '\033[34m'
yw = '\033[33m'
gn = '\033[32m'
rd = '\033[31m'
ue = '\033[4m'
we = '\033[1m'
bwe = '\033[7m'
cc = '\033[m'

# Variáveis
cont = 1
lista = []
lispar = []
lisimp = []

# Abertura
print(emoji.emojize(f':printer:  {bwe} Listas {cc} :printer:'))
# Estruturas
while True:
    # Pergunta do número
    num = int(input(f'{bwe}{cont}º{cc} {we}número:{cc} '))
    # Mandar para a lista
    lista += [num]
    # Contador da quantidade de números perguntados
    cont += 1
    # Parar o While da pergunta
    while True:
        ask = str(input(f'{we}Deseja continuar?{cc} {gn}SIM{cc} ou {rd}NÃO{cc} ')).strip().lower()
        ask = ask[0]
        if ask in 's' or ask in 'n':
            break
    if ask in 'n':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        lispar.append(v)
    elif v % 2 == 1:
        lisimp.append(v)
# Encerramento
print(f'A {we}lista completa{cc}: {we}{lista}{cc}')
print(f'A {yw}lista com pares{cc}: {yw}{lispar}{cc}')
print(f'A {be}lista com ímpares{cc}: {be}{lisimp}{cc}')
