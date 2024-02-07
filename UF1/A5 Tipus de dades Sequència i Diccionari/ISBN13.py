MIDA = 13
lst = input().split()
i = 0
sum = 0
for i in range(MIDA - 1):
    if i % 2 == 0:
        sum = sum + (int(lst[i]) * 1)
    else:
        sum = sum + (int(lst[i]) * 3)
if sum % 10 == 0:
    mom = 0
else:
    for i in range(1,10):
        if (sum + i) % 10 == 0:
            mom = i
if int(lst[12]) == mom:
    print(True)
else:
    print(False)
