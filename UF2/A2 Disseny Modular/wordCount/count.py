def get_phrase():
    phrase = input().lower()
    phrase_no_signs = ''.join(caracter for caracter in phrase if caracter.isalnum() or caracter.isspace())
    return phrase_no_signs.split()

def count_cleanWords(phrase_no_signs):
    unique_words = set(phrase_no_signs) # set elimina los duplicados
    for i in unique_words:
        print(f'{i}: {phrase_no_signs.count(i)}')
