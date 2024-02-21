"""
Eric González, Izan Fernandez , Ayman Dghoughi
08/11/2023
M03 UF1 A3
Descripció: Programa que calcula la velocitat instantània i la velocitat mitjana.
"""

vinicial = float(input("Introdueix la velocitat inicial en m/s: "))
acc = float(input("Introdueix l'acceleració en m/s²: "))
temps = float(input("Introdueix el temps en s: "))

vinst = (vinicial + acc) * temps
print(vinst)

if vinst <= 0:
    print("Esta parat i no puc calcular la mitjana")
else:
    vmitj = (vinicial + vinst) / 2
    print("La velocitat mitjana es", vmitj)