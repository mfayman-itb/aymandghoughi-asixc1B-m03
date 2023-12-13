"""
descripción: L'usuari introdueix un enter (N) i es mostra per pantalla un compte enrere de N fins a 1.
"""
num = int(input())

for i in range(num, 0, -1):
    print(i, end=" ")
