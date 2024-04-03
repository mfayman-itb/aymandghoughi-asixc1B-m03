"""
Rafael Guiotto Silva
02/04/24

cuerpo del codigo
"""
# region imports
import Coords
# endregion
# region funciones
table = [["·", "·", "·"],
         ["·", "·", "·"],
         ["·", "·", "·"]]
def play():
    Exit = False
    turns = 9
    while not Exit and turns != 0:
        coords = Coords.get_coords()
        if table[int(coords[0])][int(coords[1])] == "·":
            if turns % 2 == 0:
                table[int(coords[0])][int(coords[1])] = "0"
            else:
                table[int(coords[0])][int(coords[1])] = "X"
            turns -= 1
            show_table()
            if turns <= 6:
                winner = check_win()
                print(winner)
                if winner != None:
                    Exit = True
        else:
            print("posición ocupada")
            show_table()
    show_winner(winner)


def show_table():
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end=" ")
        print()

def check_win():
    winner = None
    for horizontal in range(len(table)):
        if table[horizontal] == ["X", "X", "X"]:
            winner = 1
        if table[horizontal] == ["0", "0", "0"]:
            winner = 2
    if winner == None:
        for vertical in range(len(table)):
            if table[0][vertical] == table[1][vertical] == table[2][vertical] == "X":
                winner = 1
            if table[0][vertical] == table[1][vertical] == table[2][vertical] == "0":
                winner = 2
    if winner == None:
        if table[0][0] == table[1][1] == table[2][2] == "X":
            winner = 1
        if table[0][0] == table[1][1] == table[2][2] == "0":
            winner = 2

        elif table[0][2] == table[1][1] == table[2][0] == "X":
            winner = 1
        elif table[0][2] == table[1][1] == table[2][0] == "0":
            winner = 2
    return winner

def show_winner(winner):
    if winner == 1:
        print("=========================\n player 1 [x] Wins ! \n=========================")
    elif winner == 2:
        print("=========================\n player 2 [0] Wins ! \n=========================")
    else:
        print("=========================\n EMPATE \n=========================")
# endregion
