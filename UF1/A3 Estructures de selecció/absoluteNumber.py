"""
descripción: Mostrar el valor absolut d'un enter entrat per l'usuari.
"""
num = int(input("Give me a negative num: "))

if num < 0:
    integer = num * (-1)
    print(integer)
else:
    print(num)
