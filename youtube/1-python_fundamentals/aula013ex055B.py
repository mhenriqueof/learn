# Abertura
print('Quem é o peso pena e o peso pesado?')
# Perguntas
lista = []
for a in range(1,6):
    pessoa = float(input(f'Qual é o peso da {a}ª pessoa? '))
    lista += [pessoa]
print(f'O peso pena é {min(lista)} e o pesado {max(lista)}.')
