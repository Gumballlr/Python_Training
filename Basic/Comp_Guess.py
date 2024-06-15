import random

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
