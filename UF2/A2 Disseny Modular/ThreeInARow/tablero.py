def inicializar_tablero():
    return [['·', '·', '·'],
            ['·', '·', '·'],
            ['·', '·', '·']]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))

def verificar_ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '·' or \
           tablero[0][i] == tablero[1][i] == tablero[2][i] != '·':
            return tablero[i][i]

    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '·' or \
       tablero[0][2] == tablero[1][1] == tablero[2][0] != '·':
        return tablero[1][1]

    return None

def jugada_valida(tablero, fila, columna):
    return 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == '·'

def realizar_jugada(tablero, fila, columna, jugador):
    tablero[fila][columna] = jugador
