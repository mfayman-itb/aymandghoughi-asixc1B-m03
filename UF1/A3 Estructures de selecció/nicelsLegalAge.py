"""
descripción: eres mayor de edad o no
"""
try:
    edat = int(input("How old r u? "))

    if edat >= 18 and edat <= 120:
        print("Eres mayor de edad")
    elif edat > 120:
        print("U gotta be a zombie")
    else:
        print("Cuidao con lo que haces pequeñin")
except Exception as e:
    if ValueError:
        print("Put a number ma G")
    else:
        print(e)