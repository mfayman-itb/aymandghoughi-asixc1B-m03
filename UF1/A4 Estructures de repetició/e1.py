"""
descripción: Implementa un programa que demani un número i
calculi el seu factorial. Per exemple 5! = 1x2x3x4x5= 120)
"""
num = int(input("Give me a number: "))
m = 1

for i in range(1, num):
    m = m * (i + 1)
print(f"{num}! = {m}")
