    # Cadastro de Trabalhador #
# Modules
from datetime import date
# Variables
year = date.today().year
ficha = {}
    # Code #
ficha['Nome'] = str(input('Nome: ')).lower().capitalize()
ficha['Idade'] = year - int(input('Ano de Nascimento: '))
ficha['CTPS'] = int(input('CTPS (0 para não): '))
if ficha['CTPS'] != 0:
    ficha['Contratação'] = int(input('Ano de Contratação: '))
    ficha['Salário'] = float(input('Salário: R$ '))
    ficha['Aposentadoria'] = (35 - (year - ficha['Contratação'])) + ficha['Idade']
    # Encerramento #
print('-' * 50)
for k, v in ficha.items():
    print(f'{k}: {v}')
print('-' * 50)
