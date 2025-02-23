#laws_razors_etc.py

from pathlib import Path
import random

FILE_PATH = Path("LawsRazorsEtc.txt")

def get_dict() -> dict:
    '''Reads the given file, then returns a dictionary containing all interesting claims and principles'''
    with open(FILE_PATH, 'r') as the_file:
        lines = the_file.read().split('\n\n')

        laws_dict = {}

        for line in lines:
            parts = line.split(': ')
            key = parts[0]
            value = parts[1]
            laws_dict.update({key: value})

    return laws_dict

def random_law(laws_dict: dict) -> str:
    '''Returns a law at random from the dictionary'''
    key = random.choice(list(laws_dict.keys()))
    return laws_dict[key]

def random_laws(laws_dict: dict, n: int) -> str:
    '''Returns n laws at random with labels from the dictionary'''
    keys = random.choices(list(laws_dict.keys()), k=n)
    return {key: laws_dict[key] for key in keys}


if __name__ == '__main__':
    d = get_dict()
