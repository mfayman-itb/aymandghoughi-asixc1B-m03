"""
descripción: te dice que pizza tienes que comprarte dependiendo de cuaal es mas grande.
"""
num = input("Dame el Diametro de la pizza y los lados de la otra pizza: ").split()
import math

radio = (int(num[0]) / 2)
areaC = (radio * radio) * math.pi
areaR = int(num[1]) * int(num[2])

if areaC > areaR:
    print("Compra la circular")
else:
    print("Compra la rectangular")
