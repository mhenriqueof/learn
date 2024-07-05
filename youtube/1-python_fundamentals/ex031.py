viagem = float(input('Qual é a distância da viagem em Km? '))

duze = 0.50 * viagem
sup = 0.45 * viagem

if viagem <= 200:
    print(f'O valor da viagem é de R${duze:.2f}')
else:
    print(f'O valor da viagem é de R${sup:.2f}')
print('A forma de pagamento será crédito ou débito?')
