import random
import string
from unidecode import unidecode
ALLOWED = string.ascii_letters

def get_input():
    text = input("Introduce texto: ")
    return text
def check_input(text, option):
    if option == "crazywords":
        if not text or len(str(text)) <= 3:
            print("Text is empty or too short.")
            exit(1)
        else:
            return str(text)
    elif option == "palindromo":
        if not text or len(str(text)) < 3:
            print("Text is empty or too short.")
            exit(1)
        else:
            return str(text)

def fix_punctuation(text):
    try:
        words = []
        current_word = ''
        for char in text:
            if char in ALLOWED:
                current_word += char
            else:
                if current_word:
                    words.append(current_word)
                    current_word = ''
                words.append(char)
        if current_word:
            words.append(current_word)
    except Exception as e:
        print(e)
    return words

def disorder_words(words):
    try:
        disorder_text = []
        for word in words:
            if len(word) <= 3 or not any(char in ALLOWED for char in word[1:-1]):
                disorder_text.append(word)
            else:
                first_letter = word[0]
                last_letter = word[-1]
                middle_letters = list(word[1:-1])
                random.shuffle(middle_letters)
                disorder_word = first_letter + ''.join(middle_letters) + last_letter
                disorder_text.append(disorder_word)
    except Exception as e:
        print(e)
    return ''.join(disorder_text)

def palindrom(text):
    especiales = '!\"#$%&\'()*+,-./:;<=>?[]^_'
    frase = text.lower()
    cleanstr = frase.replace(" ", "")
    for character in cleanstr:
        for special in especiales:
            if character == special:
                cleanstr.replace(character, "")
    clean = list(unidecode(cleanstr))
    rev = clean[::-1]
    if rev == clean:
        result = f"{frase} es palíndromo"
    else:
        result = f"{frase} NO es palíndromo"
    return result
def caesarCipher():
    shift = 0
    result = ""
    text = input("Introduce texto a encriptar: ")
    while shift < 1 or shift > 25:
        shift = int(input("Introduce el shift (1-25): "))
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        if char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
    print(f"Texto encriptado: ", end="")
    return result