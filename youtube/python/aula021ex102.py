    # Função para fatorial #
# Functions
def fatorial(a, b = 0):
    """
    -> Fatorial de um número
        - parâmetro (a): número fatorial.
        - parâmetro (b): mostrar a estrutura do fatorial ou não.
    """
    f = 1
    for z in range(a, 0, -1): # Estrutura do fatorial
        f *= z
        if b  == 1: # Mostrar ou não a estrutura
            print(z, end='')
            if z == 1:
                print(' = ', end='')
            else:
                print(' x ', end='')
    return f

# Code
x = fatorial(int(input('Fatorial do número: ')), int(input('Deseja mostrar os números do fatorial? [0 para NÃO ou 1 para SIM] ')))
# Closure
print(x)
help(fatorial)
