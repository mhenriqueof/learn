# Abertura
print('Quem é o peso pena e o peso pesado?')
# Perguntas
soma = 0
maior = 0
menor = 0
for a in range(1,6):
    pessoa = float(input(f'Qual é o peso da {a}ª pessoa? '))
    soma += pessoa
    if a == 1:
        maior = pessoa
        menor = pessoa
    else:
        if pessoa > maior:
            maior = pessoa
        if pessoa < menor:
            menor = pessoa
print(maior, menor, soma / a)