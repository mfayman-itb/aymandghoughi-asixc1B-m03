"""
descripción: programa que demani per teclat dos números i a
continuació imprimeixi tots els nombres parells entre tots dos.
"""
limI = int(input("Introcuce el limite inferior: "))
limS = int(input("Introduce el limite superior: "))

for i in range(limI, limS):
    if i % 2 == 0:
        print(i, end=" ")
