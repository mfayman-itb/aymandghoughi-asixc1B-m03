'''
Ayman Dghoughi, Nizar El Khoulfi, Ian Diaz
11/10/23
ASIXc M03 UF1 A2
Descripció: Programa que llegeixi l'edat de l'usuari i mostri si té edat per treballar
'''

try:
    edat = int(input("Quina edat tens? "))

    if edat >= 16 and edat <= 65:
        print("Apte per treballar")
    else:
        print("No apte per treballar")

except Exception as e:
    print(e)
    exit(1)