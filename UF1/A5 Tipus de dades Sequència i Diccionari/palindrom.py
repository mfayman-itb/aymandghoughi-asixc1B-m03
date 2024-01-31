from unidecode import unidecode
palindrom = input().lower()
pal = palindrom.replace(" ","")
pal = list(unidecode(pal))
revrs = pal[::-1]
if revrs == pal:
    print("es un palindrom")
else:
    print("no es un palindrom")