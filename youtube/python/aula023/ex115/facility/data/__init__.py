import os

def checkFile(file):
    try:
        check = open(r'C:\Users\mhenr\OneDrive\Documentos\GitHub\Python-Curso_em_Video\Python\aula023\ex115\data.py', 'r')
        check.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
    
def createFile(file):
    try:
        create = open(r'C:\Users\mhenr\OneDrive\Documentos\GitHub\Python-Curso_em_Video\Python\aula023\ex115\data.py', 'w+')
        create.close()
    except:
        print('Erro!')
    
    
def openFile(file):
    try:
        abrir = open(r'C:\Users\mhenr\OneDrive\Documentos\GitHub\Python-Curso_em_Video\Python\aula023\ex115\data.py', 'rt')
    except:
        print('Erro!')
    else:
        for l in abrir:
            data = l.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30} {data[1]:>8}')


def register(name='', age=0):
    try:
        reg = open(r'C:\Users\mhenr\OneDrive\Documentos\GitHub\Python-Curso_em_Video\Python\aula023\ex115\data.py', 'at')
    except:
        print('Erro ao abrir data.py para cadastro!')
    else:
        try:
            reg.write(f'{name};{age}\n')
        except:
            print('Erro ao cadastrar!')
        else:
            print(f'\033[32mCadastro de [{name}] realizado com sucesso!\033[m')


def cleanData():
    try:
        os.remove(r'C:\Users\mhenr\OneDrive\Documentos\GitHub\Python-Curso_em_Video\Python\aula023\ex115\data.py')
    except:
        print('Erro ao abrir o arquivo para limpá-lo!')
    else:
        print('\033[32mLista limpada com sucesso!\033[m')
        print('-' * 50)
