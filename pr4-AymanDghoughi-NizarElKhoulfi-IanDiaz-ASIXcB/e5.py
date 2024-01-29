""""
Ayman Dghoughi, Ian Díaz, Nizar ElKhoulfi
30/11/2023
M03 UF1 pp4
Descripció: Programa que realitza la multiplicació, de dos nombres sencers, mitjançant sumes.
"""

try:
    nombres = input("Introdueix dos nombres a sumar separats per un espai: ")
    nums = nombres.split()
    resultat = 0
    while len(nums) != 2:
        nombres = input("Introdueix dos nombres a sumar separats per un espai: ")
        nums = nombres.split()

    for i in range(1, int(nums[1]) + 1):
        resultat += int(nums[0])
    print(resultat)
except Exception as e:
    if ValueError:
        print("Si us plau, introdueïx dos nombres.")
    else:
        print(e)
