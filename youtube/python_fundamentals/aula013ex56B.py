# Abertura
print('Média de idade, homem mais velho, mulheres com menos de 20 anos')
# Perguntas
soma = 0
idademaior = 0
nomemaior = ''
mulher = 0
for a in range(1,5):
    print('-' * 3, f'{a}ª Pessoa', '-' * 3)
    nome = str(input('Nome? ')).strip().lower().title()
    idade = int(input('Idade? '))    
    soma += idade
    print('Qual é o seu sexo?\n1 | Feminino\n2 | Masculino')
    sexo = int(input(''))
    if a == 1 and sexo == 2:
        idademaior = idade
        nomemaior = nome
    if sexo == 2 and idade > idademaior:
        idademaior = idade
        nomemaior = nome
    if sexo == 1 and idade < 20:
        mulher += 1
print(f'A média de idade é {soma / a}.')
if idademaior > 0:
    print(f'O homem mais velho tem {idademaior} e se chama {nomemaior}.')
else:
    print(end="")
print(f'{f"Existem {mulher}" if mulher > 0 else "Não há"} mulheres menores de 20 anos.')
