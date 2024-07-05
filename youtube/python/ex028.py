import random

usuario = int(input('Choose a number between 0 e 5: '))
num = random.randint(0,5)

print(f'The chosen number is {num}.')
if usuario == num:
    print('Congratulations! You chose the right number!')
else:
    print('Uncongratulations! You did not choose the right number.')
print('Thank you for playing my first game.')
