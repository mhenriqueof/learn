ano = int(input('Digite um ano para saber se ele é bissexto: '))

bi = ano % 4

if bi == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
print('Espero ter sanado sua dúvida. Obrigado!')
