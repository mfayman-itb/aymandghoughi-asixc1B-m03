"""
Rafael Guiotto Silva
02/04/24

input
"""
# region funciones
def get_coords():
    while True:
        coords = input().split(" ")
        if len(coords) == 2:
            if coords[0].isdigit() and coords[1].isdigit():
                if 2 >= int(coords[0]) >= 0 and 2 >= int(coords[1]) >= 0:
                    return coords
                else:
                    print("valor fuera de tabla")
            else:
                print("valores incorrecto")
        else:
            print("introduce 2 coordenadas")
# endregion
