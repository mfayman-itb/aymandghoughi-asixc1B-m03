try:
    BLANC = "B"
    NEGRE = "N"
    pos = input("Introduce una posición para el alfil con dos números separados por un espacio (y x): ").split()
    while int(pos[0]) < 1 or int(pos[0]) > 8 or int(pos[1]) > 8 or int(pos[1]) < 1:
        pos = input("Introduce una posición para el alfil con dos números separados por un espacio (y x): ").split()
    for i in range(1, 9):
        for j in range(1, 9):
            if i == int(pos[0]) and j == int(pos[1]):
                print("*", end=" ")
            elif j == int(pos[1]) - (int(pos[0]) - i) or j == int(pos[1]) + (int(pos[0]) - i):
                print("*", end=" ")
            elif (i + j) % 2 == 0:
                print(BLANC, end=" ")
            else:
                print(NEGRE, end=" ")
            print(" ", end="")
        print()
except Exception as e:
    if ValueError:
        print("Introduce un valor de coordenada correcto.")
    else:
        print(e)