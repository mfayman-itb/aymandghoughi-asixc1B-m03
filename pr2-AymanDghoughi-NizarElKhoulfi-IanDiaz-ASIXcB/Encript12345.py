'''
Ayman Dghoughi, Nizar El Khoulfi, Ian Diaz
11/10/23
ASIXc M03 UF1 A2
Descripció: Programa que llegeixi l'edat de l'usuari i mostri si té edat per treballar.
'''

try:
    import re

    word = str(input("Tell me a word: "))
    if re.match("^[a-zA-Z]+$", word):
        word = word.replace("a", "1").replace("A", "1").replace("e",
        "2").replace("E","2").replace("i", "3").replace("I",
        "3").replace("o", "4").replace("O","4").replace("u",
        "5").replace("U", "5")
        print(word)
    else:
        print("L'entrada conté caràcters no alfabètics.")

except Exception as e:
    print(e)
    exit(1)