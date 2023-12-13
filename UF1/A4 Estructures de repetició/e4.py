"""
descripción: programa informarà de quants són més grans que 0, menors que 0 i iguals a 0.
"""
try:
    length = int(input("Quants numeros vols introduir? "))
    nombres = input(f"Introdueix {length} nombres enters separats per espais: ")
    nums = nombres.split()
    positius = 0
    negatius = 0
    zeros = 0
    while len(nums) != length:
        nombres = input(f"Introdueix {length} nombres enters separats per espais: ")
        nums = nombres.split()
    for num in nums:
        if int(num) > 0:
            positius += 1
        elif int(num) < 0:
            negatius += 1
        elif int(num) == 0:
            zeros += 1

    print("Has introduït " + str(positius) + " nombre/s positiu/s, " + str(negatius) + " negatiu/s i " + str(zeros) + " zero/s.")
except Exception as e:
    if ValueError:
        print("Si us plau, introdueix només nombres enters.")
    else:
        print(e)