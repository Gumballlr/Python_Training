import random
from words import words
import string


#random choice 
def get_valid_word(words):
    #word = the word to random dot choice word
    word =random.choice(words)
    #while = guess 1 word correctly
    while '' in word or '-' in word:
        word = random.choice(words)
    return word.upper()

valid_word = get_valid_word(words)
print(valid_word)