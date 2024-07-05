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
    for tabu in range(usuario, (usuario * 10) + 1, usuario):
        print(f'{usuario} x {tabu / usuario:.0f} = {tabu}')
