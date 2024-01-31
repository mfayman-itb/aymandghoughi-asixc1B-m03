lst = input().split()
lstF = [False, False, False, False, False, False, False, False, False, False, False]
i = 0
while i < len(lst) and int(lst[i]) != -1:
    pressB = int(lst[i])
    lstF[pressB] = not lstF[pressB]
    i += 1
print(lstF)
