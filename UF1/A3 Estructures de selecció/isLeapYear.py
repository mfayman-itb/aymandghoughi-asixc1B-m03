any = int(input())

if any % 4 == 0 or any % 400 == 0:
    print(f"{any} es un any de traspas.")
else:
    print(f"{any} no es un any de traspas.")
