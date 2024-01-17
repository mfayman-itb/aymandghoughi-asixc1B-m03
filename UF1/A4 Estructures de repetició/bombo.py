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