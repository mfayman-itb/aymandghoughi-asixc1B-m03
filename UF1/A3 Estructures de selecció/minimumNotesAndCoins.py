diners = float(input())

if diners >= 500:
    r = diners / 500
    print(f"{int(r)} billets de 500")
    a = diners - 500
elif r / 200 != 0:
    r2 = a / 200
    print(f"{int(r2)} billets de 200")
    b = a - 200
elif r2 / 100 != 0:
    r3 = b / 100
    print(f"{int(r3)} billets de 100")
    c = b - 100
elif: