"""
25/10/2023
Ayman Dghoughi Nouri
M03 UF1 A3
Descripció: Demanar un enter a l'usuari que indica el número de
més i retorna el nombre de dies del mes.
"""

month = int(input())

if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    print("31")
elif month == 4 or 6 or 9 or 11:
    print("30")
elif month == 2:
    print("28 o 29")
