"""
Ayman Dghoughi Nouri
21/09/2023
ASIXc M03 UF1 A1
Descripció: Programa que demana l'edat i diu si ets major d'edat.
"""
try:
    age = int(input("How old are you? "))
    if age >= 18:
        print("You are of age")
    else:
        print("You are a minor")
    print("Program completed")
except Exception as e:
    print("ERROR: Invalid value")
    print(e)
    exit(1)