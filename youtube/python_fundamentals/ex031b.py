viagem = float(input('Qual é a distância da viagem em Km? '))

if viagem <= 200:
    duze = viagem * 0.5
else:
    duze = viagem * 0.45
    
print(f'O valor a ser pago pela viagem será de R${duze:.2f}.')
