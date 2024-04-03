import re
from unidecode import unidecode
import string
import random
ALLOWED = string.ascii_letters

def check_input(text, option):
    if option != 2 or option != 4:
        if not text or len(str(text)) <= 3:
            print("Text is empty or too short.")
            exit(1)
        else:
            return str(text)
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

def crazy_words(words):
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

def es_palindrom():
    palindrom = input().lower()
    pal = re.sub(r'[^a-z0-9]', '', unidecode(palindrom))
    revrs = pal[::-1]

    if revrs == pal:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

def xifratge_cesar(texto, desplazamiento):
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():  # Verificar si el carácter es una letra
            if char.islower():  # Para letras minúsculas
                nuevo_ascii = (ord(char) - 97 + desplazamiento) % 26 + 97
            elif char.isupper():  # Para letras mayúsculas
                nuevo_ascii = (ord(char) - 65 + desplazamiento) % 26 + 65
            texto_cifrado += chr(nuevo_ascii)
        else:
            texto_cifrado += char
    return texto_cifrado
