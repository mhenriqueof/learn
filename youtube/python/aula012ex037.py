# Fachada
print(f'-' * 15 + '|', 'Bem-vindo(a) ao \033[1;33mConversor de Bases\033[m!', "|" + '-' * 15)
# Módulos
import time
import emoji
time = time.strftime('%H',time.localtime())
horario = int(time)
# Cores
b = '\033[1;34m'
y = '\033[1;33m'
g = '\033[1;32m'
r = '\033[1;31m'
w = '\033[1;97m'
cc = '\033[m'
# Perguntas
if horario >= 6 and horario < 12:
    num = int(input('Bom dia! Qual número você deseja converter? '))
elif horario >= 12 and horario < 18:
    num = int(input('Boa tarde! Qual número você deseja converter? '))
else:
    num = int(input('Boa noite! Qual número você deseja converter? '))
# Pergunta para bases
print(f'Você deseja converter o número {g}{num}{cc} para qual base?\nDigite {b}1{cc} para {r}binário{cc}\nDigite {b}2{cc} para {r}octal{cc}\nDigite {b}3{cc} para {r}hexadecimal{cc}')
base = int(input(''))
# Condições
if base > 3 or base < 0:
    print(f'Por favor, digite {b}1{cc}, {b}2{cc} ou {b}3{cc}!')
    base = int(input(''))
if base == 1:
    print(f'O número {g}{num}{cc} em {r}binário{cc} é {w}{num:b}{cc}.')
elif base == 2:
    print(f'O número {g}{num}{cc} em {r}octal{cc} é {w}{num:o}{cc}.')
else:
    print(f'O número {g}{num}{cc} em {r}hexadecimal{cc} é {w}{num:x}{cc}.')
# Despedida
print(emoji.emojize(f'Obrigado por utilizar o nosso {y}Conversor de Bases{cc}! Até mais!:wink:', use_aliases=True))
