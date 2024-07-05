def lin():
    print('-' * 30)
    
    
# Programa Principal
lin()
print('Pão')
lin()

def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)
    
# Programa
título(' pão ')
título(' criança ')
título(' mamãe ')

# Prática
print('---')
def soma(a, b):
    s = a + b
    print(s)


soma(a = 4, b = 5) # 4, 5 = parâmetros
soma(b = 8, a = 9)
soma(2, 1)

def contador(*núm):
    print(núm)
    print()

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def contador(*núm):
    for v in núm:
        print(v, end='')
    print()

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def contador(*núm):
    tam = len(núm)
    print(f'A lista {núm} possui {tam} números.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos  < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} é igual a {s}')
soma(5, 2)
soma(2, 9, 4)
