"""
descripción: no acabado
"""
diners = float(input())

if diners >= 500:
    r = diners / 500
    print(f"{int(r)} billets de 500")
    a = diners - (500 * r)
if a / 200 != 0:
    r2 = a / 200
    print(f"{int(r2)} billets de 200")
    b = a - (200 * r2)
