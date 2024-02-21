try:
    num = int(input())
    mult2 = False
    mult5 = False
    if num % 2 == 0:
        mult2 = True
    elif num % 5 == 0:
        mult5 = True
    print(f'Múltiple de 2: {mult2}\nMúltiple de 5: {mult5}')
except (ValueError, TypeError) as e:
    print("Introduce un numero entero...")
    print(e)