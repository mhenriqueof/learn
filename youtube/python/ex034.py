salario = float(input('Qual é o seu salário? '))

if salario >= 1250:
    print(f'Seu aumento será de R${(salario * 1.10) - salario:.2f}! Passando a ser R${salario * 1.10:.2f}!')
else:
    print(f'Seu aumento será de R${(salario * 1.15) - salario:.2f}! Passando a ser R${salario * 1.15:.2f}!')
print('Nós honestamente agradecemos por toda a sua contribuição com a Martech! Esperamos que o aumento atenda às suas necessidades.')
