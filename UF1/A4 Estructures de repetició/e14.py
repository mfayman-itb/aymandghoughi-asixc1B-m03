"""
descripción: programa per determinar a quin quilòmetre d'aquesta carretera es trobaran.
"""
vel = float(input("A que velocidad van los coches en km/h: "))
pos1 = 70
pos2 = 180
distT = pos2 - pos1
posR = distT / (2 * vel)
print(posR)