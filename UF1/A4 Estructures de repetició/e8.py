"""
descripción: el programa demanarà per teclat números fins que introduïm el 0.
Quan acabi el programa donarà la informació següent:
- La suma dels números que estan dins de l'interval SENSE ser cap dels valors indicats com a límit inferior o límit superior  (interval obert)
- Quants números són fora de l'interval.
- Informar de si hem introduït algun número que sigui igual al límit inferior o al límit superior de l'interval, o no.
"""
limI = int(input())
limS = int(input())
suma = 0
fora = 0
enLim = False

while limI > limS:
    limI = int(input())
    limS = int(input())

num = int(input())
while num != 0:
    num = int(input())
    if num > limI and num < limS:
        suma += num
    elif num < limI or num > limS:
        fora += 1
    elif num == limI or num == limS:
        enLim = True
print(f"suma de fora {suma}")
if enLim == True:
    print()
else:
    print()