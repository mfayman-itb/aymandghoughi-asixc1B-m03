MIDA = 10
lst = input().split()

mult = sum(int(lst[x]) * (x + 1) for x in range(MIDA - 1))  # Reduje el rango para excluir el último dígito

if mult % 11 == 10:
    mom = 'X'
else:
    mom = str(mult % 11)

if mom == lst[-1] or (mom == 'X' and lst[-1] == '0'):  # Corregí la condición para comparar con '0' en lugar de '10'
    print(True)
else:
    print(False)
