# Fachada
print('()' * 8,'Bem vindo(a) ao \033[7mComparador de Números\033[m!','()' * 8)
# Módulos
import emoji
from time import sleep
import time
time = time.strftime('%H',time.localtime())
hora = int(time)
# Cores
w = '\033[1;97m'
b = '\033[1;34m'
r = '\033[1;31m'
cc = '\033[m'
# Perguntas
if hora >= 6 and hora < 12:
    print(emoji.emojize(f'Bom dia!:sunny:  Digite {w}dois números{cc} para compará-los!',use_aliases=True))
elif hora >= 12 and hora < 18:
    print(emoji.emojize(f'Boa tarde!:sun_with_face: Digite {w}dois números{cc} para compará-los!',use_aliases=True))
else:
    print(emoji.emojize(f'Boa noite!:crescent_moon: Digite {w}dois números{cc} para compará-los!',use_aliases=True))
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
sleep(.25)
print('Espere um momento, vou analisá-los...')
sleep(2)
print(f'Analisando {w}{num1}{cc}...')
sleep(2)
print(f'Analisando {w}{num2}{cc}...')
sleep(2)
print('\033[32mAnálise concluída!\033[m')
sleep(.5)
# Condições
if num1 == num2:
    print(f'O número {w}{num1}{cc} e {w}{num2}{cc} são \033[1;33miguais{cc}.',end='')
if num1 < num2:
    print(f'O {b}menor{cc} número é {w}{num1}{cc}',end=' ')
elif num2 < num1:
    print(f'O {b}menor{cc} número é {w}{num2}{cc}',end=' ')
if num1 > num2:
    print(f'e o {r}maior{cc} é {w}{num1}{cc}.',end='')
elif num2 > num1:
    print(f'e o {r}maior{cc} é {w}{num2}{cc}.',end='')
# Agradecimento
print(emoji.emojize('\nObrigado por utilizar o nosso \033[7mComparador de Números\033[m!:ghost:',use_aliases=True))
