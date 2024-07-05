import guessing
import hangman

print('-' * 30)
print('Games'.center(30))
print('-' * 30)

game = int(input('[1] Forca [2] Adivinhação\n'))

if game == 1:
    hangman.play()
elif game == 2:
    guessing.play()
    