import random

def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < randomNumber:
            print('Guess again, too low.')
        elif guess > randomNumber:
            print('Guess again, too high.')
    print('Wooohooo! Congrats! You have guessed the number!')
guess (10)