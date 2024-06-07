import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low')
        if guess > random_number:
            print('Sorry, guess again. Too high')
    print('You right')   
guess(10)


def computer_guess(x):
    low = 1
    high = x
    comment = ''
    while comment != 'c':
        if low != high:
            guess= random.randint(low,high)
        else:
            guess = low
            print(f' I guessed your number, it is {guess}')
        comment = input (f' Is number {guess} is high -H- or low -L- or Correct -C-')
        if comment =='h':
            high = guess -1
        elif comment == 'l':
            low = guess+1 
        if low > high:
            print('You wrong')
    print(f'cpu guessed your number  = {guess}')
computer_guess(20)
