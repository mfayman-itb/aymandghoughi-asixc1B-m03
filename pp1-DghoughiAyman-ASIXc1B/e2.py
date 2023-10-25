"""
19/10/2023
Ayman Dghoughi Nouri
ASIXcB
M03 pp1
Descripció: Programa que calcula la nota final de la UF1 del mòdul 03 de 3 alumnes amb 2 decimals
"""

alumne1 = input("Nom del alumne: ")
alumne2 = input("Nom del alumne: ")
alumne3 = input("Nom del alumne: ")

RA1_a1 = float(input("Nota de RA1: "))
RA1_a2 = float(input("Nota de RA1: "))
RA1_a3 = float(input("Nota de RA1: "))

RA2_a1 = float(input("Nota de RA2: "))
RA2_a2 = float(input("Nota de RA2: "))
RA2_a3 = float(input("Nota de RA2: "))

QUF1a1 = (0.70 * RA1_a1) + (0.30 * RA2_a1)
QUF1a2 = (0.70 * RA1_a2) + (0.30 * RA2_a2)
QUF1a3 = (0.70 * RA1_a3) + (0.30 * RA2_a3)

print(f"La nota de la UF1 de {alumne1} es: {QUF1a1:.2f}")
print(f"La nota de la UF1 de {alumne2} es: {QUF1a2:.2f}")
print(f"La nota de la UF1 de {alumne3} es: {QUF1a3:.2f}")