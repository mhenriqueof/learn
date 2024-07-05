from time import sleep
from facility.estilos import *
from facility.data import *
# Checar inputs
def checkStr(txt):
    while True:
        try:
            check = str(input(txt)).strip().lower().title()
        except KeyboardInterrupt:
            print('\033[34mNenhuma pessoa cadastrada!\033[m')
            return 0
        else:
            return str(check)
        
        
def checkInt(txt):
    while True:
        try:
            check = int(input(txt))
        except ValueError or TypeError:
            print('\033[31mERRO! Digite apenas NÚMEROS INTEIROS para a idade!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[34mNenhuma idade cadastrada!\033[m')
            return 0
        else:
            return int(check)

def checkAsk(txt):
    while True:
        try:
            check = int(input(txt))
        except ValueError or TypeError:
            print('\033[31mERRO! Digite apenas NÚMEROS INTEIROS!\033[m')
        except KeyboardInterrupt:
            print('Até logo!')
        else:
            if 1 <= check <= nMenu:
                return check
            else:
                print('\033[31mERRO! Não existe esta opção!\033[m')
                continue


# Code
nMenu = 0
def menu(lista):
    global nMenu
    for n, o in enumerate(lista):
        nMenu += 1
        print(f'{br(f"[{n+1}] {o}")}')
    opc = checkAsk('')
    return opc


file = 'data.py'
pessoas = []
dado = []
def lista(file): # Lista
        color(7)
        print('-' * 50)
        print(f"{'Nome':^30} {'Idade':>10}")
        openFile(file)
        print('-' * 50, end='')
        ccolor()
        sleep(2)


def adic(): # Adicionar
        cont = 1
        print(rd('[0 para cancelar]'))
        while True:
            name = checkStr(br(f'Nome da {cont}ª pessoa: '))
            if name == 0:
                break
            elif name in '0':
                break
            else:
                dado.append(name)
            age = checkInt(br('Idade: '))
            if age == 0:
                print(gn('Reiniciando a coleta de dados...'))
                sleep(1)
                dado.clear()
                continue
            else:
                dado.append(age)
            register(name, age)
            cont += 1
        print('-' * 50)
        