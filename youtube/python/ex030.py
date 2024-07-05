num = int(input('Digite um número para saber se ele é par ou ímpar: '))

a = num % 2

if a == 0:
    print(f'O número {num} é par.')
else :
    print(f'O número {num} é ímpar.')
