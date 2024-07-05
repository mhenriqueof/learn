# Módulos
import emoji
# Cores
rd = '\033[31m'
we = '\033[1m'
gn = '\033[32m'
yw = '\033[33m'
bbe = '\033[44m'
brd = '\033[41m'
cc = '\033[m'

# Variáveis
quest = []
lista = []
mai = men = 0

# Abertura
print(emoji.emojize(f' :a: :b: :a: {brd} Nomes {cc} + {bbe} Pesos {cc} :seven: :zero:',use_aliases=True))
# Estruturas
while True:
    # Perguntas da pessoa
    quest.append(str(input('Nome: ')))
    quest.append(float(input('Peso: ')))
    # Colocar nas listas
    if len(lista) == 0:
        mai = men = quest[1]
    else:
        if quest[1] > mai:
            mai = quest[1]
        elif quest[1] < men:
            men = quest[1]
    lista.append(quest[:])
    quest.clear()
    # Perguntar continuar₢
    while True:
        ask = str(input(f'Deseja continuar? {gn}SIM{cc} ou {rd}NÃO{cc} ')).strip().lower()
        if ask[0] in 'n' or ask[0] in 's':
            break
    if ask[0] in 'n':
        break
# Encerramentolista.sort()
print(lista)
print('=' * 50)
print(f'Foram contadas {we}{len(lista)}{cc} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de | ',end='')
for p in lista:
    if p[1] == mai:
        print(p[0], end=' | ')
print()
print(f'O menor peso foi de {men}Kg. Peso de | ',end='')
for p in lista:
    if p[1] == men:
        print(p[0], end=' | ')
print()
