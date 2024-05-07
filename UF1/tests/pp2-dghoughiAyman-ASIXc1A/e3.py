"""
14/12/2023
Ayman Dghoughi Nouri
ASIXcB
M03 pp2
Descripció: Programa que marca al taulell d'escacs amb * les caselles a les quals
un alfiler pot moure dependent de la posicio donada a l'input.
"""
BLANC = "B "
NEGRE = "N "
for i in range(1, 9):
    for j in range(1, 9):
        if (i + j) % 2 == 0:
            print(BLANC, end="")
        else:
            print(NEGRE, end="")
        print(" ", end="")
    print()
