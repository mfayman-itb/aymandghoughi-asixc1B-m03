"""
15/11/2023
Ayman Dghoughi Nouri
M03 UF1 A4
Descripció: IsPinOk
"""
x = 1
PIN = 1234
EASTER_EGG = "0007"

clave = input("Dime la clave: ")
while int(clave) != PIN and clave != EASTER_EGG and x != 3:
    print("Clave incorrecta")
    clave = input("Dime la clave: ")
    x += 1
if x == 3:
    print("Intents esgotats: LAS CAGAO BACALAO")
elif int(clave) == PIN:
    print("PIN correcte has fet servir " + str(x) + " intents")
elif clave == EASTER_EGG:
    print("EASTER EGG correcte has fet servir " + str(x) + " intents")
