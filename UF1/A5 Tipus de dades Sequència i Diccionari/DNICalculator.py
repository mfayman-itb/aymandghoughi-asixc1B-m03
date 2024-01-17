try:
    num = input()
    LETTER = ("T","R","W","A","G","M","Y","F","P","D","X","B","N",
              "J","Z","S","Q","V","H","L","C","K","E")
    if len(num) == 8:
        fnum = int(num) % 23
        print(LETTER[fnum])
    else:
        print("dni incorrecte")
except Exception as e:
    print(e)
