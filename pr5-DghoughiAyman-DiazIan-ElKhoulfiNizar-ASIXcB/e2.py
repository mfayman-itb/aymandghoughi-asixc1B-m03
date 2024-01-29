"""
24/01/2024
Ayman Dghoughi, Nizar El Khoulfi, Ian Díaz
ASIXcB e2 UF1
Programa que generi una llista de 100 nombres aleatoris entre 1 i 50. Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.
"""

import random

LIMITINF, LIMITSUP = 1, 50
lista = [random.randint(LIMITINF, LIMITSUP) for i in range(100)]
totalParells, totalSenars = 0

for i in range(len(lista)):
    if i % 2 == 0:
        totalParells += lista[i]
    else:
        totalSenars += lista[i]

mitjanaParells = totalParells / (len(lista) / 2)
mitjanaSenars = totalSenars / (len(lista) / 2)
print(f'Mitjana de les posicions parelles: {mitjanaParells}\nMitjana de les posicions senars: {mitjanaSenars}')