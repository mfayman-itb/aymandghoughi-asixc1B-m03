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