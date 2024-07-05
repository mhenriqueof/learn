    # Função para votação #
# Functions
def voto(ano=0):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NEGADO'
    elif 16 <=  idade < 18 or idade > 65:
        return f'Com {idade} anos: OPCIONAL'
    else:
        return f'Com {idade} anos: OBRIGATÓRIO'
    

# Closure
print(voto(int(input(f'Ano de nascimento: '))))
