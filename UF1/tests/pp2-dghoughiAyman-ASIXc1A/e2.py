"""
14/12/2023
Ayman Dghoughi Nouri
ASIXcB
M03 pp2
Descripció: Programa que indica quantes vegades apareix una lletra dins s'una frase.
"""
letter = input()
cadena = input()
i = 0
count = 0
length = len(cadena)

while i != length:
    if letter in cadena[i]:
        count += 1
    i += 1
print(f"La frase '{cadena}' té {count} lletres {letter}")
