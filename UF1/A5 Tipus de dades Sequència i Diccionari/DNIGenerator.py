try:
    dniNums = int(input())

    while len(str(dniNums)) != 8:
        dniNums = int(input())

    TUP = ("T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S",
           "Q","V","H","L","C","K","E")

    div = dniNums % 23
    lletra = TUP[div]
    print(lletra)
except (ValueError, TypeError) as e:
    print("Introdueix només nombres enters... Excepció:")
    print(e)