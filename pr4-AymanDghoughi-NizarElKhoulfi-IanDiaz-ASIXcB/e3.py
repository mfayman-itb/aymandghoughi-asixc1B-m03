""""
Ayman Dghoughi, Ian Díaz, Nizar ElKhoulfi
30/11/2023
M03 UF1 pp4
Descripció: Programa que mostra per pantalla la suma de tots els nombres
senars i de tots els nombres parells inferiors a un número límit.
"""

try:
    num = int(input("Donam un límit: "))
    sumaParells = 0
    sumaSenars = 0
    for i in range(num):
        if i % 2 == 0:
            sumaParells += i
        else:
            sumaSenars += i
    print("La suma dels nombres parells es: " + str(sumaParells))
    print("La suma dels nombres senars es: " + str(sumaSenars))
except Exception as e:
    if ValueError:
        print("Si us plau, introdueix només nombres enters.")
    else:
        print(e)
