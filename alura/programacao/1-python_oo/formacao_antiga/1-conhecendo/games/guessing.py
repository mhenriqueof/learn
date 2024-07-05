def play():
    print('=' * 30)
    print('Guessing Game'.center(30))
    print('=' * 30)
    
    # Modules
    from random import randint
    # Variables
    guessing = randint(1, 100)
    attempts = 1
    score = 1000
    # Difficulty
    print('[1] Easy [2] Normal [3] Hard')

    difficulty = int(input('Difficulty: '))
    if difficulty == 1:
        attempts = 20
    elif difficulty == 2:
        attempts = 10
    else:
        attempts = 5
    # Game
    for attempt in range(1, attempts+1):
        try:
            print(f"Attempt {attempt} of {attempts}")
            while True:
                number = int(input("Which number am I thinking? "))
                if not 1 <= number <= 100:
                    print("Try a number between 1 and 100!")
                    continue
                break
        except:
            print('Invalid number.')
        else:
            print('-' * 30)
            correct = number == guessing
            up      = number > guessing
            if correct:
                print(f"You're correct! Score: {score}")
                break
            else:
                if up:
                    print("You're wrong! Low!")
                    if attempt == attempts:
                        print(f'The secret number was: {guessing}')
                else:
                    print("You're wrong! Up!")
                    if attempt == attempts:
                        print(f'The secret number was: {guessing}')
                lost_points = abs(guessing - number)
                score -= lost_points
            print('-' * 30)
            
            
if __name__ in "__main__":
    play()
    