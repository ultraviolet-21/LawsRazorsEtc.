#answers_to_paradoxes.py

import laws_razors_etc as lr
from pathlib import Path


def questions(laws_dict: dict) -> dict:
    '''Returns all questions from the dictionary'''
    return {key: laws_dict[key] for key in laws_dict if '?' in laws_dict[key]}

def answer_questions(laws_dict: dict):
    '''Asks the user to answer all the questions'''
    try:
        with open('answers.txt', 'w') as f: #replace with your chosen file
            for key in questions(laws_dict):
                answer = input(key + ': ' + laws_dict[key])
                f.write(answer + '\n')
    except FileNotFoundError:
        print('FILE NOT FOUND')

if __name__ == '__main__':
    d = lr.get_dict()
