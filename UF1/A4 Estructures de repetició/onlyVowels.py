"""
descripción: Donada una llista de lletres, imprimeix únicament les vocals que hi hagi.
"""
num = int(input())
letter = input().split()
length = len(letter)
i = 0

while(i != length and num == length):
   if letter[i] in ["a","e","i","o","u"]:
       print(letter[i], end=" ")
   i += 1