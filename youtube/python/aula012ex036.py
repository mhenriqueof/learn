# Fachada
print('-' * 10 + 'Bem-vindo(a) ao \033[1;42mEmpréstimo Bancário\033[m!' + '-' * 10)
# Imports
import emoji
import time
from datetime import date
year = date.today().year
time = time.strftime('%H',time.localtime())
horario = int(time)
# Perguntas
nome = str(input('Olá! Qual é o seu nome? '))
name = nome.lower().title()
if horario >= 12 and horario < 18:
    print(f'Boa tarde, {name}!')
elif horario >= 18 or horario < 18:
    print(f'Boa noite, {name}!')
elif horario >= 6 and horario < 12:
    print(f'Bom dia, {name}!')
salario = float(input(f'{name}, qual é o seu salário? (Digite sem vírgulas e pontos, considerando os centavos) R$ '))
casa = float(input('Qual é o valor da casa? (Digite sem vírgulas e pontos, considerando os centavos) R$ '))
ano = int(input('Em que ano você pretende quitar a casa? '))
if ano <= year:
    print(f'Por favor, digite um ano maior que {year}.')
    ano = int(input(''))
# Cálculos
prestacao = casa / ((ano - year) * 12)
limite = salario * 0.30
# Conclusão
print(f'As prestações da casa com valor {casa:.2f} para ser paga em {ano - year} anos será de {prestacao:.2f}.')
# Condições
ccolor = '\033[m'
if prestacao > limite:
    print(emoji.emojize(f'Desculpe, {name}, seu pedido de empréstimo \033[1;31mnão foi aprovado{ccolor}.:pensive:', use_aliases=True))
else:
    print(emoji.emojize(f'{name}, seu pedido de empréstimo \033[1;32mfoi aprovado{ccolor}!:star_struck:', use_aliases=True))
