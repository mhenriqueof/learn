import math
ang = float(input('Digite um ângulo para saber seu seno, cosseno e tangente: '))
nseno = math.radians(ang)
ncos = math.radians(ang)
ntan = math.radians(ang)
seno = math.cos(nseno)
cos = math.sin(ncos)
tan = math.tan(ntan)
print(f'O ângulo {ang} possui o seu seno igual a {seno}, cosseno valendo {cos} e tangente como {tan}.')
