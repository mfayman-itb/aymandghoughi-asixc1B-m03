def turno_jugador():
    try:
        entrada = input()
        fila, columna = map(int, entrada.split())
        return fila, columna
    except ValueError:
        print("Por favor, introduce números válidos.")
        return turno_jugador()

def cambiar_jugador(jugador_actual):
    return 'O' if jugador_actual == 'X' else 'X'
