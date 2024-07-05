# Módulos
import emoji
# Cores
w = '\033[1;97m'
g = '\033[37m'
cc = '\033[m'
# Fachada
print(emoji.emojize(':money_with_wings: Cálculo do valor de um produto :money_with_wings:', use_aliases=True))
# Perguntas
valor = float(input('Valor do produto: '))
forma = int(input('Forma de pagamento\n1 | À vista no dinheiro\n2 | 2x no cartão\n3 | 3x ou mais no cartão\n4 | À vista no cartão\n'))
# Cálculos
juros = valor * 1.20
# Condições
if forma == 1:
    print(f'Novo valor: {w}{valor * 0.9:.2f}{cc}')
elif forma == 2:
    print(f'{w}2{cc} parcelas de {w}{valor / 2:.2f}{cc}.')
elif forma == 3:
    print(f'Novo valor de: {w}{juros:.2f}{cc}')
    parcelas = int(input('Parcelado em quantas vezes? '))
    print(f'{w}{parcelas}{cc} parcelas de {w}{juros / (parcelas):.2f}{cc}.')
elif forma == 4:
    print(f'Novo valor: {w}{valor * 0.95:.2f}{cc}')
else:
    print('Opção inválida!')