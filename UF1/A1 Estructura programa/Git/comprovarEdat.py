"""
Ayman Dghoughi Nouri
21/09/2023
ASIXc M03 UF1 A1
Descripció: Programa que demana l'edat i diu si ets major d'edat.
"""
try:
    edat = int(input("Quina edat tens? "))
    if edat >= 18:
        print("Ets MAJOR d'edat")
    else:
        print("Ets MENOR d'edat")
    print("Programa finalitzat")
except ValueError:
    print("ERROR: Valor no valid")
