"""
descripción: programa comprovarà si es tracta d’una vocal.
Si ho és, escriurà en pantalla ‘VOCAL’. En cas contrari, ‘NO VOCAL’
"""
vow = ""
vowels = "aeiou"
while vow != " ":
    vow = input("Write only one char: ")
    if len(vow) > 1:
        print("Error escribe solo una letra.")
    else:
        if vow in vowels:
            print("vowel")
        elif vow == " ":
            print("leaving...")
        else:
            print("no vowel")
