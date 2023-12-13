"""
descripción: Crea una aplicació que permet endevinar un número.
"""
import random
num = random.randint(1, 100)
intentos = 0
mynum = ""

while mynum != num and intentos < 10:
    mynum = int(input("Introduce el numero ganador: "))
    intentos += 1
    if mynum < num:
        print("Mas grande chavalin\n")
    elif mynum > num:
        print("Mas pequeño chavalin\n")
if mynum == num:
    print("God diiiid")
else:
    print(f"No lo adivinaste con {intentos} intentos perdedor")
print(f"El numero generado por mi bro es {num} y has usado {intentos} intentos para adivinarlo.")