"""
09/05/2024
Ayman Dghoughi Nouri
ASIXcB
M03 UF3 pp1
Descripció: programa principal
"""

from logger import *
from data_source import *
from worder import *

def main():
    text = get_data_from_file()
    word_leght_2(text)
    word_leght_4(text)
    word_leght_6(text)
    word_leght_8(text)
    word_leght_10(text)

if __name__ == "__main__":
    main()