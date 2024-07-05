# Módulos
import emoji
# Cores
bgn = '\033[42m'
yw = '\033[33m'
co = '\033[36m'
rd = '\033[31m'
gn = '\033[32m'
we = '\033[1m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f' :arrow_down_small::keycap_ten::arrow_down_small: {bgn} Loja do DezConto {cc} :arrow_down_small::keycap_ten::arrow_down_small: ',use_aliases=True))
# Variáveis
total = cont = contMil = menor = 0
barato = ''
# Estruturas
while True:
    # Nome
    produto = input(f'{yw}Nome:{cc} ').strip()
    # Preço
    while True:
        preco = int(input(f'{co}Preço:{cc} '))
        if preco > 0:
            break
    total += preco
    if preco >= 1000:
        contMil += 1
    # Menor preço
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    # Continuar?
    while True:
        stop = str(input(f'{we}Continuar?{cc}\n[{rd}N{cc}] para {rd}NÃO{cc} OU [{gn}S{cc}] para {gn}SIM{cc}\n')).strip()[0]
        if stop in "sSnN":
            break
    if stop in "nN":
        break
# Encerramento
print(f'O {we}total{cc} da compra é {we}R$ {total:.2f}{cc}\n{we}{contMil}{cc} {"produto" if contMil == 1 else "produtos"} com valor maior que {we}R$ 1000.00{cc}\nO produto mais {we}barato{cc} é {yw}{barato}{cc} que custa {we}R$ {menor:.2f}{cc}')
