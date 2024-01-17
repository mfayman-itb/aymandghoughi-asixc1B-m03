try:
    num = int(input())
    LETTER = ("T","R","W","A","G","M","Y","F","P","D","X","B","N",
              "J","Z","S","Q","V","H","L","C","K","E")
    if len(str(num)) == 8:
        fnum = num % 23
        print(LETTER[fnum])
    else:
        print("dni incorrecte")
except Exception as e:
    print(e)
