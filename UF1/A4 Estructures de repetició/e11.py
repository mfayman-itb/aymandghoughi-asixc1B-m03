"""
descripción: Escriu un programa que digui si un número introduït per teclat és primer o no.
"""
num = int(input("Dime un numero: "))
primo = True

if num < 2:
    primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

if primo:
    print("Número primo")
else:
    print("NO número primo")
