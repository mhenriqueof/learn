# Módulos
import emoji
# Abertura
print(emoji.emojize(':one:  :arrow_up_small: :three:  Progressão Aritmética :three:  :arrow_up_small: :five:', use_aliases=True))
# Perguntas
num = int(input('Digite um número para continuar dele a progressão aritmética: '))
ordem = int(input('Digite a ordem da PA: '))
# Repetições
for pa in range(num, num + (ordem * 10), ordem):
    print(f' | {pa}', end=" | ")
