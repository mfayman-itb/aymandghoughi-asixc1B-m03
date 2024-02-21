"""
Eric González, Izan Fernandez , Ayman Dghoughi
08/11/2023
M03 UF1 A3
Descripció: Programa que demana dos números si el primer és més gran o igual que
el segon els intercanvia i torna a mostrar els valors per pantalla.
"""

num1 = int(input("Introueix el primer numero: "))
num2 = int(input("Introueix el segon numero: "))

if num1 >= num2:
    num1 , num2 = num2 , num1
    print(num1)
    print(num2)
else:
    print("EL primer nombre no es mes gran ni igual que el segon")