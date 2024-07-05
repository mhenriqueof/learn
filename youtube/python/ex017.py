import math

g = '\033[32m'
b = '\033[34m'
y = '\033[33m'
c = '\033[m'
co = float(input(f'Qual é o valor da {g}altura{c} do triângulo?  '))
ca = float(input(f'Qual é o valor da {y}base{c} do triângulo? '))
x = math.pow(co, 2) + math.pow(ca, 2)
h = math.sqrt(x)

print(f'Com a {g}altura{c} valendo {g}{co:.2f}{c} e a {y}base{c} valendo {y}{ca:.2f}{c} {b}, a hipotenusa{c} desse triângulo é {b}{math.floor(h):.2f}{c}.')
