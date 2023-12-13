"""
descripción: Programa per crear una serp Python a mida.
"""
largo = int(input())
CAP= "....\...../...."
ULLS= "...╚⊙ ⊙╝..."
COS = "═(███)═"
CUA =  " ═V═ "
count = 1

print(CAP)
print("  " + ULLS)
for i in range(largo):
    print("    " + COS)
    count += 1
    if count % 2 == 0:
        print("   " + COS)
    elif count % 2 != 0:
        print("   " + COS)
print("     " + CUA)
