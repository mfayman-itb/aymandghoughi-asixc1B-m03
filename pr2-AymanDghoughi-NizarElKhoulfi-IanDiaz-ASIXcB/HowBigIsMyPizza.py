'''
Ayman Dghoughi, Nizar El Khoulfi, Ian Diaz
11/10/23
ASIXc M03 UF1 A2
Descripció: Programa per calcular la superfície d'una pizza a partir del diàmetre
'''

try:
    import math

    diàmetre = float(input("Introdueix el diàmetre de la pizza en centímetres...\t"))

    superfície = math.pi * (diàmetre**2 / 4)

    print(f"\nLa superficie de la pizza es: {superfície:.2f}cm")

except Exception as e:
    print(e)
    exit(1)