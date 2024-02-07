try:
    lst = input().split()
    lstF = [0,0,0,0,0,0,0,0,0,0,0]
    i = 0
    while int(lst[i]) != -1:
        lstF[int(lst[i])] += 1
        i += 1
    print(lstF)
except Exception as e:
    print(e)
