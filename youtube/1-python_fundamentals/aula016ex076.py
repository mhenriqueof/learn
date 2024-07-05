# Módulos
import emoji
# Cores
ue = '\033[4m'
byw = '\033[1;43m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f'{f":radio: {byw} Produtos e Preços {cc} :credit_card:":^63}',use_aliases=True))
# Lista
lista = ('Lápis', 2.00,
         'Borracha', 1.50,
         'Caderno', 20.00,
         'Caneta', 1.75,
         'Mochila', 30.00)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        # Nome
        print(f'{lista[pos]:.<30}',end='')
    else:
        # Preço
        print(f'R$ {lista[pos]:>5.2f}')
    # Encerramento
print(emoji.emojize(f'{f"{ue}Aproveite os descontos!{cc} :wink:":^50}',use_aliases=True))
