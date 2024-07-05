    # Função para votação #
# Functions
def voto(idade):
    from datetime import date
    ano = date.today().year
    anos = ano - idade
    situ = ''
    if ano - idade >= 18:
        situ = 'OBRIGATÓRIO'
    elif 16 <= anos < 18 or anos > 65:
        situ = 'OPCIONAL'
    else:
        situ = 'INAPTO'
    return situ, anos


# Code
nasc = int(input(f'Ano de nascimento: '))
# Closure
print(f'Com {voto(nasc)[1]} anos seu voto é {voto(nasc)[0]}.')
