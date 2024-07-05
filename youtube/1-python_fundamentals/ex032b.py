from datetime import date

ano = int(input('Digite 0 para saber se seu ano atual é bissexto ou não. Ou digite um ano qualquer: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
    