# Abertura
print('Média de idade, homem mais velho, mulheres com menos de 20 anos')
# Perguntas
soma = 0
nomes = []
idades = []
for a in range(1,3):
    print('-' * 3, f'{a}ª Pessoa', '-' * 3)
    nome = str(input('Nome? ')).strip().lower().title
    nomes += [nome]
    idade = int(input('Idade? '))
    idades += [idade]
    soma += idade
    print('Qual é o seu sexo?\n1 | Feminino\n2 | Masculino')
    sexo = int(input(''))
    if sexo == 1:
        sexo = 1
    elif sexo == 2:
        sexo = 2
print(nomes, idades, soma / a)
