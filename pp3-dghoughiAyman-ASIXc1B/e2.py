"""
Ayman Dghoughi Nouri
01/02/2024
pp3
Descrició: Programa que demana el nombre de files i columnes d'una matriu i comprova si es quadrada i que la seva mida sigui parella. També la mostra per pantalla.
"""
try:
    numFC = input().split()
    x = int(numFC[0])
    y = int(numFC[1])
    if x != y or x % 2 != 0 and y % 2 != 0:
        print("Mida de la matriu incorrecta. Cal posar només números parells")
    else:
        mida = int(numFC[0])
    matrix = [[0] * mida for i in range(mida)]
    for fila in range(mida):
       for columna in range(mida):
           if fila == 0 or fila == mida -1:
               matrix[fila][columna] = 1
           elif columna == 0 or columna == mida -1:
               matrix[fila][columna] = 1
           else:
               matrix[fila][columna] = 0
    for fila in matrix:
       print(' '.join([str(elem) for elem in fila]))
except Exception as e:
    print(e)
