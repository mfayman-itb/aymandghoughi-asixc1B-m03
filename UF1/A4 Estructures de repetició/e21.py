"""
descripción: Crea una aplicació que permet endevinar un nombre aleatori pensat per un usuari.
"""
import random

num = int(input("Piensa en un numero del 1 al 100: "))
urnum = random.randint(1, 100)
intentos = 0
topB = 0
topA = 100
while urnum != num and intentos < 10:
    intentos += 1
    mas = input(f"Es mas grande que {urnum}?\n").lower()
    if mas == "si":
        topB = urnum
    if mas == "no":
        topA = urnum
    urnum = random.randint(topB + 1, topA - 1)
if urnum == num:
    print("God diiiid")
else:
    print(f"No lo adivinaste con {intentos} intentos perdedor")
print(f"El numero generado por mi bro es {num} y has usado {intentos} intentos para adivinarlo.")

