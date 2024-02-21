""""
Ayman Dghoughi, Ian Díaz, Nizar ElKhoulfi
30/11/2023
M03 UF1 pp4
Descripció: Programa que demana a l'usuari la introducció de 10 nombres
sencers i mostra quants són positius, quants negatius i quants zero.
"""

try:
    nombres = input("Introdueix 10 nombres enters separats per espais: ")
    nums = nombres.split()
    positius = 0
    negatius = 0
    zeros = 0
    while len(nums) != 10:
        nombres = input("Introdueix 10 nombres enters separats per espais: ")
        nums = nombres.split()
    for num in nums:
        if int(num) > 0:
            positius += 1
        elif int(num) < 0:
            negatius += 1
        else:
            zeros += 1

    print("Has introduït " + str(positius) + " nombre/s positius, " + str(negatius) + " negatius, i " + str(zeros) + " zeros.")
except Exception as e:
    if ValueError:
        print("Si us plau, introdueix només nombres enters.")
    else:
        print(e)
