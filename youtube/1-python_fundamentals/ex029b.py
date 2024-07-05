velo = float(input('Em qual velocidade o seu carro está se movendo? '))

n1 = float(velo - 80)

if velo > 80:
    print('Você está fora da velocidade permitida! Por favor, reduza a velocidade para no máximo 80 Km/h o mais rápido possível! Dirija com segurança!')
    print(f'Você terá que pagar uma multa de R${n1 * 7:.2f}.')
print('Dirija com segurança!')
    