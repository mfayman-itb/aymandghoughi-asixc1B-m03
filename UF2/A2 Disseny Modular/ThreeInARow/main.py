from tablero import inicializar_tablero, mostrar_tablero, verificar_ganador, jugada_valida, realizar_jugada
from jugador import turno_jugador, cambiar_jugador

def jugar_tres_en_raya():
    tablero = inicializar_tablero()
    jugador = 'X'

    while True:
        mostrar_tablero(tablero)
        print("Turno del jugador", jugador)
        fila, columna = turno_jugador()

        if jugada_valida(tablero, fila, columna):
            realizar_jugada(tablero, fila, columna, jugador)
            ganador = verificar_ganador(tablero)
            if ganador:
                mostrar_tablero(tablero)
                print("¡El jugador", ganador, "ha ganado!")
                break
            elif all('·' not in fila for fila in tablero):
                mostrar_tablero(tablero)
                print("¡Empate!")
                break
            jugador = cambiar_jugador(jugador)
        else:
            print("Movimiento no válido. Inténtalo de nuevo.")

if __name__ == "__main__":
    jugar_tres_en_raya()
