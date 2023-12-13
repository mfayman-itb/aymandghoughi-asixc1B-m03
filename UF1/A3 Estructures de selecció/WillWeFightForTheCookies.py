"""
25/10/2023
Ayman Dghoughi
M03 UF1 A3
Descripció: si hay la misma cantidad de galletas para todos dice lets eat si no lets fight
"""

situation = input()

peopleCookie = situation.split()
calculo = int(peopleCookie[0]) % int(peopleCookie[1])
if calculo == 0:
    print("Let's eat")
else:
    print("Let's fight")