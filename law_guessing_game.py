#law_guessing_game.py

import laws_razors_etc as lr
import random
from pathlib import Path

def guess_the_law(laws_dict: dict) -> bool:
    '''Returns True if the user guesses the law correctly and False otherwise'''
    key = random.choice(list(laws_dict.keys()))
    print(laws_dict[key])
    guess = input()
    if '\'' in guess:
        parts = guess.split('\'')
        key_parts = key.split('â€™')
        if parts[0].upper() == key_parts[0].upper() and parts[1].upper() == key_parts[1].upper():
            return True
        return False
    else:
        if guess.upper() == key.upper():
            return True
        return False

def guessing_game(laws_dict: dict, n: int) -> int:
    '''Asks user to guess n laws and returns the number of correct guesses'''
    score = 0
    for x in range(n):
        result = guess_the_law(laws_dict)
        if result == True:
            score += 1

    return score

if __name__ == '__main__':
    d = lr.get_dict()
    n = input("How many questions? ")
    guessing_game(d, n)
