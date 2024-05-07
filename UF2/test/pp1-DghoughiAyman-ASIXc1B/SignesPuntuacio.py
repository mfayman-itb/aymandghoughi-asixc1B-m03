"""
4/04/2024
Ayman Dghoughi Nouri
ASIXcB
M03 UF2 pp1
Descripció: bloc de definicións de signes de puntuació.
"""

#region defs
def netejar_frase():
    phrase = input().lower()
    lenght = len(phrase)
    phrase_no_signs = ''.join(caracter for caracter in phrase if caracter.isalnum() or caracter.isspace())
    lenght_clean = len(phrase_no_signs)
    return lenght_clean, lenght


def quantitat(lenght_clean, lenght):
    return print(f"De {lenght} caràcteres {lenght_clean} són lletres.")

def posició(phrase_no_signs):
    unique_words = set(phrase_no_signs)
    for i in unique_words:
        print(f'{i}: {phrase_no_signs.count(i)}')
#enregion
