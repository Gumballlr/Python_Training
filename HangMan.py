#HangManGAME

import random
from words import words
import string


#random choice 
def get_valid_word(words):
    #word = the word to random dot choice word
    word =random.choice(words)
    #while = guess 1 word correctly
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()

#Set are used to store multiple items in a single variable
def hangman():
    word = get_valid_word(words)
    #separate
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    #what the user has guessed 
    used_letters = set() 
    while len(word_letters) >0:
        # ' 'join(['a', 'b', 'cd']) ---> 'a b cd'
        print('you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that character. Please try again!')
        else:
            print('Please try again!')
    print(f'You guessed the word, {word}')
hangman()