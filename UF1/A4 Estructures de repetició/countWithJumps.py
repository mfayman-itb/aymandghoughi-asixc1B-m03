"""
descripción: L'usuari introdueix dos valors enters, el final i el salt
Escriu tots els números des de l'1 fins al final, amb una distància de salt
"""
num1 = int(input())
count = int(input())

for i in range(1, num1 + 1, count):
    print(i, end=" ")
