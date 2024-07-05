# Módulos
import emoji
# Cores
we = '\033[1m'
rd = '\033[31m'
cc = '\033[m'
# Abertura
print(emoji.emojize(':soon: Número por Extenso :end:',use_aliases=True))
# Tuplas
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
# Pergunta
while True:
    escolha = int(input(f'Número de {we}0{cc} a {we}20{cc}: '))
    if escolha >= 0 and escolha <=20:
        break
    else:
        print(f'{rd}Erro! Digite novamente.{cc}',end=' ')
# Encerramento
print(emoji.emojize(f'{we}{numeros[escolha]}{cc} :wink:',use_aliases=True))
