""""
Ayman Dghoughi, Ian Díaz, Nizar ElK
30/11/2023
M03 UF1 pp4
Descripció: Programa que mostra un triangle amb nombres a les cantonades.
"""

try:
    alçada = int(input("Donam una alçada entre el 2 i el 9: "))
    if alçada >= 2 and alçada <= 9:
        for i in range(1, alçada + 1):
            for j in range(1, i + 1):
                if i == alçada:
                    print(str(i) * alçada)
                    break
                elif j == 1 or i == j:
                    print(i, end="")
                else:
                    print(" ", end="")
            print()
except Exception as e:
    if ValueError:
        print("Si us plau, introdueix una alçada entre el 2 i el 9.")
    else:
        print(e)



