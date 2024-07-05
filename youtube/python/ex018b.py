from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo para saber seu seno, cosseno e tangente: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'O ângulo {ang} possui o seu seno igual a {seno:.2f}, cosseno valendo {cos:.2f} e tangente como {tan:.2f}.')
