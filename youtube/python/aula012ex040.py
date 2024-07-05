# Módulos
import emoji
# Cores
w = '\033[1;97m'
cc = '\033[m'
# Fachada
print(emoji.emojize(':white_square_button: \033[7mMédia dos alunos\033[m :black_square_button:', use_aliases=True))
# Perguntas
n1 = float(input('Primeira nota:\n'))
n2 = float(input('Segunda nota:\n'))
# Condições
media = (n1 + n2) / 2
if media < 5:
    print(f'A média do aluno é {w}{media:.1f}{cc}.\nO aluno está \033[1;31mreprovado\033[m!')
elif media >= 5 and media < 7:
    print(f'A média do aluno é {w}{media:.1f}{cc}.\nO aluno está em \033[1;33mrecuperação\033[m!')
else:
    print(f'A média do aluno é {w}{media:.1f}{cc}.\nO aluno está \033[1;32maprovado\033[m!')
