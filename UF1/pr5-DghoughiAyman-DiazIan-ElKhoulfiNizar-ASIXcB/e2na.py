'''
24/1/2024
Ayman Dghoughi, Nizar ElKhoulfi, Ian Díaz
Programa que calcula la suma dels dígits parells d'un número positiu.
'''

try:
    numero = input()
    digits = list(numero)
    sumadig = 0
    for digit in digits:
        if int(digit) % 2 == 0:
            sumadig += int(digit)
    print(sumadig)
except Exception as e:
    print(e)