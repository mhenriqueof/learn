# Módulos
import emoji
# Cores
gn = '\033[1;32m'
we = '\033[1m'
rd = '\033[1;31m'
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
    if escolha < 0 or escolha > 20:
        print(f'{rd}Erro! Digite novamente.{cc}',end=' ')
    elif escolha >= 0 and escolha <=20:
        print(emoji.emojize(f'{we}{numeros[escolha]}{cc} :wink:',use_aliases=True))
        while True:
            ask = int(input(f'Desejar continuar? [{we}0{cc}] para {rd}NÃO{cc} | [{we}1{cc}] para {gn}SIM{cc} '))
            if 0 <= ask <= 1:
                break
            else:
                continue
        if ask == 1:
                continue
        elif ask == 0:
                break
# Encerramento
print(f'{we}Obrigada!{cc}')
