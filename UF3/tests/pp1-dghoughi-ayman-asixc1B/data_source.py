"""
09/05/2024
Ayman Dghoughi Nouri
ASIXcB
M03 UF3 pp1
Descripció: get data
"""

import os
from logger import *

inputFIle = os.path.join('.', 'paraules.txt')
allWords = []

def get_data_from_file():
    if os.path.exists(inputFIle):
        with open(inputFIle, 'r') as file:
            text = file.read().split()
    else:
        print(f'File "{file}" not found.')
        logger('error', f'File {file} not found.')
        exit(1)
    logger('info', 'Succesfully loaded the data.')
    return text
