""""
Ayman Dghoughi, Ian Díaz, Nizar ElKhoulfi
30/11/2023
M03 UF1 pp4
Descripció: Programa que imprimeix un tauler d’escacs per pantalla. Un taulell
d’escacs comença amb la casella  Blanca i és de mida 8x8 sempre.
"""

BLANC = "██"
NEGRE = "  "
for i in range(1, 9):
    print(i, end=" ")
    for j in range(1, 9):
        if (i + j) % 2 == 0:
            print(BLANC, end="")
        else:
            print(NEGRE, end="")
        print(" ", end="")
    print()
print("   " + "a  b  c  d  e  f  g  h")
