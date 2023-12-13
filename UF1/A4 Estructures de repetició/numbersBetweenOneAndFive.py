"""
descripción: Demanar a l'usuari un enter entre 1 i 5.
"""
num = int(input())

while(not (num >= 1 and num <= 5)):
   num = int(input())
print("El número introduït: ", num)