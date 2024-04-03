"""
Rafael Guiotto Silva
07/03/2024

"""
import SystemColors

def get_rectangle():
    rectangleList = []
    Exit = False
    while not Exit:
        rectangle = input().split(" ")
        if rectangle[0] != ";Q":
                if len(rectangle) == 3:
                    if rectangle[0].upper() in SystemColors.COLOR_CODES:
                        if rectangle[1].isdigit() and rectangle[2].isdigit():
                            if int(rectangle[1]) > 0 and int(rectangle[2]) > 0:
                                rectangulo = [rectangle[0], int(rectangle[1]), int(rectangle[2])]
                                rectangleList.append(rectangulo)
                            else:
                                print("la largada y anchura deben ser superiores a 0")
                        else:
                            print("la largada y anchura deben ser numeros")
                    else:
                        print("color incorrecto")
                else:
                    print("faltan argumentos")
        else:
            Exit = True

    do_rectangle(rectangleList)


def do_rectangle(rectangulos):
    shape = "X"
    for r in range(len(rectangulos)):
        color = SystemColors.COLOR_CODES[rectangulos[r][0].upper()]
        x = rectangulos[r][1]
        y = rectangulos[r][2]
        for i in range(y):
            for j in range(x):
                print(color + shape, end="")
            print()
        print()
