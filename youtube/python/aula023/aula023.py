
try:
    a = int(input('Numerador: '))
    b = int(input('Demonidados: '))
    r = a / b
except Exception as erro:
    print(f'Houve um problema! Erro: {erro.__class__}')
else:
    print(f'O resultado é {r}.')
finally:
    print('Pão!')

#

try:
    a = int(input('Numerador: '))
    b = int(input('Demonidados: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Houve um problema!')
except ZeroDivisionError:
    print('Dividir por zero não dá.')
except KeyboardInterrupt:
    print('Nada informado.')
else:
    print(f'O resultado é {r}.')
finally:
    print('Pão!')
    