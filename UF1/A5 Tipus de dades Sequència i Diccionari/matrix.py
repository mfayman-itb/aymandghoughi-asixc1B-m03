MIDA = 4
matrix = [[0] * MIDA for i in range(MIDA)]
print(matrix)    #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for fila in range(MIDA):
   for columna in range(MIDA):
       if fila < columna:
           matrix[fila][columna] = 0
       elif fila > columna:
           matrix[fila][columna] = 2
       else:
           matrix[fila][columna] = 1
for fila in matrix:
   print(' '.join([str(elem) for elem in fila]))
