    # Mensagem com tamanho adaptável #
# Functions
def mensagem(msg):
    cont = len(msg)
    print('-' * (cont + 4))
    print(f'  {msg}')
    print('-' * (cont + 4))

    
# Code
mensagem(str(input('')))

'''
    # Mensagem com tamanho adaptável #
# Functions
def mensagem(msg):
    cont = len(msg) + 4
    print('-' * (cont))
    print(f'{msg:^{cont}}')
    print('-' * (cont))

    
# Code
mensagem(str(input('')))
'''

'''
    # Mensagem com tamanho adaptável #
# Functions
def mensagem(msg):
    cont = len(msg) + 4
    print('-' * (cont))
    print(msg.center(cont))
    print('-' * (cont))

    
# Code
mensagem(str(input('')))
'''