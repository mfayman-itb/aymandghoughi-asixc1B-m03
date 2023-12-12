import random

num = int(input("Piensa en un numero del 1 al 100: "))
urnum = random.randint(1, 101)
intentos = 0

while urnum != num and intentos < 10:
    intentos += 1
    mas = input(f"Es mas grande que {urnum}?\n").lower()
    if mas == "si":
        urnum = random.randint(urnum + 1, 100)
    if mas == "no":
        urnum = random.randint(1, urnum - 1)
if urnum == num:
    print("God diiiid")
else:
    print(f"No lo adivinaste con {intentos} intentos perdedor")
print(f"El numero generado por mi bro es {num} y has usado {intentos} intentos para adivinarlo.")

