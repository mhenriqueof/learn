        # Sistema de Cadastro #
# Modules
from facility.estilos import *
from facility.recursos import *
from facility.data import *
from time import sleep
    # Code #
# Check file

# Banner
color(43)
hyphens("Voluntários do Fazer o Bem Sem Olhar a Quem")
ccolor()
# Data
while True:
    file = 'data.py'
    if not checkFile(file):
        createFile(file)
    ask = menu(['Mostrar os voluntários',
                'Adicionar mais voluntários',
                'Limpar lista',
                'Sair'])
    if ask == 1: # List
        lista(file)
    elif ask == 2: # Add
        adic()
    elif ask == 3: # Limpar lista
        cleanData()
    else: # Sair
        print('Até logo!')
        break
