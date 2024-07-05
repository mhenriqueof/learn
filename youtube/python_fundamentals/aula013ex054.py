# Módulos
from datetime import date
year = date.today().year
print(year)
# Repetições
mai = 0
men = 0
what = 0
for pessoas in range(1, 8):
    ano = int(input(f'Qual é o ano de nascimento da {pessoas}ª pessoa? '))
    maior = year - ano
    if maior >= 21:
        mai += 1
    elif maior < 0:
        what += 1
    else:
        men += 1
print(f'{f"Há {men} pessoas menores" if men > 0 else "Não há nenhuma pessoa menor"} de idade e {f"{mai} pessoas maiores" if mai > 0 else "não há nenhuma pessoa maior"} de idade.{f" E {what} que ainda nem nasceram." if what >= 1 else ""}')
