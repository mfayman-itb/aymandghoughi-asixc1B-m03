"""
Eric González, Izan Fernandez , Ayman Dghoughi
08/11/2023
M03 UF1 A3
Descripció: Programa que detecta si tres números demanats han estat introduïts en ordre creixent.
"""

nums = str(input("Introdueix una serie de 3 numeros:")).split()

if nums[1] > nums[0] and nums[1] < nums[2]:
    print("Els numeros estan en ordre creixent")
else:
    print("Els numeros NO estan en ordre creixent")