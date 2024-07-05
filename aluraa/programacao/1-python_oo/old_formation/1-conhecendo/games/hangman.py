def play():
    print('=' * 30)
    print('Hangman'.center(30))
    print('=' * 30)
    
    secret_word = 'pao'
    secret = []
    
    hanged = False
    correct = False
    
    for n in enumerate(secret_word):
        secret.append(' ')
        
    while not (hanged or correct):
        
        for word in secret:
            print(f'\033[4m{word}\033[m', end=' ')
        print()
            
        guess = str(input('Letter: ')).lower().strip()
        
        for pos, letter in enumerate(secret_word):
            if guess == letter:
                secret[pos] = letter
        
    
if __name__ in '__main__':
    play()
    
lista = [0,1,3]
print( min(lista))
