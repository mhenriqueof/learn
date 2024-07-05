    # Escola Henrique Swachneguer #
# Modules
from random import randint as r
# Functions
def name(checkName):
    nameOk = input(checkName).lower().capitalize()
    while not nameOk.isalpha():
        print('ERRO! Digite apenas letras para o nome do aluno(a)!')
        nameOk = input(checkName)
    nameOk = str(nameOk)
    return nameOk
    
    
def ask(checkAsk):
    askOk = input(checkAsk).lower()
    while not askOk.isalpha():
        print('ERRO! Digite SIM ou NÃO!')
        askOk = input(checkAsk).lower()
    askOk = str(askOk)
    return askOk


def notas(*num, situ='n'):
    """
    Analisar notas de vários estudantes
        param n: as notas do aluno;
        param situ: mostrar ou não a situação;
        return: retornar o dicionário com as informações obtidas.
    """
    ficha = {}
    ficha["Quantidade de notas"] = len(num)
    ficha["Maior nota"] = max(num)
    ficha["Menor nota"] = min(num)
    ficha["Média das notas"] = (sum(num) / len(num))
    if situ in 's':
        if ficha["Média das notas"] >= 7:
            ficha["Situação"] = 'Bom'
        elif ficha["Média das notas"] < 5:
            ficha["Situação"] = 'Ruim'
        else:
            ficha["Situação"] = 'Razoável'
    return ficha

# Code
dadosNota = []
nome = name('Nome: ')
pergunta = ask(f'Mostrar a situação de {nome}? SIM ou NÃO ')
if pergunta[0] in 's':
    pão = 's'
else:
    pão = 'n'
aluno = notas(r(0,10), r(0,10), r(0,10), r(0,10), situ=pão)
print(aluno)
print('-' * 30)
print(f'{nome.capitalize()} Silva Pereira dos Santos Gomes de Oliveira: ')
for k, v in aluno.items():
    print(f'    {k}: {v}')
