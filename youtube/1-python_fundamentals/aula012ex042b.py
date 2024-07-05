# Módulos
import emoji
# Cores
b = '\033[1;34m'
cc = '\033[m'
# Fachada
print(emoji.emojize(':small_red_triangle: Triângulos :small_red_triangle:', use_aliases=True))
# Perguntas
n1 = float(input('Primeiro lado: '))
n2 = float(input('Segundo lado: '))
n3 = float(input('Terceiro lado: '))
# Cálculos
dif = n2 - n3
if dif < 0:
    dif = dif * -1
soma = n2 + n3
# Condições
if n1 > dif and n1 <= soma:
    if n1 == n2 == n3:
        print(f'É formado um triângulo {b}equilátero{cc}.')
    elif n1 != n2 != n3 != n1:
        print(f'É formado um triângulo {b}escaleno{cc}.') 
    else:
        print(f'É formado um triângulo {b}isósceles{cc}.')
else:
    print('\033[1;31mNão é possível\033[m formar um triângulo.')
print(emoji.emojize(':small_red_triangle: Espero ter sanado a sua dúvida! :small_red_triangle:',use_aliases=True))
