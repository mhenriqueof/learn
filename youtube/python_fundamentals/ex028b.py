from random import randint as sorteio
from time import sleep as espera

print("Hi! Let's play a game?!")
usuario = int(input('Which number between 0 e 5 am I thinking? '))
num = sorteio(0,5)

print("Wait a second! I'm thinking which one to choose...")
espera(4)

if usuario >= 6:
    print('Please, choose a number between 0 and 5.')
    print('Try again.')
else:
    print(f'You chose {usuario}, I chose {num}.')
if usuario == num:
    print('Congratulations! You won!')
else:
    print('"Uncongratulations". I won.')
print('Thank you for playing my first game!')
