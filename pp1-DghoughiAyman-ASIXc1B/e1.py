"""
19/10/2023
Ayman Dghoughi Nouri
ASIXcB
M03 pp1
Descripció: Programa que calcula la diagonal d'un camp donada l'alçada i l'amplada
"""

try:
    import math

    amplada = float(input("Introdueix l'amplada del camp en metres: "))
    alçada = float(input("Introdueix l'alçada del camp en metres: "))

    sumaPotencies = float(amplada**2 + alçada**2)
    diagonal = math.sqrt(sumaPotencies)

    print(f"El valor de la diagonal del camp es de {diagonal}m")

except Exception as e:
    print(e)