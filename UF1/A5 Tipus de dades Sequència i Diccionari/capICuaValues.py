num = int(input())
lst = input().split()

if len(lst) != num:
    print("numero de valors incorrecte")
if lst[::-1] == lst:
    print("cap i cua")
else:
    print("pinga")
