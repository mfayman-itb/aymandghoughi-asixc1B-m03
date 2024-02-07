TORRE = "♖"
POS_TORRE = "♜"
MIDA = 8
try:
    move = input().split()
    x = int(move[0])
    y = int(move[1])

    for columna in range(MIDA):
        for fila in range(MIDA):
            if columna == y and fila == x:
                print(end=TORRE)
            elif columna == y or fila == x:
                print(end=POS_TORRE)
            else:
                print(end='x')
            if fila == 7: print(end="\n")
            else: print(end=" ")
except Exception as e:
    print(e)