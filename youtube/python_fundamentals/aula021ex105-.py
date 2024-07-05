    # Escola Henrique Swachneguer #
# Functions
def name(checkName):
    nameOk = input(checkName).lower().capitalize()
    while not nameOk.isalpha():
        print('ERRO! Digite apenas letras para o nome do aluno(a)!')
        nameOk = input(checkName)
    nameOk = str(nameOk)
    return nameOk


def grade(checkGrade):
    notaOk = input(checkGrade)
    while not notaOk.isnumeric():
        print('ERRO! Digite apenas números!')
        notaOk = input(checkGrade)
    notaOk = int(notaOk)
    return notaOk


def ask(checkAsk):
    askOk = input(checkAsk).lower()
    while not askOk.isalpha():
        print('ERRO! Digite SIM ou NÃO!')
        askOk = input(checkAsk).lower()
    askOk = str(askOk)
    return askOk
    

def notas(nota):
    global dadoNota
    dadoNota.append(nota)
    

# Code
dadoNota = []
while True:
    while True:
        nome = name('Nome: ')
        nota = grade(f'Nota de {nome}: ')
        print('-' * 30)
        correto = ask(f'Estudante: {nome}\nNota: {nota}\nAs informações estão corretas? [SIM ou NÃO] ')
        if correto in 'sn':
            if correto in 's':
                break
    notas(nota)
    continuar = ask('Deseja adicionar mais alunos? ')
    if continuar in 'sn':
        if continuar in 'n':
            break
dados = {"Quantidade de notas":len(dadoNota),
         "Maior nota":max(dadoNota),
         "Menor nota":min(dadoNota),
         "Média das notas":(sum(dadoNota) / len(dadoNota))
        }
for k, v in dados.items():
    print(f'{k}: {v}')
    