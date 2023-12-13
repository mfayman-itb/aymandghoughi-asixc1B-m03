"""
descripción: Per exemple les xifres del nombre 456 sumen (4+5+6) = 15
"""
num = input()
i = 0
suma = 0
length = len(num)

while(i != length):
   suma += int(num[i])
   i += 1
print(suma)