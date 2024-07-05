# Módulos
import emoji
# Fachada
print(emoji.emojize(':heavy_multiplication_x:   \033[4mTabuadas\033[m :heavy_multiplication_x:', use_aliases=True))
# Perguntas
usuario = int(input('Olá! Qual tabuada você quer saber?\n'))
# Repetições
if usuario == 0:
    print(emoji.emojize('O número 0 não tem tabuada!:wink:',use_aliases=True))
else:
    print(f'Dá uma olhada na tabuada do {usuario}')
    for tabu in range(1, 11):
        print(f'{usuario} x {tabu:.0f} = {tabu*usuario}')
