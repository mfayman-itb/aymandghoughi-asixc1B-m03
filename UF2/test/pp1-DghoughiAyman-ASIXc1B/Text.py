"""
4/04/2024
Ayman Dghoughi Nouri
ASIXcB
M03 UF2 pp1
Descripció: bloc de definicions d'encriptació i descodificació.
"""
#region Imports
import systemColors
#endregion

#region Constants
A = systemColors.CGREEN + "a"
E = systemColors.CBLUE + "e"
I = systemColors.CBEIGE + "i"
O = systemColors.CRED + "o"
U = systemColors.CYELLOW +"u"
#endregion

#region defs
def cesar_input():
    shift = 0
    text = input("Introduce texto a encriptar: ")
    while shift < 1 or shift > 25:
        shift = int(input("Introduce el shift (1-25): "))
    return text, shift

def cesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        if char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
    print(f"Texto encriptado: ", end="")
    return result

def text_codificar():
    text = input().lower()
    #for i in text:
        #if i in VOWELS:
            #i = A
#enregion