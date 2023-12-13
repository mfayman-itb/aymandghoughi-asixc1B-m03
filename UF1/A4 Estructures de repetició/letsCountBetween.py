"""
descripción: Mostrar per pantalla tots els valors que hi ha entre els dos valors introduïts ordenats de menor a major.
"""
num1 = int(input())
num2 = int(input())

for i in range(num1 + 1, num2):
    print(i, end=" ")