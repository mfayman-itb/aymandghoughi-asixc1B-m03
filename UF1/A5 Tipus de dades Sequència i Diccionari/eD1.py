# Escriu un programa que demani un número per teclat i que creï un diccionari les claus del qual vagin des del número 1 fins al número indicat, i els valors siguin els quadrats de les claus.
import math
num = int(input())
x = 1
dicc = {x:x*x for x in range(num)}
print(dicc)